#!/usr/bin/env python3
import re
import os
import json
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).resolve().parents[1]
README = REPO_ROOT / "README.md"

BADGE_DIR = REPO_ROOT / "docs" / "badges"
BADGE_DIR.mkdir(parents=True, exist_ok=True)

# ここに表を差し込むマーカーをREADMEに用意しておく
START_MARK = "<!-- solved:start -->"
END_MARK = "<!-- solved:end -->"


LANG_MAP = {
    ".py": "Python",
    ".cpp": "C++",
    ".cc": "C++",
    ".cxx": "C++",
    ".ts": "TypeScript",
    ".js": "JavaScript",
}


def detect_contest_round_problem(path: Path):
    """
    返却: (contest, round, problem_letter)
    - abc/123/b.py           -> ('abc', '123', 'b')
    - abc/045/045c.py        -> ('abc', '045', 'c')
    - arc/084/084c.py        -> ('arc', '084', 'c')
    - agc/003/A.py           -> ('agc', '003', 'a')
    - その他は best-effort（problem_letter はファイル名から単語先頭の a~f を拾う）
    """
    parts = path.parts
    # 期待: <root>/<contest>/<round>/<file>
    if len(parts) < 3:
        return None

    contest = parts[-3].lower()  # abc, arc, agc, other...
    round_ = parts[-2]

    fname = parts[-1]
    stem = Path(fname).stem  # 049c, b, c_1 など
    m = re.search(r'([a-fA-F])', stem)
    letter = m.group(1).lower() if m else None

    # 大文字ファイル(A.cpp)対応
    if letter is None and re.fullmatch(r'[A-F]', stem):
        letter = stem.lower()

    # round は 3桁ゼロ埋めしたい（数字のみ想定）
    m_round = re.search(r'(\d+)', round_)
    if m_round:
        round_ = f"{int(m_round.group(1)):03d}"
    else:
        # typical90など数字じゃないケースはそのまま
        pass

    return (contest, round_, letter)


def atcoder_task_url(contest, round_, letter):
    """
    ABC/ARC/AGCは規則的なのでリンク生成（それ以外はNone）
    例: https://atcoder.jp/contests/abc139/tasks/abc139_b
    """
    if contest not in ("abc", "arc", "agc"):
        return None
    if not letter:
        return None
    slug = f"{contest}{int(round_):03d}"
    return f"https://atcoder.jp/contests/{slug}/tasks/{slug}_{letter}"


def iter_solution_files():
    targets = ["abc", "arc", "agc", "other"]
    exts = set(LANG_MAP.keys())
    for t in targets:
        base = REPO_ROOT / t
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if p.is_file() and p.suffix.lower() in exts:
                yield p


def build_table_rows():
    rows = []
    per_contest = defaultdict(int)
    per_lang = defaultdict(int)

    for p in iter_solution_files():
        rel = p.relative_to(REPO_ROOT)
        ext = p.suffix.lower()
        lang = LANG_MAP.get(ext, ext.lstrip("."))
        info = detect_contest_round_problem(rel)
        if not info:
            continue
        contest, round_, letter = info

        per_contest[contest] += 1
        per_lang[lang] += 1

        # GitHub 上のファイルへの相対リンク
        file_link = f"[{rel.as_posix()}]({rel.as_posix()})"

        # AtCoder 問題リンク（作れない場合は "—"）
        task_link = atcoder_task_url(contest, round_, letter)
        task_cell = f"[{contest}{round_} {letter}]" if task_link else "—"
        if task_link:
            task_cell = f"[{contest}{round_} {letter}]({task_link})"

        rows.append({
            "contest": contest.upper(),
            "round": round_,
            "prob": (letter or "—").upper(),
            "lang": lang,
            "file": file_link,
            "task": task_cell
        })

    # 並び順: contest -> round昇順 -> problem昇順
    rows.sort(key=lambda r: (r["contest"], int(
        r["round"]) if r["round"].isdigit() else 10**9, r["prob"]))
    return rows, per_contest, per_lang


def make_markdown():
    rows, per_contest, per_lang = build_table_rows()

    total = sum(per_contest.values())
    contest_summary = " | ".join(
        f"{k.upper()}: {v}" for k, v in sorted(per_contest.items()))
    lang_summary = " | ".join(f"{k}: {v}" for k, v in sorted(per_lang.items()))

    lines = []
    lines.append("")
    lines.append("| Contest | Round | Problem | Lang | File | Task |")
    lines.append("|---|---:|:---:|:---:|---|---|")

    for r in rows:
        lines.append(
            f"| {r['contest']} | {r['round']} | {r['prob']} | {r['lang']} | {r['file']} | {r['task']} |")

    return "\n".join(lines) + "\n"


def replace_section_in_readme(new_md: str):
    if not README.exists():
        # READMEがない場合は新規作成
        README.write_text(
            f"""# Solutions

{START_MARK}
{new_md}{END_MARK}
""",
            encoding="utf-8"
        )
        return True

    original = README.read_text(encoding="utf-8")
    if START_MARK in original and END_MARK in original:
        pattern = re.compile(
            re.escape(START_MARK) + r".*?" + re.escape(END_MARK),
            re.DOTALL
        )
        updated = pattern.sub(f"{START_MARK}\n{new_md}{END_MARK}", original)
    else:
        # マーカーがない場合は末尾に追記
        updated = original.rstrip() + f"\n\n{START_MARK}\n{new_md}{END_MARK}\n"

    if updated != original:
        README.write_text(updated, encoding="utf-8")
        return True
    return False


def write_badge_json(total, per_contest, per_lang):
    """
    Shields endpoint 形式の JSON を複数出力する。
    - docs/badges/total.json
    - docs/badges/abc.json / arc.json / agc.json
    - docs/badges/python.json / cpp.json （存在すれば）
    """
    def badge(label, message, color="blue"):
        return {
            "schemaVersion": 1,
            "label": label,
            "message": str(message),
            "color": color
        }

    # 総数
    (BADGE_DIR / "total.json").write_text(
        json.dumps(badge("solved", total, "blue")), encoding="utf-8"
    )

    # コンテスト別
    for key in ("abc", "arc", "agc"):
        val = per_contest.get(key, 0)
        (BADGE_DIR / f"{key}.json").write_text(
            json.dumps(badge(key.upper(), val, "informational")), encoding="utf-8"
        )

    # 言語別（必要に応じて拡張）
    lang_key_map = {
        "Python": "python",
        "C++": "cpp",
        "JavaScript": "javascript",
        "TypeScript": "typescript",
    }
    for lang_label, short in lang_key_map.items():
        if lang_label in per_lang:
            (BADGE_DIR / f"{short}.json").write_text(
                json.dumps(badge(lang_label, per_lang[lang_label], "success")), encoding="utf-8"
            )


def main():
    md = make_markdown()

    # テーブル差し替え
    changed = replace_section_in_readme(md)

    # バッジ JSON も毎回更新
    rows, per_contest, per_lang = build_table_rows()
    total = sum(per_contest.values())
    write_badge_json(total, per_contest, per_lang)

    print("README updated:" if changed else "No changes.")


if __name__ == "__main__":
    main()
