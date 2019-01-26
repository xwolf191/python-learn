
"""
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
Example 1:
Input: s = "egg", t = "add"
Output: true
Example 2:
Input: s = "foo", t = "bar"
Output: false
Example 3:
Input: s = "paper", t = "title"
Output: true

@author xwolf
@status
"""

import re
class IsomorphicStrings:

    def __init__(self):
        pass

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = set(zip(s, t))
        print(s)
        print(type(s))
        print(s[0])
        print(s(1))


if __name__ == '__main__':

    st = IsomorphicStrings()
    s = "abab"
    t = "baba"
    print(st.isIsomorphic(s, t))
