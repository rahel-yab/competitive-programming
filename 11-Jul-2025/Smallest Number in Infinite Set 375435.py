# Problem: Smallest Number in Infinite Set - https://leetcode.com/problems/smallest-number-in-infinite-set/description/

class SmallestInfiniteSet:

    def __init__(self):
        self.sett = set(range(1, 1001))
        self.heap = []
        for num in self.sett:
            heappush(self.heap , num)

    def popSmallest(self) -> int:
        if self.heap:
            val = heappop(self.heap)
            self.sett.remove(val)
            return val

    def addBack(self, num: int) -> None:
        if num not in self.sett:
            self.sett.add(num)
            heappush(self.heap , num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)