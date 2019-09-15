class Solution:
    def romanToInt(self, s):
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = 0
        for i in range(len(s)-1):
            if d[s[i]] >= d[s[i+1]]:
                n = n + d[s[i]]
            else:
                n = n - d[s[i]]
        n = n + d[s[len(s) - 1]]
        return n


if __name__ == '__main__':
    a = Solution()
    romans = input("请输入罗马数字：")
    print("转换为整数后：%d" % a.romanToInt(romans))
