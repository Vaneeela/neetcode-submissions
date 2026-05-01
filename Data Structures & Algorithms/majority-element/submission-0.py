class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mydict = {}
        for num in nums:
            if num not in mydict:
                mydict[num] =1
            else:
                mydict[num] +=1
                
        for i,val in mydict.items():
            if val > len(nums)//2:
                return i

        