class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def check_anagram(g):
            mydict = {}
            for i in list(g):
                if i in mydict:
                    mydict[i] += 1
                else:
                    mydict[i] = 1
            return mydict
        return check_anagram(s) == check_anagram(t)
                



        