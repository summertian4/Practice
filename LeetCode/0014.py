class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        if strs.count < 1 {
            return ""
        }
        if strs.count < 2 {
            return strs.first!
        }
        var result = ""
        var minLen = Int.max
        for item in strs {
            minLen = min(minLen, item.lengthOfBytes(using: String.Encoding.utf8))
        }
        print(minLen)

        for i in 0..<minLen {
            let temp  = Array(strs.first!)[i]
            var allSame = true
            for item in strs {
                if temp != Array(item)[i] {
                    allSame = false
                    break
                }
            }
            if allSame {
                result.append(temp)
            } else {
                break
            }
        }
        return result
    }
}

var s = Solution()
var result = s.longestCommonPrefix(["flower","flow","flight"])
print(result)
