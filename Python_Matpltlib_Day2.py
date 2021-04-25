import pandas as pd
import matplotlib.pyplot as plt
print("一、讀取檔案(0~12列)繪製圖表設定xy軸及圖表名稱，")
unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
first_twelve = unrate[0:12]
plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
plt.xticks(rotation=90)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')
plt.show()


import matplotlib.pyplot as plt
print("二、取圖表的子圖")
#繪製圖表的宇集合
fig = plt.figure()
#(只取子圖：想像成3x2矩陣 取第1個元素)
ax1 = fig.add_subplot(3,2,1)
#(只取子圖：想像成3x2矩陣 取第2個元素)
ax2 = fig.add_subplot(3,2,2)
#(只取子圖：想像成3x2矩陣 取第6個元素)
ax2 = fig.add_subplot(3,2,6)
plt.show()

import numpy as np
print("三、設定宇集合(想像成矩陣)，並在子圖上隨便畫")
#設定繪製宇集合大小 3x3
fig = plt.figure(figsize=(3, 3))
#取其中2x1的第1個元素
ax1 = fig.add_subplot(2,1,1)
#取其中2x1的第2個元素
ax2 = fig.add_subplot(2,1,2)
plt.show()
#在ax1子圖上繪製圖表
ax1.plot(np.random.randint(1,5,5), np.arange(5))
#在ax2子圖上繪製圖表
ax2.plot(np.arange(10)*3, np.arange(10))
plt.show()

print("四、在圖表上畫出兩條折線")
unrate['MONTH'] = unrate['DATE'].dt.month
unrate['MONTH'] = unrate['DATE'].dt.month
fig = plt.figure(figsize=(6,3))
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c='red')
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], c='blue')
plt.show()

print("五、使用迴圈畫出多條折線")
fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i])
    
plt.show()

print("六、賦予折線名稱(迴圈中)，及定義名稱位置")
fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
#決定legend放那個位置，best找出最佳位置。
plt.legend(loc='best')
#print help(plt.legend)
plt.show()

ptint("七、加上xy軸及圖表名稱")
fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')
plt.xlabel('Month, Integer')
plt.ylabel('Unemployment Rate, Percent')
plt.title('Monthly Unemployment Trends, 1948-1952')

plt.show()