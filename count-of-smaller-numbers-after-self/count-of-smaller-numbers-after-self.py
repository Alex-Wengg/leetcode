class Solution:
    def countSmaller(self, nums):
        def sort(enum):
            half = int(len(enum)/2)
            
            if half:
                left = sort(enum[:half])
                right = sort(enum[half:])
                
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        small[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        small = [0] * len(nums)
        sort(list(enumerate(nums)))
        return small