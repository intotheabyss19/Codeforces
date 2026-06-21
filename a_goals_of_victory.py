# author: Yash Gupta
# created: 02.05.2026 01:53:01


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    print(-sum(a))


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
