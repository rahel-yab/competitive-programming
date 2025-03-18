# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

def min_penalty_kicks(s):
    # Simulating two cases
    def simulate(team_favored):
        score_A = score_B = 0
        remaining_A = remaining_B = 5  # Each team has 5 kicks in total

        for i in range(10):
            if i % 2 == 0:  # Team A's turn
                if s[i] == '1':
                    score_A += 1
                elif s[i] == '?':
                    if team_favored == "A":  # Assume best for A
                        score_A += 1
                remaining_A -= 1
            else:  # Team B's turn
                if s[i] == '1':
                    score_B += 1
                elif s[i] == '?':
                    if team_favored == "B":  # Assume best for B
                        score_B += 1
                remaining_B -= 1

            # Check if it's impossible for the other team to catch up
            if score_A > score_B + remaining_B:
                return i + 1  # Stopped after i+1 kicks
            if score_B > score_A + remaining_A:
                return i + 1
        
        return 10  
    return min(simulate("A"), simulate("B"))
t = int(input().strip())
for _ in range(t):
    s = input().strip()
    print(min_penalty_kicks(s))