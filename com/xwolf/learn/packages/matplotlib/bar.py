
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties


class bar:

    def __init__(self):
        pass

    def bar(self):
        """

        :return:
        """
        # 中文字体支持
        font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
        movies = ["罗马假日", "硫磺岛家书", "紫日", "奥特曼", "美国沦陷"]
        num_oscars = [5, 11, 3, 8, 10]
        # 条形的默认宽度是0.8，因此我们对左侧坐标加上0.1
        # 这样每个条形就被放置在中心了
        xs = [i + 0.1 for i, _ in enumerate(movies)]
        # 使用左侧x坐标[xs]和高度[num_oscars]画条形图
        plt.bar(xs, num_oscars)
        plt.ylabel("所获奥斯卡金像奖数量", fontproperties=font)
        plt.title("我最喜爱的电影", fontproperties=font)
        # 使用电影的名字标记x轴，位置在x轴上条形的中心
        plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies, fontproperties=font)
        plt.show()


if __name__ == '__main__':
    bar = bar()
    bar.bar()
