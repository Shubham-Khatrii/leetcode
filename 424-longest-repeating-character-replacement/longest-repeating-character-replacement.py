class Solution(object):
    def characterReplacement(self, s, k):
        max_len = 0
        count = [0] * 26  
        max_count = 0     
        left = 0          

        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            count[index] += 1

            max_count = max(max_count, count[index]) 

            if (right - left + 1) - max_count > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len