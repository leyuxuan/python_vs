import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

data = pd.read_csv('data.csv')
plt.rcParams['font.family'] = ['SimHei']
plt.bar(data['建筑名称'],data["高度"])
plt.title('世界著名建筑高度')
plt.xlabel('建筑名字')
plt.ylabel('建筑高度(米)')
plt.show()
