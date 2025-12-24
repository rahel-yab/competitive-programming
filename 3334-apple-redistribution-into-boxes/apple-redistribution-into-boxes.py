class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        summ = sum(apple)
        capacity.sort(reverse= True)
        i = 0
        while summ > 0  and i < len(capacity):
            summ -= capacity[i]        
            i += 1
        
        return i

        