class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        if x < 0 {
            return false
        }
        var x = x < 0 ? -x: x
        var arr: [Int] = Array<Int>()
        while true {
            // 最后一位
            let temp = x % 10
            arr.append(temp)
            x = x / 10
            if x  == 0 {
                break
            }
        }
        var index = arr.count - 1
        var arr2: [Int] = Array<Int>()
        while index >= 0 {
            arr2.append(arr[index])
            index -= 1
        }
        var flag = true
        for (index, value) in arr.enumerated() {
            if value != arr2[index] {
                flag = false
            }
        }
        return flag
    }
}

var s = Solution()
var result = s.isPalindrome(1221)
print(result)