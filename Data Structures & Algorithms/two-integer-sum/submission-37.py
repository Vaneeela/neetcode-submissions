from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store numbers with their original indices
        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        # Sort by the numbers
        nums_with_index.sort(key=lambda x: x[0])
        
        j = 0
        k = len(nums_with_index) - 1
        
        while j < k:
            val1, idx1 = nums_with_index[j]
            val2, idx2 = nums_with_index[k]
            total = val1 + val2
            
            if total == target:
                # Return smaller index first
                return [min(idx1, idx2), max(idx1, idx2)]
            elif total < target:
                j += 1
            else:
                k -= 1
