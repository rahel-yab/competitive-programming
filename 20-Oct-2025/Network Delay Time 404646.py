# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, weight in times:
            graph[u].append((v, weight))
        
        dist = {node:float("inf") for node in range(1,n+1)}
        dist[k] = 0
        heap = [k]

        while heap:
            node = heappop(heap)
            for nei, weight in graph[node]:
                if dist[nei] > dist[node] + weight:
                    dist[nei] = dist[node] + weight
                    heappush(heap ,nei)
                    
        ans = max(dist.values())
        if ans != float('inf'):
            return ans
        return -1