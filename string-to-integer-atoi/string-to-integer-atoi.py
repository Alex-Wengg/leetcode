class Solution:
    def myAtoi(self, s: str) -> int:
        substring = ""
        minLimit = -2147483648
        maxLimit = 2147483648
        index =0
        sign =""

        
        while index < len(s) and s[index] == ' ':
            index +=1
        
        if index < len(s) and (s[index]=="-"):
            sign = "-"
            index +=1
        elif index < len(s) and (s[index]=="+"):
            sign = ""
            index +=1    
        
        
        while index < len(s) and s[index] == "0":
            index+=1
            
        valided = ["0","1","2",'3','4','5','6','7','8','9']
        #check if the char isn't a whitespace AND if its a number 
        for i in range(index, len(s)):
            if (s[i]== " "):
                if substring:
                    substring = sign+substring
                    return substring
                else:
                    return 0
            if (s[i] in valided)and (s[i]!= " "):
                substring += s[i]
            if (s[i] not in valided)and (s[i]!= " "):
                break
            else:
                continue
        if substring =="":
            return 0
        
        substring = sign+substring

        if(int(substring) <= minLimit):
            return minLimit
        elif(int(substring) >= maxLimit):
            return maxLimit-1
        else:
            return (substring)