class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (-2**31 >int(dividend/divisor)):
            return (-2**31)
        elif ((2**31-1) <int(dividend/divisor)):
            return (2**31-1)
        return int(dividend/divisor)