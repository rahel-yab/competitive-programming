# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class MapSum:
    def __init__(self):
        self.mapp = {}

    def insert(self, key: str, val: int) -> None:
        self.mapp[key] = val

    def sum(self, prefix: str) -> int:
        ans = 0
        for k , v in self.mapp.items():
            if k.startswith(prefix):
                ans += v
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)