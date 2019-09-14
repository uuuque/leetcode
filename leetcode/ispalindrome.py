class Solution:
    def isPalindrome(self, x):
        rx = str(x)[::-1]
        if str(x) == rx:
            return True
        else:
            return False


if __name__ == '__main__':
    a = Solution()
    X = int(input("请输入一个整数："))
    print(a.isPalindrome(X))
