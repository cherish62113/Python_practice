import pandas as pd

print("一、讀取csv檔案並列印DATE這行第0行至12行")
unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
print(unrate.head(12))

import matplotlib.pyplot as plt
print("二、plt.plot()要繪製的圖表，plt.show()顯示圖表")
#()為空，則會顯示一個空的圖表
plt.plot()
plt.show()

print("三、繪製檔案unrate第0列至12列")
first_twelve = unrate[0:12]
#           X軸                     Y軸
plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
plt.show()

print("四、繪製圖表 x,y軸的字體可以旋轉")
plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
# x軸 名稱顯示 旋轉45度 名字太長可以使用
plt.xticks(rotation=45)
plt.yticks(rotation=45)
#print help(plt.xticks)
plt.show()


#xlabel(): x軸的標題
#ylabel(): y軸的標題
#title():  整個圖表的標題
print("五、X,Y軸及圖表名稱")
plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
plt.xticks(rotation=90)
# x 軸的 數值名稱
plt.xlabel('Month')
# y 軸的 數值名稱
plt.ylabel('Unemployment Rate')
#圖表的名稱
plt.title('Monthly Unemployment Trends, 1948')
plt.show()