# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())
def prime(k):
    sett = set()
    while k % 2 == 0:
        sett.add(2)
        k //= 2
    for i in range(3, int(k**0.5)+1, 2):
        while k % i == 0:
            sett.add(i)
            k //= i
        if k == 1:
            break
    if k > 2:
        sett.add(k)
    return len(sett)

count = 0
for i in range(2,n +1):
    if prime(i) == 2:
        count += 1
print(count)