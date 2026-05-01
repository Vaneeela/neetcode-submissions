class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        SortedArray = sorted(nums)
        return SortedArray[len(nums)//2]
        