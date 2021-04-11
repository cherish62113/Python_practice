#載入 numpy 模組
import numpy as np

#創造一個列表元素個數為0~14 (15個) 矩陣形狀為3x5
a = np.arange(15).reshape(3, 5)
print("一、創造一個列表元素個數為0~14 (15個) 矩陣形狀為3x5")
print(a)
print("\n\n")

#矩陣形狀
print("二、印出列表的形狀")
print(a.shape)
print("\n\n")

#矩陣維度
print("三、列印出列表的維度")
print(a.ndim)
print("\n\n")

print("四、列印列表資料型態")
print (a.dtype)
print("五、列印列表的大小(元素個數)")
print (a.size)
print("\n\n")

print("六、建立一個3x4的零矩陣")
b = np.zeros ((3,4))
print(b)
print("\n\n")

print("七、建立一個2x3x4矩陣(3維)元素全是1")
c=np.ones((2,3,4), dtype=np.int32 )
print(c)
print("\n\n")


#numpy.arange(star,stop,step,dtype) 
print("八、使用range建立列表(類等差數列)")
e=np.arange( 10, 30, 5 )
print(e)
print("\n\n")


print("九、range進階使用")
f=np.arange( 0, 2, 0.3 )
print(f)
print("\n\n")

print("十、建立一個具12個元素之列表(4x3)")
g=np.arange(12).reshape(4,3)
print (g)
print("\n\n")


# np 模組中使用 pi  (np.pi)
#from numpy import pi 指令將np.pi 簡化為 pi
from numpy import pi
print("十一、建立一個等差級數的列表(從0開始)，2*pi 為等差，算100個")
h = np.linspace( 0, 2*pi, 100 )
print(h)
print("\n\n")


print("十二、取三角函數")
i=np.sin(np.linspace( 0, 2*pi, 100 ))
print(i)
print("\n\n")

print("十三、取三角函數")
j=np.sin(pi/6)
k=np.cos(pi/3)
print(j)
print(k)
print("\n\n")


a = np.array( [20,30,40,50] )
b = np.arange( 4 )
print("十四、創建兩個1x4列表")
print (a) 
print (b)

c = a-b
d = a+b 
print("十五、列表運算")
print (c)
print (d)
print("\n\n")


print("十六、平方運算")
print (b**2)
print("\n\n")


print("十七、比較運算")
print (a<35)
print("\n\n")



#建立兩個2x2矩陣
A = np.array( [[1,1],
               [0,1]] )
B = np.array( [[2,0],
               [3,4]] )
print (A)
print (B)
#print A*B
print("十八、矩陣乘積(3種指令)")
print (A.dot(B))
print("\n")
print (np.dot(A, B))
print("\n") 
print (A@B)
print("\n\n")

print("------------------------------")
print("Day3 結束")
print("------------------------------")
print("\n\n")