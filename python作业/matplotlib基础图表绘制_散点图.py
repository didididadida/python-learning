
import numpy as np
import matplotlib.pyplot as plt

#绘制两组100个随机数的散点图
x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x, y)
plt.show()
