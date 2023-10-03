class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_new = ("".join(i for i in s if i.isalnum())).lower()
        return (str_new==str_new[::-1])