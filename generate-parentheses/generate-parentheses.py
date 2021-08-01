  
class Solution:

            
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(result, open, close, nums, element):
            if len(element) == nums*2:
                result.append(element)
            if open < nums:
                helper(result, open+1, close, nums, element+"(")
            if open > close:
                helper(result, open, close+1, nums, element+")")    
                
        result = []
        helper(result,0,0,n, "")
        return result
    
