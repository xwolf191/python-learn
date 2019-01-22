# coding:utf8

"""
matplotlib 练手示例
"""
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties


class linePlot:

    def __init__(self):
        pass

    def line(self):

        """
        折线图
        :return:
        """
        font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
        years = ['<1', '1', '2', '3-5', '6-10', '10>', '30>', '60>']
        income = [3000, 4200, 8700, 18000, 24000, 30000, 5000, 2000]
        # 创建一幅线图，x轴是工作年限，y轴是收入
        plt.plot(years, income, color='red', marker='o', linestyle='solid')
        # 添加一个标题
        plt.title("工作年限和收入关系", fontproperties=font)
        # 给x轴加标记
        plt.xlabel("工作年限", fontproperties=font)
        # 给y轴加标记
        plt.ylabel("元", fontproperties=font)
        plt.show()


if __name__ == '__main__':
    p = linePlot()
    p.line()

