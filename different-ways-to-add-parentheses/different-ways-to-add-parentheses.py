class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []
        
        
        if "-" not in expression and "+" not in expression and "*" not in expression:
            result.append(int(expression))
        else:
            for i in range(len(expression)):
                print(i)
                if expression[i].isdigit() ==False:
                    part1 = self.diffWaysToCompute(expression[0:i])
                    part2 = self.diffWaysToCompute(expression[i+1:len(expression)])

                    for a in part1:
                        for b in part2:
                            if  expression[i] == '+':
                                result.append(int(a) + int(b))
                            if  expression[i] == '*':
                                result.append(int(a) * int(b))
                            if  expression[i] == '-':
                                result.append(int(a) - int(b))
        return result