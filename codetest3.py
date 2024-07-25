class Solution(object):
    def mymedian(self, myl):
        # 根据定义算中位数
        length = len(myl)
        if length == 1:
            return myl[0]
        if (length) % 2 == 1:
            res = myl[length // 2]
            return res
        else:
            res = (myl[length//2] + myl[length//2 - 1]) / 2
            return res

    def mymean(self, myl):
        # 平均数
        return sum(myl)/len(myl)

    def MaxWeigtVal(self, a, n):
        res = -10**9
        # 这里想的是直接遍历，每种子序列
        # 有点问题因为复杂度这样的话是O（2**n*n）
        for i in range(2**n):
            subsequence = []
            for j in range(n):
                if (i & (1 << j)) > 0:
                    subsequence.append(a[j])
            if(len(subsequence)== 0):
                continue
            t = self.mymean(subsequence) - self.mymedian(subsequence)
            res = res if res > t else t
        return res
    
a = [1,3,5,9]
n = 4
test = Solution()
res = test.MaxWeigtVal(a, n)
print(res)
