#載入 numpy 模組
import numpy as np

#創造一個1x4列表
vector1 = np.array([5, 10, 15, 20])

# == 是比較是否相等 
print("一、比較1x4列表元素是否與10相等")
print(vector1 == 10)
print("\n\n")



#創造一個3x3列表
matrix1 = np.array([
                    [5, 10, 15], 
                    [20, 25, 30],
                    [35, 40, 45]
                 ])
#比較3x3列表中元素是否有與25相等
print("二、比較3x3列表元素是否與25相等")
print(matrix1 == 25)
print("\n\n")



#創造一個1x4列表
vector2 = np.array([5, 10, 15, 20])

#比較是否與10相同 將結果放入 x
x = (vector2 == 10)

#印出x的結果  
print("三、比較1x4列表元素是否與10相等")
print(x)
print("\n\n")



#印出vector2[x]列表中的x    
print("四、列印1x4列表中元素x")
print(vector2[x])
print("\n\n")



#創造一個3x3的列表
matrix2 = np.array([
                [5, 10, 15], 
                [20, 25, 30],
                [35, 40, 45]
             ])

#比較每列的第1的元素是否與25相等   
y = (matrix2[:,1] == 25)

#印出比較結果
print("五、列印3x3列表中(第二行)元素是否與25相等")
print(y)
print("\n\n")



#印出y在的那一列
print("六、列印3x3列表中(y所在的那一列)元素")
print(matrix2[y,:])
print("\n\n")



#創造一個1x4的列表
vector3 = np.array([5, 10, 15, 20])

#比較1x4列表是否與10或5相等的元素
z = (vector3 == 10) & (vector3 == 5)
print("七、列印1x4列表中元素是否與10且5相等的元素")
print(z)
print("\n\n")



#創造一個1x4的列表
vector4 = np.array([5, 10, 15, 20])

#比較1x4列表中是否與10或5相等的元素
z = (vector4 == 10) | (vector4 == 5)
print("八、列印1x4列表中元素是否與10或5相等的元素")
print (z)
print("\n\n")


#創造一個1x4列表
vector5 = np.array([5, 10, 15, 20])

#比較1x4的列表中元素與10或5相同的元素
w = (vector5 == 10) | (vector5 == 5)

#將1x4列表中與10或5相同的元素改成50
vector5[w] = 50

#列印1x4列表並將與與原先是5或10的元素改成50
print("九、列印1x4列表並將與與原先是5或10的元素改成50")
print(vector5)
print("\n\n")



#創造一個3x3的列表
matrix3 = np.array([
            [5, 10, 15], 
            [20, 25, 30],
            [35, 40, 45]
         ])

#比較第二行的元素是否與25相同         
x = matrix3[:,1] == 25

#將3x3的列表將第二行元素是否與25相同並列印
print("十、將3x3的列表將第二行元素是否與25相同並列印")
print (x)
print("\n\n")



#將剛剛3x3的列表x所在的位置元素改成10
matrix3[x, 1] = 10

#將剛剛3x3的列表x所在的位置元素改成10並列印
print("十一、將剛剛3x3的列表x所在的位置元素改成10並列印")
print (matrix3)
print("\n\n")



#We can convert the data type of an array with the ndarray.astype() method.
#創造一個1x3的列表，裡面元素型態為字串
vector6 = np.array(["1", "2", "3"])

#列印 vector6 的資料型態
print("十二、列印 vector6 的資料型態")
print(vector6.dtype)
print("\n\n")



#列印 vector6 資料
print("十三、列印 vector6 的資料")
print(vector6)
print("\n\n")



#將 vector6 的資料型態更改為浮點數(小數)                 # .astype
vector6 = vector6.astype(float)

#列印 vector6 的資料型態
print("十四、列印 vector6 的資料型態")
print(vector6.dtype)
print("\n\n")



print("十五、列印 vector6 的資料")
print(vector6)
print("\n\n")


#創造一個1x4的列表
vector7 = np.array([5, 10, 15, 20])
#將1x4列表中所有元素相加
print("十六、將1x4列表中所有元素相加")
print(vector7.sum())
print("\n\n")



#創造一個3x3的列表
matrix4 = np.array([
                [5, 10, 15], 
                [20, 25, 30],
                [35, 40, 45]
             ])
#列印每一列的加總
print("十七、列印每一列的加總")
print(matrix4.sum(axis=1))
print("\n\n")



#列印每一列的加總
print("十八、列印每一行的加總")
print(matrix4.sum(axis=0))
print("\n\n")


print("------------------------------")
print("Day2 結束")
print("------------------------------")
print("\n\n")
