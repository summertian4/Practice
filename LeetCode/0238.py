class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        _len = len(nums)
        prod = 1
        for i in range(_len):
            answer.append(prod)
            prod *= nums[i]
        prod = 1
        for i in range(_len - 1, -1, -1):
            answer[i] *= prod
            prod *= nums[i]
        return answer