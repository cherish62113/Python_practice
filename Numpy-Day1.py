#安裝 Numpy 終端機輸入 "pip install numpy"
# 載入 Numpy 模組 設定別名 np
import numpy as np 

#開啟文本
# 自訂變數 = np.genfromtxt("檔名.txt", delimiter=",", dtype="U75", skip_header=1)
#delimiter=","表示每列的資料之間使用，做分隔符號
#dtype="U75"表示資料以字串方式置入（75為置入的字的個數)
#skip_header=1 ：表示從txt的第1列開始讀取(開頭為第零列)
txt = np.genfromtxt("world_alcohol.txt", delimiter=",", dtype="U75", skip_header=1)  

#會列印出 NaN (Not a Number)  無法表示 
print("一、印出文本內容(跳過第零列)")
print(txt)
print("\n\n")  

print("二、印出檔案的類型")
print(type(txt))
print("\n\n")   

#建立一個1x4的列表
vector = np.array([5, 10, 15, 20]) # 1x4
#建立一個3x3的列表 
matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print ("三、列印剛剛所創1x4及3x3列表")
print (vector)
print (matrix)
print("\n\n")   

print("四、列印vector的列表形狀")
print(vector.shape)
print("\n\n")

print("五、列印vector的列表大小(元素個數)")
print(vector.size)
print("\n\n")

#建立一個2x3的列表          
matrix = np.array([[5, 10, 15], [20, 25, 30]])

print("六、列印matrix的列表形狀")
print(matrix.shape)
print("\n\n")

print("七、列印matrix的列表大小(元素個數)")
print(matrix.size)
print("\n\n")

#列表中每個元素必須為同類型 - 整數
numbers = np.array([1, 2, 3, 4])

print("八、列印出此列表元素的資料型態")
print(numbers.dtype)
print("\n\n")

#列表中每個元素必須為同類型 - 浮點數(小數)
numbers = np.array([1.214, 2, 3, 4])
print("九、列印出此列表元素的資料型態")
print(numbers.dtype)
print("\n\n")

#開頭皆為第0行第0列
#指定文本列表中 [1,4] 第二列第五行的元素 放進 x 變數
x = txt[1,4] 
#指定文本列表中 [2,2] 第三列第三行的元素 放進 y 變數
y = txt[2,2] 
print("十、列印出文本內列表位置[1,4][2,2]的元素")
print (x)
print (y)
print("\n\n")

# #創造一個1x4列表
# vector = np.array([5, 10, 15, 20])
#紙列印從第0個到第2個(不包含3)    印出5,10,15
print("十一、只列印vector列表中從第0個到第2個(不包含3)的元素")
print(vector[0:3]) 
print("\n\n") 

#創造一個3x3的列表 (二維)
matrix = np.array([
                    [5, 10, 15], 
                    [20, 25, 30],
                    [35, 40, 45]
                    ])
print("十二、列印第二行元素")                    
print(matrix[:,1]) 
print("\n\n")

print("十三、列印每列的第零個元素到第一個元素")
print(matrix[:,0:2])
print("\n\n")


print("------------------------------")
print("Day1 結束")
print("------------------------------")
print("\n\n")
