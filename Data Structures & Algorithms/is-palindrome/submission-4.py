class Solution:
    def isPalindrome(self, s: str) -> bool:
        mystring =""
        for c in s:
            if c.isalnum():
                mystring +=c
            else:
                continue

        mystring = mystring.lower()
        reversed_string = mystring[::-1]
        return mystring == reversed_string
        