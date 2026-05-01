class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a_list = sorted(s)
        b_list = sorted(t)
        if len(a_list) != len(b_list):
            return False
        for i in range(len(b_list)):
            if a_list[i] != b_list[i]:
                return False
        return True

        