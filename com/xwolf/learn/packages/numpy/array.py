import numpy as np

aary = [[1, 2, 3], [2, 3, -5], [4, 7, 1]]
a = np.array(aary)
print(a)
# 转置
ta = a.transpose()
print(ta)
# 行列式的值
aalg = np.linalg.det(aary)
print(aalg)
