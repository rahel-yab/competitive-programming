# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

from collections import defaultdict

def is_spruce(n, p):
    tree = defaultdict(list)
    for i in range(n - 1):
        tree[p[i]].append(i + 2)
    # print(tree)
    for node in range(1, n + 1):
        if node in tree:
            lc = 0
            for child in tree[node]:
                if child not in tree: 
                    lc += 1
            if lc < 3: 
                return "No"
    return "Yes"
n = int(input())
p = [int(input()) for _ in range(n - 1)]
print(is_spruce(n, p))