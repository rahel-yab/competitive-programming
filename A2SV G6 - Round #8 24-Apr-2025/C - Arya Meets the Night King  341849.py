# Problem: C - Arya Meets the Night King  - https://codeforces.com/gym/599383/problem/C

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
    s , b = mi()
    attacking_powers = li()
    
    bases = []  
    for i in range(b):  
        d, g = mi()
        bases.append((d, g))  

    bases.sort()  

    defenses = [grid[0] for grid in bases]  
    golds = [grid[1] for grid in bases]  

    prefix_sum = [0] * b  
    prefix_sum[0] = golds[0]  
    for i in range(1, b):  
        prefix_sum[i] = prefix_sum[i - 1] + golds[i]  

    result = []  
    for power in attacking_powers:  
        index = bisect_right(defenses, power) - 1  
        
        if index == -1:  
            result.append(0)  
        else:  
            result.append(prefix_sum[index])  

    print(*result)  
# =========================================
def main():
    t = 1
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