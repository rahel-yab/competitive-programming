# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k

        for num in nums:
            self.add(num)

    def heapify(self, nums, n, i):
        minn = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and nums[left] < nums[minn]:
            minn = left
        if right < n and nums[right] < nums[minn]:
            minn = right

        if minn != i:
            nums[i], nums[minn] = nums[minn], nums[i]
            self.heapify(nums, n, minn)

    def build_heap(self, nums):
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            self.min_heap.append(val)
            self.build_heap(self.min_heap)
        elif val > self.min_heap[0]:
            self.min_heap[0] = val
            self.heapify(self.min_heap, len(self.min_heap), 0)
        return self.min_heap[0]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)