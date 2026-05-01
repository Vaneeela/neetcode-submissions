class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # mydict={x: 0 for x in range(len(nums))}
        mydict={}
        for i in nums:
            mydict[i]=0
        for i in nums:
            mydict[i]+=1
        newdict = dict(sorted(mydict.items(),key=lambda item:item[1]))
        sorted_list= list(newdict.keys())
        new_list = sorted_list[-k:]
        return new_list
        