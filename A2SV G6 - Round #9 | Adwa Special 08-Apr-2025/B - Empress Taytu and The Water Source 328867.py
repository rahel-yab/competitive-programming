# Problem: B - Empress Taytu and The Water Source - https://codeforces.com/gym/601269/problem/B

import math
from math import gcd
import sys, threading
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
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
# =========================================

"""
# Note

"""

def solve():
    n , k = mi()
    demand = li()
    time = li()

    def validate(mid):
        summ = 0
        for i in range(n):
            add = math.ceil(demand[i]/mid)
            summ += (add *time[i])
        return summ <= k
    
    low = 1
    high = max(demand)
    flag = False
    while low <= high:
        mid = (low+high) // 2
        if validate(mid):
            high = mid-1
            flag = True
        else:
            low = mid + 1
    if flag:
        print(low)
    else:
        print(-1)

# =========================================
def main():
    t = ii()
    for _ in range(t):
        solve()

# =========================================
main()
# if __name__ == '__main__':
#   sys.setrecursionlimit(1 << 30)
#   threading.stack_size(1 << 27)
#   main_thread = threading.Thre ad(target=main)
#   main_thread.start()
#   main_thread.join()