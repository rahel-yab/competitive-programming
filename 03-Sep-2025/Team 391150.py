# Problem: Team - https://codeforces.com/contest/231/problem/A

n = int(input())
count = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    summ = sum(arr)
    if summ >= 2:
        count += 1
print(count)