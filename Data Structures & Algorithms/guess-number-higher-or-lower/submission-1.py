# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i=1
        j=n
        l=0
        while (guess(l)!=0 and i<=j):
            l=(i+j)//2
            if guess(l)==-1:
                j=l-1
            if guess(l)==1:
                i=l+1
        return l 