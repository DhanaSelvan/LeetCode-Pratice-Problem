class Solution(object):
    def addTwoNumbers(self, l1, l2):
        print(f"{l1,l2}")
        res_l1 = l1.reverse()
        res_l2 = l2.reverse()
        print(f'{l1,l2}')
        result_l1 = []
        result_l2 = []
        for i in l1:
            result_l1.append(str(i))
        for j in l2:
            result_l2.append(str(j))
        print("".join(result_l1))
        print("".join(result_l2))
        result = int("".join(result_l1)) + int("".join(result_l2))
        final = []
        for k in str(result):
            final.append(k)
        print(final[::-1])
        
    
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

obj = Solution()
obj.addTwoNumbers(l1,l2)