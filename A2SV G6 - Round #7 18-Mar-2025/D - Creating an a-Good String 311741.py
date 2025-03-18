# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

def min_moves_to_good(s, c):
    n = len(s)
    if n == 1:
        return 0 if s[0] == c else 1
    
    mid = n // 2
    left_half, right_half = s[:mid], s[mid:]
    
    # Count how many are already 'c' in each half
    left_cost = mid - left_half.count(c)
    right_cost = mid - right_half.count(c)
    
    # Recur for the other half with (c+1)
    return min(left_cost + min_moves_to_good(right_half, chr(ord(c) + 1)),
               right_cost + min_moves_to_good(left_half, chr(ord(c) + 1)))
 
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    print(min_moves_to_good(s, 'a'))