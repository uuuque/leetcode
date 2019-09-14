class Solution:
    def reverse(self, x):
        flag = 1
        if x < 0:
            flag = -1
        x = abs(x)
        rx = str(x)[::-1]
        rx = flag*int(rx)
        if rx < -(2**31) or rx > (2**31)-1:
            return 0
        else:
            return rx


if __name__ == '__main__':
    a = Solution()
    X = int(input("请输入一个整数："))
    Rx = a.reverse(X)
    print("反转数为：%d" % Rx)
