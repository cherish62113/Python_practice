import numpy as np
B = np.arange(3)
print("建立一個1x4之列表")
print (B)

print("一、以自然數e為底的次方運算")
print (np.exp(B))
print("\n\n")


print("二、開根號運算(兩種方法)")
print (np.sqrt(B))
print (B**0.5)
print("\n\n")

#np.random.random((形狀))  值 0~1之間
#floor取下限整數 EX: 3.4 = 3
print("三、建立一個3x4隨機列表(值0-1之間)取floor")
a = np.floor(10*np.random.random((3,4)))
print (a)
print("\n\n")


print("列表形狀操作")
print(a.shape)
print("\n\n")


print("四、將列表變成一維陣列")
print (a.ravel())
print("\n\n")


print("五、將矩陣轉置")
print (a.T)
print("\n\n")


print("六、更改列表形狀(但元素個數必須相同)")
a.shape = (6,2)
print (a)
print("\n\n")


print("七、更改列表大小(元素個數)超過原先列表元素將以零代之")
a.resize((2,6))
print (a)
print("\n\n")


print("建立兩個2x2列表")
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print("矩陣操作")
print (a)
print ("----------")
print (b)
print ('----------')
print("七、個人猜測【Horizontal】橫向堆疊(合併)矩陣")
print (np.hstack((a,b)))
print("\n\n")


print("八、個人猜測【vertical】垂直(堆疊)合併矩陣")
print (np.vstack((a,b)))
print("\n\n")

print("隨機建立(2x12)列表 10*(元素0~1)取Floor")
a = np.floor(10*np.random.random((2,12)))
print (a)
print("九、將矩陣a(橫向)分割(縱刀)成3個矩陣")
print (np.hsplit(a,3))
print("十、將矩陣a由(列的第3個元素(第4行)及第4個元素(第5行)做分割【第1個位置為0，分割線放左邊變array】")
print (np.hsplit(a,(3,4)))   
print ("\n\n")

print("隨機建立(12x2)列表 10*(元素0~1)取Floor")
a = np.floor(10*np.random.random((12,2)))
print (a)
print("十一、將矩陣a(縱向)分割(橫刀)成3個矩陣")
print (np.vsplit(a,3))
print("十二、將矩陣a由(行的第3個元素(第4列)及第4個元素(第5列)做分割【第1個位置為0，分割線放上邊變array】")
print (np.vsplit(a,(3,6,8)))
print("\n\n")


print("建造一個(1x4)列表0~11")
a = (np.arange(12))
b = a
print("a列表：",a)
print("----------")
print("b列表：",b)
print("\n")
print("十三、a & b 2個變數皆代表同一個(多維度)陣列")
b is a
print("更改列表形狀")
b.shape = 3,4
print (a.shape)
print("----------")
print(a)
print("----------")
print(b)
print("----------")

print("十四、列印a & b 所對應之列表ID(相同代表共用同一個列表)")
print (id(a))
print (id(b))
print("\n\n")



print("十五、Data是一樣的但形狀可改變")
c = a.view()
c is a
c.shape = 2,6
print (a.shape)
c[0,4] = 1234
print ("改變C的形狀(但元素不變)")
print(c)
print ("改變c列表元素A列表也會跟著改變(共用資料)")
print(a)
print("----------")
print("代表共用資料但是不同兩個列表")
print(id(a))
print(id(c))
print("\n\n")




print("十六、copy將不影響原本的列表")
d = a.copy() 
d is a
d[0,0] = 9999
print("改變d列表中的元素")
print (d) 
print("\n")
print("a列表保持不變(不共用資料)")
print (a)
print("\n")
print("表示a & c 為不同的列表也不共用資料")
print(id(a))
print(id(c))

print("\n\n")
