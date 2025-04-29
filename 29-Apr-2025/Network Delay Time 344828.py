# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, weight in times:
            graph[u].append((v, weight))
        
        q = deque([(k, 0)])
        res = {i: float('inf') for i in range(1, n + 1)}
        res[k] = 0

        while q:
            node, curr = q.popleft()
            for nei, weight in graph[node]:
                if curr + weight < res[nei]:
                    res[nei] = curr + weight
                    q.append([nei, curr + weight])
        
        ans = max(res.values())
        if ans != float('inf'):
            return ans
        else:
            return  -1
        

        