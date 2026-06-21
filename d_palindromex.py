# author: Yash Gupta
# created: 30.04.2026 20:39:06

import sys
from sys import stdin
from math import gcd, lcm, isqrt, comb
from collections import defaultdict, Counter, deque
from itertools import accumulate
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from functools import lru_cache, reduce

input = stdin.readline
inp = lambda: input().split()
inpi = lambda d_type: map(int, inp())
inpf = lambda: map(float, inp())
rint = lambda: int(input())
rinp = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rg = lambda n: [rl() for _ in range(n)]
prl = lambda a: print(*a)

INF, MOD, MOD2, ALPHA = float("inf"), 10**9 + 7, 998244353, "abcdefghijklmnopqrstuvwxyz"


def checkpal(arr, l, r):
    for i in range(r - l + 1):
        if arr[l + i] != arr[r - i]:
            return 0
    return 1


def solve():
    n = rint()
    a = rl()
    length = 2 * n
    present = [False] * (n + 1)
    max_m = 0

    for c in range(2 * length - 1):
        left = c // 2
        right = (c + 1) // 2

        while left >= 0 and right < length and a[left] == a[right]:
            left -= 1
            right += 1

        left += 1
        right -= 1

        if left <= right:
            for i in range(left, right + 1):
                present[a[i]] = True

            mex = 0
            while mex <= n and present[mex]:
                mex += 1

            max_m = max(max_m, mex)

            for i in range(left, right + 1):
                present[a[i]] = False

    print(max_m)


def main():
    t = rint()  # remove if single test case
    for _ in range(t):
        solve()


if __name__ == "__main__":
    # sys.setrecursionlimit(3 * 10**5)
    main()
