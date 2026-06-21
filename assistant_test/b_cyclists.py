# author: Yash Gupta
# created: 14.03.2026 20:54:15

import sys
import os
from sys import stdin, stdout
from math import gcd, lcm, isqrt, log2, floor, ceil, comb, perm
from collections import defaultdict, Counter, deque
from itertools import accumulate, permutations, combinations, product
from bisect import bisect_left, bisect_right, insort
from heapq import heappush, heappop, heapify, nlargest, nsmallest
from functools import lru_cache, reduce
from typing import List, Tuple

# --- Fast I/O ---
input = stdin.readline  # replaces built-in input()


def inp():
    return input().split()


def inpi():
    return map(int, inp())


def inpf():
    return map(float, inp())


def rint():
    return int(input())


def rl():
    return list(inpi())  # read line as list of ints


def rll(n):
    return [rl() for _ in range(n)]  # n lines, each a list of ints


def rg(n, m):
    return [rl() for _ in range(n)]  # n x m grid


pr = print


def prl(a):
    print(*a)  # print list space-separated


def prc(a):
    print(*a, sep=",")  # print list comma-separated


# --- Constants ---
INF = float("inf")
MOD = 10**9 + 7
MOD2 = 998244353
ALPHA = "abcdefghijklmnopqrstuvwxyz"


# --- Utility ---
def chmin(a, b):
    return min(a, b)  # use as: val = chmin(val, candidate)


def chmax(a, b):
    return max(a, b)


def yes():
    print("YES")


def no():
    print("NO")


def yn(cond):
    print("YES" if cond else "NO")


# --- Solve ---
def solve():
    n, k, p, m = inpi()
    print("m", m)
    energy = rl()
    print("sum", sum(energy[:p]))
    wins = 0
    for e in energy:
        ...
    # first win condition
    # print("min", min(energy[:p]))
    print(m)

    pass


# --- Main ---
def main():
    t = rint()  # remove if single test case
    for _ in range(t):
        solve()


if __name__ == "__main__":
    # sys.setrecursionlimit(3 * 10**5)  # uncomment for deep recursion / DFS
    main()
