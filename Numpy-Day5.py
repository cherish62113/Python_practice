#載入 numpy 模組
import numpy as np
print("一、建立一個5x4列表(元素分別為sin0,sin1,...,sin19)")
data = np.sin(np.arange(20)).reshape(5,4)
print (data)
print("\n\n")

print("二、找出每行的最大值的【位置】")
ind = data.argmax(axis=0)
print (ind)
print("\n\n")


#Python3.0↑　xrange()包含在 range()
print("三、從range列表中選出最大值列印【以一維列表呈現】")
data_max = data[ind, range(data.shape[1])] 
print (data_max)
print("\n\n")


print("四、比較兩邊的列表元素全相同則顯示True")
print(all(data_max == data.max(axis=0)))
print("\n\n")


print("五、比較兩邊的列表只要存在一個元素相等則顯示True")
print(any(data_max == data.max(axis=0)))
print("\n\n")



print("六、arange(start,end(不含),等差10)")
a = np.arange(0, 40, 10)
print (a)
print("\n\n")


print("七、建立3x5表格內容元素為a")
b = np.tile(a, (3, 5)) 
print (b)
print("\n\n")

print("八、建立1x4表格內容元素為a")
b = np.tile(a, (1, 4))
print (b)
print("\n\n")


print("建立一個2x3的列表")
a = np.array([[4, 3, 5], [1, 2, 1]])
print (a)
print("\n\n")

print("九、每一列由小到大做排序")
b = np.sort(a, axis=1)
print (b)
print("\n\n")


print("九、每一行由小到大做排序")
b = np.sort(a, axis=0)
print(b)
print("\n\n")

print("十、a列表,每一列由小到大做排序")
a.sort(axis=1)
print (a)
print("\n\n")

print("十一、判斷是否為同一個列表")
print (id(a))
print (id(b))
print("\n\n")


print("建立1x4的列表")
a = np.array([4, 3, 1, 2])
print("十二、argsort 將列表由小到大的【位置】做排序")
j = np.argsort(a)
print (j)
print("十三、將列印a列表中[位置]，【由小到大】")
print (a[j])
