class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 2147483647
        nums.sort()
        ls = len(nums)
        for i in range(ls - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = ls - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == target:
                    res = target
                    return res
                elif curr < target:
                    j += 1
                    if abs(curr - target) <= abs(res - target) :
                        res = curr
                else:
                    k -= 1
                    if abs(curr - target) <= abs(res - target) :
                        res = curr
        return res