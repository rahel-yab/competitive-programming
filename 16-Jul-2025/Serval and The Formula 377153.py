# Problem: Serval and The Formula - https://codeforces.com/problemset/problem/2085/C

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
    x , y = mi()
    andd = x & y
    if x == y:
        print(-1)
        return
    if andd == 0:
        print(0)
        return
    maxx = max(x,y)
    val = maxx
    c = 0
    while maxx:
        c += 1
        maxx >>= 1
    k = (1<<c) - val
    print(k)
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
