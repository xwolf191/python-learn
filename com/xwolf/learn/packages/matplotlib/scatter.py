from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

# 字体
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
# 价格
price = [769, 655, 533, 435, 365, 354, 143, 364, 67]
priceAndRoom = ['A', 'B', 'C', 'D', 'E', 'A1', 'A2', 'A3', 'A4']
plt.scatter(price, priceAndRoom)
plt.title("城市与楼盘价格", fontproperties=font)
plt.xlabel("城市", fontproperties=font)
plt.show()
