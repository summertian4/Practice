class Solution {
    func reverse(_ x: Int) -> Int {
        let sign = x < 0 ? -1: 1
        var x = x < 0 ? -x: x
        var arr: [Int] = Array<Int>()
        var result = 0
        while true {
            // 最后一位
            let temp = x % 10
            arr.append(temp)
            x = x / 10
            if x  == 0 {
                break
            }
        }
        for (index, value) in arr.enumerated() {
            result += value * Int(pow(10.0, Double(arr.count - index - 1)))
        }
        if result > Int(pow(2.0, 31.0)) {
            return 0;
        }
        result = result * sign
        return result
    }
}

var s = Solution()
var result = s.reverse(-123)
print(result)