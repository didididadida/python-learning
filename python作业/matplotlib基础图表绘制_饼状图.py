import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
labels = ['一','二','三','四','五','六']
sizes = [1,4,5,8,13,14]
plt.pie(sizes,labels=labels,autopct='%1.1f%%',)
plt.show()

