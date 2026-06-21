# author: Yash Gupta
# created: 14.03.2026 22:11:20

import sys
from sys import stdin
from math import gcd, lcm, isqrt, comb
from collections import defaultdict, Counter, deque
from itertools import accumulate
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from functools import lru_cache, reduce

input = stdin.readline
rint = lambda: int(input())
rinp = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rg = lambda n: [rl() for _ in range(n)]
prl = lambda a: print(*a)

INF, MOD = float("inf"), 10**9 + 7


def solve(): ...


def main():
    t = rint()  # remove if single test case
    for _ in range(t):
        solve()


if __name__ == "__main__":
    # sys.setrecursionlimit(3 * 10**5)
    main()
