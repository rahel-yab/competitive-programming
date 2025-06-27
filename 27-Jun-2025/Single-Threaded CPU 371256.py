# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:        
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda t: t[0])
        ans, heap = [], []
        i, time = 0, tasks[0][0]
        while i < len(tasks):
            while i<len(tasks) and time >= tasks[i][0]:
                heappush(heap, [tasks[i][1], tasks[i][2]])
                i+=1
            if heap:
                priority, idx = heappop(heap)
                ans.append(idx)
                time += priority
            else:
                time = tasks[i][0]
        while heap:
            priority, idx = heappop(heap)
            ans.append(idx)
        return ans