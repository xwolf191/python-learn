"""
numpy基本库使用
"""
import numpy as np


class Numpy:

    def __init__(self):
        pass

    def narray(self):
        """
        多维数组
        :return:
        """
        # 普通数组转化为ndarray对象
        ary = [1, 4, 65, 1]
        print(np.array(ary))
        # N维数组构建
        aAry = np.array([[1, 4, 3], [3, 2, 1]])
        print(aAry)
        # 返回一个数组行列数的元祖
        print("数组的行列式元祖=", aAry.shape)
        # 返回数组类型的对象
        print(aAry.dtype)
        # 返回数组维度
        print("数组的维数=", aAry.ndim)
        # 每个元素都扩大10倍
        print(aAry * 10)
        # 数组相加,必须行、列数一致
        bAry = np.array([[4, 3, 2], [5, 4, 3]])
        print(aAry + bAry)
        # 创建全是0的多维数组
        zeroAry = np.zeros((2, 5))
        print("创建元素全是0的多维数组", zeroAry)
        # 创建空元素数组,默认会是比较奇怪的预设元素,慎用
        emptyAry = np.empty((4,))
        print("创建元素全是预设元素的多维数组", emptyAry)

    def ndarray(self):
        """
        :return:
        """
        # 普通数组转化为ndarray对象
        ary = [1, 4, 65, 1]
        aAry = np.array(ary)
        print("根据普通数据创建ndarray对象", aAry)
        # 创建全是0的多维数组
        zeroAry = np.zeros((2, 5))
        print("创建元素全是0的多维数组", zeroAry)
        # 创建空元素数组,默认会是比较奇怪的预设元素,慎用
        emptyAry = np.empty((4,))
        print("创建元素全是未初始化预设元素的多维数组", emptyAry)
        # 通过arange生成有序数组
        bAry = np.arange(10, dtype='float')
        print("arange生成数组对象", bAry)
        # 通过arange生成有序数组
        cAry = np.arange(start=2, stop=50, step=3, dtype='float')
        print("arange生成数组对象", cAry)
        # 元素都为1的数组
        one = np.ones((1, 3))
        print("元素为1的数组", one)
        # 对角线为1,其他均为0
        c = np.eye(4, 4)
        print("指定对角线为1的数组", c)

    def ndarrayType(self):
        """
        多维数组属性
        :return:
        """
        a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        # 数组的形状,返回一个元组(行数,列数)
        print("多维数组维度", a.shape, "元素类型", a.dtype, "元素总个数", a.size)
        b = a.astype(dtype='float')
        print("转化为指定类型的数组", b)
        # 获取指定位置元素,索引位置从0开始.两种方式是一样的...
        print("访问一行三列位置元素", a[0][2], a[0, 2])
        # 修改指定位置的元素
        a[0][2] = -5
        print("修改后元素数组元素", a)
        # 沿指定轴获取最大值元素
        maxElement = a.max(0)
        print("最大值maxElement=", maxElement)
        # 和上边的方法等价
        elementMax = np.amax(a, 0)
        print("a=", elementMax)
        # 此处有amin方法获取最小元素数组,和amax一样不做演示了
        # 切片

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
    npy.ndarrayType()
