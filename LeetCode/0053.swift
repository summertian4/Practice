class Solution {
    func maxSubArray(_ nums: [Int]) -> Int {
        var ans=nums[0]
        var sum = 0
        for i in 0..<nums.count {
            sum += nums[i]
            ans = max(sum, ans)
            sum = max(sum, 0)
        }
        return ans;
    }
}
