# 半開区間の発想で統一。is_palindrome をそのまま利用する版。

from typing import Iterable


def is_palindrome(s: str) -> bool:
    """s が回文なら True。スライス反転を使うシンプル実装。"""
    return s == s[::-1]


def has_pal_of_len(s: str, L: int) -> bool:
    """長さ L の回文部分文字列が s に存在するか。L は 1 以上。"""
    if L <= 0:
        raise ValueError("L must be >= 1")
    n = len(s)
    if L > n:
        return False
    # 区間は常に [i, i+L) で統一
    return any(is_palindrome(s[i:i+L]) for i in range(0, n - L + 1))


def longest_pal_len_by_slice(s: str) -> int:
    """is_palindrome を使う “長さ優先 + any” 版（読みやすさ最優先）。O(n^3) になりうる。"""
    for L in range(len(s), 0, -1):  # 長い順に見つけたら即 return
        if has_pal_of_len(s, L):
            return L
    return 0

# 任意: 速い版（中心展開）も置いておく。使わなければ無視でOK。


def longest_pal_len_center(s: str) -> int:
    """中心展開 O(n^2)。大きい入力用に。"""
    n = len(s)
    if n == 0:
        return 0

    def expand(l: int, r: int) -> int:
        while 0 <= l and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1
    best = 0
    for c in range(n):
        best = max(best, expand(c, c), expand(c, c + 1))
    return best


def longest_pal_len(s: str, prefer_fast: bool = False) -> int:
    """デフォは is_palindrome 利用版。大きい入力だけ速い版に切替えたいときは prefer_fast=True。"""
    if prefer_fast and len(s) > 400:
        return longest_pal_len_center(s)
    return longest_pal_len_by_slice(s)
