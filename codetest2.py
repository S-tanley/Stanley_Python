class Solution(object):
    def matchbrcket(sef, input_str):
        mystack = []
        res = [" " for _ in range(len(input_str))]

        for i, char in enumerate(input_str) :
            if char == "(" :
                mystack.append(i)
            elif char == ")" :
                if len(mystack) != 0:
                    mystack.pop()
                else:
                    res[i] = "?"
        while len(mystack) != 0:
            a = mystack.pop()
            res[a] = "x"
        return res
    
test = Solution()
res1 = test.matchbrcket("bge)))))))))")
res2 = test.matchbrcket("((IIII))))))")
res3 = test.matchbrcket("()()()()(uuu")
res4 = test.matchbrcket("))))UUUU((()")
print("bge)))))))))", "".join(res1), "((IIII))))))", "".join(res2), "()()()()(uuu", "".join(res3), "))))UUUU((()", "".join(res4), sep="\n")