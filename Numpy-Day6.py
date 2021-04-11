#載入 Numpy 模組
import numpy as np
print("一、建立一個8x8的列表【元素皆為1】")
z = np.ones((8,8))
print (z)
print("二、建立一個8x8的列表【元素皆為0】")
z = np.zeros((8,8),dtype=int)
print (z)

# z [開始位置::距離下一列的距離]
#z[1::4] 第1列都為1    下一列(1+4=5)皆為1  
#  列     行
# 1::2 , ::2

print("三、第1列(含)每隔兩列 & 第0行(含)每隔兩行 =1 ")
z[1::2,::2] = 1
print (z)
print("四、第0列(含)每隔兩列 & 第1行每隔兩行 =1 ")
z[::2,1::2] = 1
print (z)


print("五、隨機建立5x5列表元素0~1之間")
x = np.random.random((5,5))
print(x)
print("六、列印出x列表中最小值")
x1 = x.min()
print("min",x1)
print("七、列印出X列表中最大值")
x2 = x.max()
print("max",x2)
print("八、列印最大值及最小值")
x3,x4=x.min(),x.max()
print("九、特別印法")
print(f"最小值：{x3}"f"最大值：{x4}")
print(x3,x4)



print("隨機建立一個5x5列表(元素0-10之間)")
z = 10*np.random.random((5,5))
print (z)
print("九、列表最小最大值運算")
zmin,zmax = z.min(),z.max()
z = (z-zmin)/(zmax-zmin)                  
print (z)

print("建立一個5x5列表(元素都為0-4)")
o = np.zeros((5,5))
o += np.arange(5)
print (np.arange(5))
print (o)

# #生成0~10之间均匀分布的11个数，包括0和10
#np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
                          #個數   #包含(stop)結束 #以多少為底數 #dtype : bool(布林值), int(整數), float(浮點數), complex(複數)
#numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
                #起點  #終點  #取樣數  #是否包含終點  #True 列印樣本距離 
print("十、從指定範圍內挑出樣本(樣本數自訂)，選擇是否包含起終點與是否列印樣本間隔")
z = np.linspace(0,10,4,endpoint=True,retstep=True)
print (z)

print("十一、指定範圍分別列印出代入Log內運算")
e=np.logspace(0,2, num=2, endpoint=True, base=2, dtype=None)
print(e)
