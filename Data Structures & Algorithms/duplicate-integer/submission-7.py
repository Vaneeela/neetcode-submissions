from sortedcontainers import SortedSet
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) > len(SortedSet(nums)):
            return True
        return False
        
        