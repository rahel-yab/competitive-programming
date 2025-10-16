# Problem: Row GCD - https://codeforces.com/problemset/problem/1458/a

import math
import heapq
import sys, threading
from bisect import bisect_left, bisect_right
from collections import defaultdict, Counter, deque

input = lambda: sys.stdin.readline().rstrip()
def si():
    return input()
def ii():
    return int(input())
def lsi():
    return input().split()
def mi():
    return map(int, input().split())
def li():
    return list(map(int, input().split()))
yn = lambda condition: 'YES' if condition else 'NO'

# ========================================
# =========================================
def solve():
    n, m = mi()
    a = li()
    b = li()
    gcdd = 0
    for i in range(1,n):
        gcdd = math.gcd(gcdd, a[i]-a[i-1])
    ans = []
    for j in b:
        ans.append(math.gcd(gcdd, j+a[0]))
    print(*ans)
    

# =========================================
def main():
    t = 1
    for _ in range(t):
        solve()
main()

# if __name__ == '__main__':
#     sys.setrecursionlimit(1 << 25)
#     threading.stack_size(1 << 27)
#     thread = threading.Thread(target=main)
#     thread.start()
#     thread.join()





