"""
326. Power of Three
Given an integer, write a function to determine if it is a power of three.
Example 1:
Input: 27
Output: true
Example 2:
Input: 0
Output: false
Example 3:
Input: 9
Output: true
Example 4:
Input: 45
Output: false

@author xwolf
@status accept
"""
class PowerOfThree:

    def __init__(self):
        pass

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            n = n / 3
        return n == 1


if __name__ == "__main__":
    p = PowerOfThree()
    print(p.isPowerOfThree(3))


