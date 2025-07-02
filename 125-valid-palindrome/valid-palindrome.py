class Solution(object):
    def isPalindrome(self, s):
        formatted=''.join(char.lower() for char in s if char.isalnum())
        return True if formatted==formatted[::-1] else False