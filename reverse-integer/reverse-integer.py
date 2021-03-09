class Solution:
    def reverse(self, x: int) -> int:
        if not (-2147483648 <= x<= 2147483647):
            return 0
        y= str(x)
        y = y[::-1]
        y = y.replace("-", "")
        for i, c in enumerate(y):
          if c != '0':
            break;  
        y = y[(i):]
        if "-" in str(x):
          y = "-" + y
        if not y:
          y = 0
        if (-2147483648 >= int(y)) or (int(y)>= 2147483647):
          y=0
        return(y)

