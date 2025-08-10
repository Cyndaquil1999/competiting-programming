#!/usr/bin/env python3
import re
import os
import json
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).resolve().parents[1]
README = REPO_ROOT / "README.md"

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

# other/ の特殊マッピング（ディレクトリ名 -> contest slug / task prefix）
OTHER_CONTEST_MAP = {
    # Educational DP Contest
    "edpc": {"contest": "dp", "task_prefix": "dp_"},
    # Panasonic 2020
    "パナコン2020": {"contest": "panasonic2020", "task_prefix": "panasonic2020_"},
    # Sumitomo Trust 2019
    "三井住友信託銀行プロコン2019": {"contest": "sumitrust2019", "task_prefix": "sumitrust2019_"},
    # Hitachi 2020
    "日立製作所 社会システム事業部 プログラミングコンテスト2020": {
        "contest": "hitachi2020",
        "task_prefix": "hitachi2020_",
    },
    # code-festival 2016 qual B
    "codefestival2016qualb": {
        "contest": "code-festival-2016-qualb",
        "task_prefix": "code_festival_2016_qualb_",
    },
    # JOI/JOIG は下のロジックで自動判定するのでここには置かない
}

ASCII_HYPHEN_RE = re.compile(r"^[a-z0-9-]+$")


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


def parse_entry(rel: Path):
    """
    1ファイルから表示用情報を抽出。
    戻り値 dict:
      {
        group: 'abc'|'arc'|'agc'|'other',
        round: '048' or subcontest name,
        prob: 'A'.. or '—',
        contest_slug: 'abc048' / 'math-and-algorithm' / 'dp' / ... (Taskリンク用),
        task_slug: 'abc048_a' / 'math_and_algorithm_af' / 'dp_a' / ... (Taskリンク用)
      }
    """
    parts = rel.parts
    if len(parts) < 2:
        return None
    group = parts[0].lower()
    if group in {"abc", "arc", "agc"}:
        if len(parts) < 3:
            return None
        round_dir = parts[1]
        fname = parts[-1]
        stem = Path(fname).stem
        m_let = re.search(r"([a-fA-F])", stem)
        letter = m_let.group(1).lower() if m_let else None

        m_num = re.search(r"(\d+)", round_dir)
        round_ = f"{int(m_num.group(1)):03d}" if m_num else round_dir

        contest_slug = f"{group}{int(round_):03d}" if round_.isdigit(
        ) else f"{group}{round_}"
        task_slug = f"{contest_slug}_{letter}" if letter else None

        return {
            "group": group,
            "round": round_,
            "prob": (letter or "—").upper(),
            "contest_slug": contest_slug,
            "task_slug": task_slug,
        }

    # other/
    if group == "other":
        if len(parts) < 3:
            return None
        subcontest = parts[1]
        fname = parts[-1]
        # 例: math_and_algorithm_af / A / joi2023_yo1a_d / 010 など
        stem = Path(fname).stem

        # 1) 既知のマッピング
        if subcontest in OTHER_CONTEST_MAP:
            mapping = OTHER_CONTEST_MAP[subcontest]
            contest_slug = mapping["contest"]
            prefix = mapping.get("task_prefix", "")
            # stem が単文字(A/B/...)なら letter を使う、それ以外は stem をそのまま
            if re.fullmatch(r"[A-Za-z]", stem):
                letter = stem.lower()
                task_slug = f"{prefix}{letter}"
                prob = stem.upper()
            else:
                # すでに完全スラッグなら prefix 不要、そうでなければ prefix+stem
                if stem.startswith(prefix):
                    task_slug = stem
                else:
                    task_slug = f"{prefix}{stem}"
                # 問題記号は末尾の _x を拾う
                m_last = re.search(r"_([a-z])$", task_slug)
                prob = (m_last.group(1).upper() if m_last else "—")
            return {
                "group": group,
                "round": subcontest,
                "prob": prob,
                "contest_slug": contest_slug,
                "task_slug": task_slug,
            }

        # 2) JOI/JOIG 系（例: joi2023_yo1a_d, joig2023_b）
        if stem.startswith("joi") or stem.startswith("joig"):
            # joi2023_yo1a_d → contest joi2023yo1a / task joi2023_yo1a_d
            # joig2023_b     → contest joig2023     / task joig2023_b
            parts_ = stem.split("_")
            if len(parts_) >= 2:
                contest_slug = "".join(parts_[:-1])  # 最後の(問題記号)以外を結合
                task_slug = stem
                prob = parts_[-1].upper() if len(parts_[-1]) == 1 else "—"
                return {
                    "group": group,
                    "round": subcontest,
                    "prob": prob,
                    "contest_slug": contest_slug,
                    "task_slug": task_slug,
                }

        # 3) ASCII ハイフンだけの subcontest は、そのまま contests/<subcontest>/tasks/<stem> を試す
        #    例: math-and-algorithm / abc-like 以外でも slug がそのままならOK
        if ASCII_HYPHEN_RE.fullmatch(subcontest) and re.search(r"_", stem):
            contest_slug = subcontest
            task_slug = stem
            m_last = re.search(r"_([a-z])$", stem)
            prob = (m_last.group(1).upper() if m_last else "—")
            return {
                "group": group,
                "round": subcontest,
                "prob": prob,
                "contest_slug": contest_slug,
                "task_slug": task_slug,
            }

        # 4) dp 風：ディレクトリが edpc じゃないけど、ファイル名が dp_a 等ならそのまま
        if re.fullmatch(r"dp_[a-z]", stem):
            return {
                "group": group,
                "round": subcontest,
                "prob": stem[-1].upper(),
                "contest_slug": "dp",
                "task_slug": stem,
            }

        # 5) どうしても特定できない場合はリンクなし
        return {
            "group": group,
            "round": subcontest,
            "prob": "—",
            "contest_slug": None,
            "task_slug": None,
        }

    return None


def task_url(contest_slug: str | None, task_slug: str | None):
    if not contest_slug or not task_slug:
        return None
    return f"https://atcoder.jp/contests/{contest_slug}/tasks/{task_slug}"


def build_table_rows():
    rows = []
    per_contest = defaultdict(int)
    per_lang = defaultdict(int)

    for p in iter_solution_files():
        rel = p.relative_to(REPO_ROOT)
        ext = p.suffix.lower()
        lang = LANG_MAP.get(ext, ext.lstrip("."))

        info = parse_entry(rel)
        if not info:
            continue

        per_contest[info["group"]] += 1
        per_lang[lang] += 1

        file_link = f"[{rel.as_posix()}]({rel.as_posix()})"
        url = task_url(info["contest_slug"], info["task_slug"])
        if url:
            task_cell = f"[{info['task_slug']}]({url})"
        else:
            task_cell = "—"

        # Contest列はグループ名（ABC/ARC/AGC/OTHER）、Round列にラウンドorサブコンテスト
        rows.append(
            {
                "contest": info["group"].upper(),
                "round": info["round"],
                "prob": info["prob"],
                "lang": lang,
                "file": file_link,
                "task": task_cell,
            }
        )

    # 並び順: contest -> round昇順(数字優先) -> prob
    def round_key(v):
        r = v["round"]
        return (0, int(r)) if isinstance(r, str) and r.isdigit() else (1, str(r))

    rows.sort(key=lambda r: (r["contest"], round_key(r), r["prob"]))
    return rows, per_contest, per_lang


def make_markdown():
    rows, per_contest, per_lang = build_table_rows()

    total = sum(per_contest.values())
    contest_summary = " | ".join(
        f"{k.upper()}: {v}" for k, v in sorted(per_contest.items()))
    lang_summary = " | ".join(f"{k}: {v}" for k, v in sorted(per_lang.items()))

    lines = []
    lines.append("| Contest | Round | Problem | Lang | File | Task |")
    lines.append("|---|---:|:---:|:---:|---|---|")
    for r in rows:
        lines.append(
            f"| {r['contest']} | {r['round']} | {r['prob']} | {r['lang']} | {r['file']} | {r['task']} |"
        )
    return "\n".join(lines) + "\n"


def replace_section_in_readme(new_md: str):
    if not README.exists():
        README.write_text(
            f"# Solutions\n\n{START_MARK}\n{new_md}{END_MARK}\n", encoding="utf-8"
        )
        return True
    original = README.read_text(encoding="utf-8")
    if START_MARK in original and END_MARK in original:
        import re as _re

        pattern = _re.compile(_re.escape(START_MARK) +
                              r".*?" + _re.escape(END_MARK), _re.DOTALL)
        updated = pattern.sub(f"{START_MARK}\n{new_md}{END_MARK}", original)
    else:
        updated = original.rstrip() + f"\n\n{START_MARK}\n{new_md}{END_MARK}\n"
    if updated != original:
        README.write_text(updated, encoding="utf-8")
        return True
    return False


# --- 既存のバッジ出力（そのまま） ---
BADGE_DIR = REPO_ROOT / "docs" / "badges"
BADGE_DIR.mkdir(parents=True, exist_ok=True)


def write_badge_json(total, per_contest, per_lang):
    def badge(label, message, color="blue"):
        return {"schemaVersion": 1, "label": label, "message": str(message), "color": color}

    (BADGE_DIR / "total.json").write_text(
        json.dumps(badge("solved", total, "blue")), encoding="utf-8"
    )
    for key in ("abc", "arc", "agc", "other"):
        (BADGE_DIR / f"{key}.json").write_text(
            json.dumps(
                badge(key.upper(), per_contest.get(key, 0), "informational")),
            encoding="utf-8",
        )
    lang_key_map = {"Python": "python", "C++": "cpp",
                    "JavaScript": "javascript", "TypeScript": "typescript"}
    for lang_label, short in lang_key_map.items():
        if lang_label in per_lang:
            (BADGE_DIR / f"{short}.json").write_text(
                json.dumps(badge(lang_label, per_lang[lang_label], "success")), encoding="utf-8"
            )


def main():
    md = make_markdown()
    changed = replace_section_in_readme(md)

    # バッジ更新
    _, per_contest, per_lang = build_table_rows()
    total = sum(per_contest.values())
    write_badge_json(total, per_contest, per_lang)

    print("README updated:" if changed else "No changes.")


if __name__ == "__main__":
    main()
