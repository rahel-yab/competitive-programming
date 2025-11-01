# Problem: k-Factorization - https://codeforces.com/problemset/problem/797/A

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
def factorization(k):
    factors = []
    d = 2 
    while d * d <= k:
        while k % d == 0:
            factors.append(d)
            k //= d
    
        d += 1
    if k >= 2:
        factors.append(k)

    return factors

def solve():
    n , k = mi()
    if k == 1:
        print(n)
        return
    fs = factorization(n)
    if len(fs) < k:
        print(-1)
        return
    if len(fs) == k:
        print(*fs)
        return
    ans = fs[:k]
    left = fs[k:]
    if left:
        prod = 1
        for num in left:
            prod *= num
        ans[-1] *= prod
    print(*ans)

    return

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




 