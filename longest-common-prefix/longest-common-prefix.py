class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        k=0
        n=len(strs)
        if(n==0):
            return ""
        a=strs[0]
        for i in range(n):
            if(len(strs[i])<len(a)):
                a=strs[i]
        strs.remove(a)
        for i in a:
            flag=0
            for j in range(n-1):
                if(i!=strs[j][k]):
                    flag=1
                    break
            if(flag==1):
                break
            else:
                result+=i
            k+=1
        return result 