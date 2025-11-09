# Problem: B. Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n = int(input())
nums = list(map(int, input().split()))
odd , even = False, False
flag = False
for num in nums:
    if num %2 == 1:
        odd = True
    else:
        even = True
    if odd and even:
        flag = True
        break
if not flag:
    print(*nums)
else:
    nums.sort()
    print(*nums)