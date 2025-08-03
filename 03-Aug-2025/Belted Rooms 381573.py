# Problem: Belted Rooms - https://codeforces.com/problemset/problem/1428/B

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
    n = ii()
    graph = [[] for _ in range(n)]
    arr = si()
    ans = set()
    if '<' not in arr or '>' not in arr:
        print(n)
        return
    for i in range(n):
        
        if arr[i] == '-':
            ans.add(i)
            ans.add((i+1)%n)
    print(len(ans))
        
    
        



    return
# =========================================
def main():
    t = ii()
    for _ in range(t):
        solve()

main()

# if __name__ == '__main__':
#     sys.setrecursionlimit(1 << 25)
#     threading.stack_size(1 << 27)
#     thread = threading.Thread(target=main)
#     thread.start()
#     thread.join()






