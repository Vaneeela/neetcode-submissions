class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def checkAnagram(item1, item2):
            return sorted(item1) == sorted(item2)

        grand_list =[]
        while len(strs) != 0:
            i = 0
            rep = strs[i]
            mylist = []
            mylist.append(rep)
            for k in range(1,len(strs)):
                if checkAnagram(rep,strs[k]):
                    mylist.append(strs[k])
                else:
                    k+=1
            for item in mylist:
                strs.remove(item)
            grand_list.append(mylist)
        return grand_list
            