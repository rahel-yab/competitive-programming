# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

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
    graph = defaultdict(list)
    arr = []
    indeg = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
    for _ in range(n):
        arr.append(si())
    for i in range(n-1):
        w1 , w2 = arr[i] , arr[i+1]
        minn = min(len(w1),len(w2))
        flag = False
        for j in range(minn):
            if w1[j] != w2[j]:
                graph[w1[j]].append(w2[j])
                indeg[w2[j]] += 1
                flag = True
                break
        if not flag and len(w1) > len(w2):
            print("Impossible")
            return
    
    q = deque()
    for key , val in indeg.items():
        if val == 0:
            q.append(key)
    ans = []
    while q:
        l = q.popleft()
        ans.append(l)
        for nei in graph[l]:
            indeg[nei] -= 1
            if indeg[nei] == 0:
                q.append(nei)
    if len(ans) < 26:
        print("Impossible")
    else:
        print("".join(ans))

    

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



