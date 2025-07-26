# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

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
    arr = li()
    c = []
    def dfs(s, e, l=0):
        if e - s == 1:
            return [arr[s]]
        mid = (s + e) // 2
        left = dfs(s, mid, l + 1)
        right = dfs(mid, e, l + 1)
        curr1 = left + right
        curr2 = right + left

        if curr1 == sorted(curr1):
            return curr1
        elif sorted(curr2) == curr2:
            c.append((s, e)) 
            return curr2
        else:
            return [] 
    sort = dfs(0, n)
    res = len(c) if sort == sorted(arr) else None
    if res == None:
        print(-1)
    else:
        print(res)


    return
# =========================================
def main():
    t = ii()
    for _ in range(t):
        solve()

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 25)
    threading.stack_size(1 << 27)
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()



