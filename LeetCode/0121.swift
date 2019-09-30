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
    func maxProfit(_ prices: [Int]) -> Int {
        var array = Array<Int>()
        if prices.count <= 1 {
            return 0
        }
        for i in 1..<prices.count {
            array.append(prices[i] - prices[i - 1])
        }
        let result = maxSubArray(array)
        return max(result, 0)
    }
}
