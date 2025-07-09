# Problem: Hongcow Builds A Nation - https://codeforces.com/contest/744/problem/A

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
    n , m , k = mi()
    gov = li()
    graph = defaultdict(list)
    for _ in range(m):
        u , v = mi()
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    c = 0
    def dfs(i):
        nonlocal c
        visited.add(i)
        for nei in graph[i]:
            if nei not in visited:
                c += 1
                dfs(nei)
        return c
    ans = []
    for i in gov:
        c = 1
        ans.append(dfs(i))
    # print(ans)
    summ = 0
    nodes = sum(ans)
    for j in ans:
        summ += (j * (j-1))//2
    left = 0
    for i in range(1, n+1):
        if i not in visited:
            left += 1
    print((summ - m) + (left * (left -1) // 2) + max(ans) * left)
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