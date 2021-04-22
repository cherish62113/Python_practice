import numpy as np
#創造5x5矩陣(元素為0-24)
a = np.arange(25).reshape(5,5)
print (a)
print("一、列交換")
#a[[0,4]] = a[[4,0]] 也行，預設為列
a[[4,0]] = a[[0,4]]
print (a)
print("二、行交換")
a[:,[0,1]] = a[:,[1,0]]
print(a)



#找出數列中最接近的數
z = np.array([[0,1,2,3],[4,5,6,7]])
a = 5.1
#abs, fabs 計算整數、浮點數或複數的絕對值。對於非複數值，可以使用更快的fabs。
#np.abs(z-a).argmin()   z為陣列，a為數，找出陣列中與給定值最接近的數，利用陣列進行資料處理 數學和統計方法
#argmin() 分別為最小值的索引
#argmax() 分別為最大值的索引
print("三、找出最接近的數，abs找出差距最小，argmin找最小的位置")
print (np.abs(z-a).argmin())



#判斷矩陣是否有每列or每行為0
print("建立一個2x10列表(元素值為0-2之間)")
z = np.random.randint(0,3,(2,10))
print (z)
print("四、判斷每一行是否為零")
print (z.any(axis=0))
print("五、判斷每一行是否為非零")
print (z.all(axis=0))

print("六、指令的介紹")
print(help(np.random.randint))

#np.linspace(star,end,均勻取numble)
print("七、一定的範圍內均勻取樣本數")
x=np.linspace(-1,1,3)
print(x)
y=np.linspace(2,4,2)
print(y)

print("代研究")  
#np.meshgrid (以為中心) ;(x,y)二維;(x,y,z)三維 
x,y = np.meshgrid(np.linspace(-1,1,3),np.linspace(2,4,2))
print (x)
print (y)
z=np.meshgrid(3,2)
print(z)
print(help(np.meshgrid))

print("八、畢氏定理")
D = np.sqrt(x**2+y**2)
print (D)
sigma,mu = 1,0
a = np.exp(-(D-mu)**2/(2*sigma**2))
print (a)
