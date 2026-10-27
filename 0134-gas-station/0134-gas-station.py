class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        
        total_gas = 0
        current_gas = 0
        start = 0

        for i in range(len(gas)):
            difference = gas[i] - cost[i]

            total_gas += difference
            current_gas += difference

            if current_gas < 0:
                start = i + 1
                current_gas = 0

        if total_gas < 0:
            return -1

        return start
