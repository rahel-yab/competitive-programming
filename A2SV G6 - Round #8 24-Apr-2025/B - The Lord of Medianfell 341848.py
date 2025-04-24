# Problem: B - The Lord of Medianfell - https://codeforces.com/gym/599383/problem/B

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
   n, s = [int(i) for i in input().split()]
   m = n // 2 + 1 
   print(s // m) 
   


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