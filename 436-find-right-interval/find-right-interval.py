class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        indexed = []
        for i in range(len(intervals)):
            indexed.append([intervals[i][0] , intervals[i][1] , i])

        sorted_intervals = sorted(indexed , key= lambda x:x[0])

        def binary_search(u , v):
            low = 0
            high = len(sorted_intervals)-1
            ans = -1
            while low <= high:
                mid = (low+high)//2
                x , y, i = sorted_intervals[mid]
          
                if x >= v:
                    ans = i
                    high = mid -1
                else:
                    low = mid + 1

            return ans
        
        ans = []
        for i in range(len(intervals)):
            u , v = intervals[i]
            ind = binary_search(u , v)
            ans.append(ind)
        return ans

