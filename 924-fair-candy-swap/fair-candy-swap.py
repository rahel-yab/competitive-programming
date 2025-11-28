class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # suma -x + y = sumb -y + x
        # y = sumb - suma + 2*x
        suma = sum(aliceSizes)
        sumb = sum(bobSizes)
        sett = set(bobSizes)
        for x in aliceSizes:
            y = (sumb - suma + 2*x)//2
            if y in sett:
                return [x , y]

