# author: Yash Gupta
# created: 26.04.2026 22:49:31

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
    n = rint()
    arr = rl()
    sum = 0
    ugly = 0
    for a in arr:
        if sum == a:
            ugly = 1
            break
        sum += a
    if ugly == 1:
        arr.sort()
        sum = 0
        for a in arr:
            if sum == a:
                print("NO")
                break
    else:
        print("YES")
        print(arr)


def main():
    t = rint()  # remove if single test case
    for _ in range(t):
        solve()


if __name__ == "__main__":
    # sys.setrecursionlimit(3 * 10**5)
    main()
