class Solution {
    func isPowerOfTwo(_ num: Int) -> Bool {
        let max = Int(log2(Double(Int.max))) - 1
        let maxResult = Int(pow(Double(2), Double(max)))
        return num > 0 && (maxResult % num == 0)
    }
}
