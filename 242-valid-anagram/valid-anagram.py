class Solution(object):
    def isAnagram(self, s, t):
        l1=[]
        l2=[]
        l1=s
        l2=t
        if sorted(l1)==sorted(l2):
            return True
        else:
            return False