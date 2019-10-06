class Solution {
    func singleNumber(_ nums: [Int]) -> Int {
        var dict = Dictionary<Int, Int>()
        for num in nums {
            if let value = dict[num] {
                dict[num] = value + 1
            } else {
                dict[num] = 1
            }
        }
        var result = 0
        for key in dict.keys {
            if dict[key] == 1 {
                result = key
            }
        }
        return result
    }
}
