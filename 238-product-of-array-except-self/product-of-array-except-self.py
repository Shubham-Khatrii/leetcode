class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1] * n

        # Step 1: Compute prefix product for each index
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Step 2: Compute suffix product and multiply with result
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result

