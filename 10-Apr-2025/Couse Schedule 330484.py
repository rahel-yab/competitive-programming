# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        white = [0 for _ in range(n)]
        graph = [[] for _ in range(n)]
        for course, pre in prerequisites:
            graph[pre].append(course)

        def dfs(node):
            if white[node] == 1:
                return False
            if white[node] == 2:
                return True

            white[node] = 1
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            white[node] = 2
            return True

        for i in range(n):
            if white[i] == 0:
                if not dfs(i):
                    return False
        return True
