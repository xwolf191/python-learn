"""
65. Valid Number
Validate if a given string can be interpreted as a decimal number.
Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:
Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.
Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.

@author xwolf
@tag match
@result accept
"""


class ValidNumber:

    def isNumber(self, s: str):
        """
        :param s: str
        :return: bool
        """
        s = s.strip(' ')
        size = len(s)
        if s is None or size == 0:
            return False
        number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        chars = ['+', '-', '.', 'e']
        # 只有一个字符判断是否为数字
        if size == 1:
            return s in number
        # 最后一个字符必须为数字或.
        if s[size-1] not in number and s[size-1] != '.':
            return False
        # 第一个字符不能为e
        if s[0] == 'e':
            return False
        existChar = []
        for i in range(size):
            cur = s[i]
            print(cur, existChar)
            # 字符不能出现多次
            if cur in existChar:
                return False
            # 只能数字和指定字符
            if cur not in number and cur not in chars:
                return False
            if cur in chars and i < size-1:
                nextChar = s[i+1]
                if s[0] != '+' and s[0] != '-':
                    existChar.append(cur)
                if cur != 'e' and nextChar in chars:
                    if cur == '.' and nextChar != 'e':
                        return False
                    if i == 0 and cur == '.' and nextChar == 'e':
                        return False
                    if cur != '.' and nextChar == 'e':
                        return False
                if cur == 'e':
                    if nextChar != '+' and nextChar != '-' and nextChar not in number:
                        return False
                # +,- 不能出现在字符串中间,但是e后边可以是+,-
                if cur == '+' or cur == "-":
                    if i > 0 and s[i-1] != 'e':
                        return False
        # 判断e后字符是否合法
        if 'e' in s:
            estr = s.split("e")
            etr = estr[1]
            for j in range(len(etr)):
                er = etr[j]
                print(er)
                if j == 0 and er not in number and er != '+' and er != '-':
                    return False
                if j != 0 and er not in number:
                    return False
        # 如果字符串是否含任何数字
        res = False
        for i in range(size):
            if s[i] in number:
                res = True
        return res


if __name__ == '__main__':
    vn = ValidNumber()
    sr = "+42e+76125"
    print(vn.isNumber(sr))