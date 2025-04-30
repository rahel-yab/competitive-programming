# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        for char, f in count.items():
            heappush(heap,(-f,char))
     
        interval = 0
        while heap:
            cycle = n + 1
            on_hold = []
            last = 0
            for i in range(cycle):
                if heap:
                    last += 1
                    freq,task = heappop(heap)
                    freq = -freq
                    freq -= 1
                    if freq > 0:
                        on_hold.append((-freq,task))
            
            for task in on_hold:
                heappush(heap,task)
            if heap:
                interval += cycle
            else:
                interval += last
        
            
        return interval 
            

                

