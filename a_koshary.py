# author: Yash Gupta
# created: 30.04.2026 20:06:04

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


def solve():
    a, b = rinp()
    if a % 2 and b % 2:
        print("NO")
    else:
        print("YES")


def main():
    t = rint()  # remove if single test case
    for _ in range(t):
        solve()


if __name__ == "__main__":
    # sys.setrecursionlimit(3 * 10**5)
    main()
