"""
344. Reverse String
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.
Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


class ReverseString:

    def reverseString(self, s) -> None:
        """
        O(1)空间复杂度下翻转数组
        :param s: List[str]
        :return:
        """
        lens = len(s)
        for i in range(int(lens / 2 )):
            print(i)
            tmp = s[i]
            s[i] = s[lens - i - 1]
            s[lens - i - 1] = tmp

if __name__ == '__main__':
    rs = ReverseString()
    s = ["h", "e", "l", "l", "o"]
    rs.reverseString(s)