# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

n = int(input())

mat = []
for _ in range(n):
    arr = list(map(int, input().split()))
    mat.append(arr)

def inbound(r,c):
    return 0 <= r < n and 0 <= c < 3

for i in range(n-2,-1,-1):
    for j in range(3):
        left , up = float("-inf") , float("-inf")
        if j == 2:
            if inbound(i+1,j-1):
                left = mat[i+1][j-1]
            if inbound(i+1,j-2):
                up = mat[i+1][j-2]
            mat[i][j] += max( up,left ) 
        elif j == 1:
            if inbound(i+1,j-1):
                left = mat[i+1][j-1]
            if inbound(i+1,j+1):
                up = mat[i+1][j+1]
            mat[i][j] += max( up,left )
        elif j == 0:
            if inbound(i+1,j+1):
                left = mat[i+1][j+1]
            if inbound(i+1,j+2):
                up = mat[i+1][j+2]
            mat[i][j] += max( up,left ) 
print(max(mat[0]))
