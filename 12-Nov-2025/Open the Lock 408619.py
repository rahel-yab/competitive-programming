# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        sett = set(deadends)

        graph = defaultdict(list)
        for i in range(10):
            if i == 0:
                graph[str(i)].extend(['1', '9'])
            elif i == 9:
                graph[str(i)].extend(['0', '8'])
            else:
                graph[str(i)].extend([str(i-1), str(i+1)])
        
        q = deque()
        q.append(('0000' , 0))
        visited = set()
        visited.add("0000")
        if '0000' in sett:
            return -1

        while q:
            lock , turns = q.popleft()
            if lock == target:
                return turns
            
            for i , start in enumerate(lock):
                for nei in graph[start]:
                    new_lock = list(lock)
                    new_lock[i] = nei
                    new_lock = ''.join(new_lock)
                    if new_lock in sett:
                        continue
                    if new_lock not in visited:
                        q.append((new_lock, turns+1))
                        visited.add(new_lock)
        
        return -1

