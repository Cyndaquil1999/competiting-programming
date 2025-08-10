#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<USAGE
Usage: $(basename "$0") [-e EXT] <ATCODER_TASK_URL>
  -e EXT   出力拡張子（デフォルト: py）例: -e cpp / -e py
例:
  $(basename "$0") https://atcoder.jp/contests/abc048/tasks/abc048_a
  $(basename "$0") -e cpp https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_af
USAGE
}

ext="${AC_NEW_EXT:-py}"
while getopts ":e:h" opt; do
  case "$opt" in
    e) ext="${OPTARG#.}" ;;   # 先頭ドットは除去
    h) usage; exit 0 ;;
    \?) echo "invalid option: -$OPTARG" >&2; usage; exit 1 ;;
  esac
done
shift $((OPTIND-1))

[[ $# -ge 1 ]] || { usage; exit 1; }
url="$1"

# contest と task を抽出
contest="$(sed -n 's#^.*/contests/\([^/]\+\)/tasks/.*#\1#p' <<<"$url")"
task="$(sed -n 's#^.*/tasks/\([^/?#]\+\).*#\1#p' <<<"$url")"
if [[ -z "$contest" || -z "$task" ]]; then
  echo "URL を解析できませんでした: $url" >&2
  exit 1
fi

# 出力ディレクトリ決定
if [[ "$contest" =~ ^(abc|arc|agc)([0-9]+)$ ]]; then
  prefix="${BASH_REMATCH[1]}"
  num="${BASH_REMATCH[2]}"
  round=$(printf "%03d" "$((10#$num))")  # 8進誤解釈対策
  outdir="$prefix/$round"
else
  outdir="other/$contest"
fi

mkdir -p "$outdir"
outfile="$outdir/$task.$ext"

if [[ -e "$outfile" ]]; then
  echo "既に存在します: $outfile"
else
  # 拡張子ごとの生成
  case "$ext" in
    py)
      : > "$outfile" ;;                 # Python は空ファイル
    cpp|cc|cxx)
      cat > "$outfile" <<EOF
// URL: ${url}
// contest: ${contest}
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // TODO: 実装

    return 0;
}
EOF
      ;;
    *)
      : > "$outfile" ;;
  esac
  echo "created: $outfile"
fi

# samples ディレクトリと sample.in を用意
samples_dir="$outdir/samples"
mkdir -p "$samples_dir"

if command -v oj >/dev/null 2>&1; then
  # サンプルを取得（失敗してもスクリプトは続行）
  if ! oj download "$url" -d "$samples_dir" >/dev/null 2>&1; then
    echo "warn: oj download に失敗しました（$url）" >&2
  fi

  # 最初の .in を sample.in にコピー
  first_in="$(ls "$samples_dir"/*.in 2>/dev/null | sort | head -n 1 || true)"
  if [[ -n "${first_in:-}" ]]; then
    cp "$first_in" "$outdir/sample.in"
  else
    : > "$outdir/sample.in"
    echo "warn: サンプル入力が見つからなかったため、空の sample.in を作成しました" >&2
  fi
else
  : > "$outdir/sample.in"
  echo "warn: 'oj' が見つかりません。'pip install online-judge-tools' を推奨します。" >&2
fi

# 生成物を表示
echo "$outfile"
echo "$outdir/sample.in"

# 生成直後にエディタで開く（任意）
if [[ -n "${EDITOR:-}" ]]; then
  "$EDITOR" "$outfile"
fi
