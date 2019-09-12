class Solution:
    def twosum(self, nums, target):
        n = len(nums)
        d = {}    # 空字典保存target-num[i]和i的键值对
        for i in range(n):
            s = target - nums[i]
            if nums[i] in d:
                return d[nums[i]], i
            else:
                d[s] = i


if __name__ == '__main__':
    Nums = [2, 7, 10, 12]
    Target = 9
    x = Solution()
    print(x.twosum(Nums, Target))
