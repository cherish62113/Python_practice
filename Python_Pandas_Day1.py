import pandas as pd
print("開啟csv檔")
#逗號分隔值（Comma-Separated Values，CSV，有時也稱為字元分隔值，因為分隔字元也可以不是逗號）
food_info = pd.read_csv("food_info.csv")
print("一、列印檔案資料型態")
print(type(food_info))
print("二、列印檔案內容的資料型態")
print (food_info.dtypes)
print("三、查詢指令")
print(help(pd.read_csv))

print("四、從文件內容的開頭資料放進 first_rows")
#預設顯示前五列
first_rows = food_info.head()  
print (first_rows)
print("五、列印文件前三列")
print(food_info.head(3))
print("六、列印文件的行名稱(標題列)")
print (food_info.columns)
print("七、列印文件內容大小(列數,行數) ")
print (food_info.shape)


print("八、列印第零列")
print (food_info.loc[0])

print("九、列印第七列(第一列為第零列)")
print(food_info.loc[6])

# print("十、若超過檔案索引顯示error")
# print(food_info.loc[8620])



#object - For string values
#int - For integer values
#float - For float values
#datetime - For time values
#bool - For Boolean values
print("十、列印資料型態")
print(food_info.dtypes)




print("十一、列印第3列-第6列(開頭為第零列)")
print(food_info.loc[3:6])

print("十二、列印指定列數(方法一)")
two_five_ten = [2,5,10] 
print(food_info.loc[two_five_ten])

print("十三、列印指定列數(方法二)")
print(food_info.loc[[2,5,10]])


print("十四、列印指定行數(方法一)")
ndb_col = food_info["NDB_No"]
print (ndb_col)

print("十五、列印指定行數(方法二)")
col_name = "NDB_No"
ndb_col = food_info[col_name]
print(ndb_col)



print("十六、列印指定行數(可以指定不只一行)(方法一)")
columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]
print (zinc_copper)


print("十七、列印指定行數(可以指定不只一行)(方法二)")
zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]
print (zinc_copper)


print("十八、列印行名(每一列開頭)")
print(food_info.columns)
print("十九、列印前3列(從0-2含標題)")
print(food_info.head(2))

print("二十、列印每行的名稱(列標題)")
col_names = food_info.columns.tolist()
print (col_names)


print("二一、判斷行名稱具有g中的前三列")
gram_columns = []
for c in col_names:
    if c.endswith("(g)"): #判斷結尾是否含有g
        gram_columns.append(c)
gram_df = food_info[gram_columns]
print(gram_df.head(3))