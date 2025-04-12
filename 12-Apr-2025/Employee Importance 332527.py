# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        res = 0
        maps = {emp.id :emp for emp in employees}
        # print(maps)
        def dfs(target):
            nonlocal res
            if target not in maps:
                return
            emp = maps[target]
            res += emp.importance
                    
            for sub in emp.subordinates:
                dfs(sub)
        dfs(id)
        return res
        