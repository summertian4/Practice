class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        var map: Set = Set<Int>()
        for num in nums {
            map.insert(num)
        }
        if map.count == nums.count {
            return false
        } else {
            return true
        }
    }
}