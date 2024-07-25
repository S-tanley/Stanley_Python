class Solution(object):
    def mymedian(self, myl):
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
        return sum(myl)/len(myl)

    def MaxWeigtVal(self, a, n):
        res = -10**9
        all_subsequences = []
        for i in range(2**n):
            subsequence = []
            for j in range(n):
                # Check if j-th bit in i is set
                if (i & (1 << j)) > 0:
                    subsequence.append(a[j])
            if(len(subsequence)== 0):
                continue
            t = self.mymean(subsequence) - self.mymedian(subsequence)
            res = res if res > t else t
            all_subsequences.append(subsequence)
        return res
    
a = [1,3,5,9]
n = 4
test = Solution()
res = test.MaxWeigtVal(a, n)
print(res)