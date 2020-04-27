import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 饼图
labels = 'Chrome', 'IE', 'FireFox', 'Opera'
#
sizes = [40, 20, 35, 5]
# 图形中的偏移弧度
explode = (0, 0.1, 0, 0)
# 字体大小
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.title('浏览器市场占有率', fontproperties=font)
# 保证图形为圆形
ax1.axis('equal')
plt.show()