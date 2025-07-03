class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count_dict = {}

        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
                if count_dict[num] > 1:
                    return True
            else:
                count_dict[num] = 1
        
        return False

        