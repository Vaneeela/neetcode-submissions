class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mylist = sorted(strs)
        first = mylist[0]
        newstring=""
        for i in range(len(first)):
            flag = False
            for item in mylist[1:]:
                if(first[i] != item[i]):
                    flag = True
                    break
            if flag:
                break
            newstring+=first[i]   
        return newstring



# 1. you sorrt
# 2. pick the first element
# 3. compare each character with all the character at that index of other elements
# 4. in the inner for loop, if we find out the characters are not the same, it means, that is not the
# longest prefix
# 5. so how do we know outside the inner for loop if it was 2 characters that are not the same that ended the loop or it was done going through every element
# simple, we use a boolean flag, set it to false at the start, and if we end up breaking out, we set it to true
# 6. if flag remained false, just append the character at that index to the newstring and continue normally
# else we just break, and return the string we have built so far.