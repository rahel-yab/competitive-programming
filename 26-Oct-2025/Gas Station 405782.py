# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        curr = 0
        ans = 0
        for i in range(len(gas)):
            curr += gas[i] -cost[i] 
            tank += gas[i] -cost[i] 
            if tank < 0:
                ans = i+ 1
                tank = 0
                
        if curr < 0:
            return -1
        return ans
