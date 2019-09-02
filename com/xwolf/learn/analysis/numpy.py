"""
numpy基本库使用
"""
import numpy as np


class Numpy:

    def __init__(self):
        pass

    def array(self):
        """
        基础数组
        :return:
        """
        ary = np.array([[1, 4, 3], [3, 2, 1]])
        print(ary)

    def trigonometricFunction(self):
        """
        三角函数,sin cos tan arcsin arccos arctan
        :return:
        """
        # 角度转化为弧度
        angle = 30 / 180 * np.pi
        # 正弦
        print("sin30°=", np.sin(angle))
        # 余弦
        print("cos30°=", np.cos(angle))
        # 正切
        print("tan30°=", np.tan(angle))
        # 没有提供余切,可用正切的倒数来计算
        print("cot30°= 1/tan30°=", 1 / np.tan(angle))

        # 反正弦
        print("arcsin30°=", np.arcsin(angle))
        # 反余弦
        print("arccos30°=", np.arccos(angle))
        # 反正切
        print("arctan30°=", np.arctan(angle))

        # 反双曲正弦
        print("arcsinh30°=", np.arcsinh(angle))
        # 反双曲余弦
        print("arccosh30°=", np.arccosh(angle))


if __name__ == '__main__':
    npy = Numpy()
    npy.array()
