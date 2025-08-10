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

ext="py"
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
  # ✗ round=$(printf "%03d" "$num")   # 063 が 8進扱いになり 051 になってしまう
  round=$(printf "%03d" "$((10#$num))")  # ← 10進に固定してゼロ埋め
  outdir="$prefix/$round"
else
  outdir="other/$contest"
fi

mkdir -p "$outdir"
outfile="$outdir/$task.$ext"

if [[ -e "$outfile" ]]; then
  echo "既に存在します: $outfile"
  echo "$outfile"
  exit 0
fi

# 拡張子ごとの生成
case "$ext" in
  py)
    # Python の雛型は不要 → 空ファイルを作成
    : > "$outfile"
    ;;
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
    # それ以外は空ファイルだけ作る
    : > "$outfile"
    ;;
esac

echo "created: $outfile"
echo "$outfile"
