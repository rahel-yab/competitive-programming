# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def valid(row,col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0])) and grid[row][col] == 1  

        directions = [(0,1) , (1,0), (-1,0), (0,-1)]
        queue = deque()
        time , fresh = 0 , 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row,col))
                    
        while queue and fresh > 0:
            for _ in range(len(queue)):
                i , j = queue.popleft()
                for dr , dc in directions:
                    R = i + dr
                    C = j + dc
                    if valid(R,C):
                        grid[R][C] = 2
                        fresh -= 1
                        queue.append((R,C))
            time += 1

        if fresh > 0:
            return -1
        else:
            return time

                