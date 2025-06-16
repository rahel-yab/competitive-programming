# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.median = []
        

    def addNum(self, num: int) -> None:
        self.median.append(num)
        

    def findMedian(self) -> float:
        self.median.sort()
        n = len(self.median)
        mid = n // 2
        if n == 1:
            return self.median[0]
        if n % 2 == 1:
            return self.median[mid]
        else:
            return (self.median[mid] + self.median[mid-1])/2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()