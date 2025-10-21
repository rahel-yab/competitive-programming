# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            u , v = edges[i]
            graph[u].append((v, succProb[i]))
            graph[v].append((u , succProb[i]))
        
        prob = [float("-inf")] * n
        prob[start_node] = 1
        heap = [start_node]
        while heap:
            node = heappop(heap)
            for nei, pr in graph[node]:
                if pr * prob[node] > prob[nei]:
                    prob[nei] = pr * prob[node]
                    heappush(heap, nei)
        return prob[end_node] if prob[end_node] != float("-inf") else 0
            