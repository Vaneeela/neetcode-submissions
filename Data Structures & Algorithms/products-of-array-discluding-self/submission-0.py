class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newlist = []
        for i in range(len(nums)):
            product = math.prod(nums[j] for j in range(len(nums)) if j != i)
            newlist.append(product)
        return newlist