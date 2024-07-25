class Solution(object):
    def minfsubseq(self, source, target):
        ps = 0
        pt = 0
        count = 0
        while(pt < len(target)):
            flag = pt
            for i in source:
                if i == target[pt]:
                    pt += 1
            if flag == pt:
                return -1
            count += 1
        return count

test = Solution()
res1 = test.minfsubseq("abc", "abcbc")
res2 = test.minfsubseq("abc", "acdbc")
res3 = test.minfsubseq("xyz", "xzyxz")
print(res1, res2, res3)