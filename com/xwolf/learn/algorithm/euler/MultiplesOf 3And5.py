
"""
<a href="https://projecteuler.net/problem=1">Multiples of 3 and 5</a>
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5,
 we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

@author xwolf
"""


class MultiplesOf3And5:

    def __init__(self):
        pass

    def multsum(self,n):
        """
        the target number
        :param n:
        :return:
        """
        res = []
        for i in range(1, n):
            if i % 3 == 0 or i % 5 == 0:
                res.append(i)
        return sum(res)


if __name__ == '__main__':
    mlt = MultiplesOf3And5()
    print(mlt.multsum(1000))



