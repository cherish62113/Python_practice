import pandas as pd
from pandas import Series,DataFrame
import numpy as np
print("一、讀取csv檔並列印")
titanic_survival = pd.read_csv("titanic_train.csv")
print(titanic_survival.head())

print("二、列印此檔案的(Age行)前10列(標題列0~9列)")
age = titanic_survival["Age"]
print(age.loc[0:10])
print("三、判斷age這欄是否有NaN")
age_is_null = pd.isnull(age)
print (age_is_null)
print("四、只列印AGE行空值得列數")
age_null_true = age[age_is_null]
print (age_null_true)
print("五、計算NaN的數量")
age_null_count = len(age_null_true)
print(age_null_count)

print("六、對缺值做處理，計算平均數")
mean_age = sum(titanic_survival['Age'])/len(titanic_survival['Age'])
print ("平均年齡：",mean_age)

print("七、對非空值做運算(方法一)平均數")
good_ages = titanic_survival["Age"][age_is_null == False]
print (good_ages)
print("八、對空值做運算(方法二)平均數")
correct_mean_age = sum(good_ages) / len(good_ages)
print (correct_mean_age)
print("九、對空值做運算(方法三)，平均數忽略NaN算出平均值")
correct_mean_age = titanic_survival["Age"].mean()
print (correct_mean_age)

print("十、定義")
passenger_classes = [1, 2, 3]
fares_by_class = {}
for this_class in passenger_classes:
    pclass_rows = titanic_survival[titanic_survival["Pclass"] == this_class]
    pclass_fares = pclass_rows["Fare"]
    fare_for_class = pclass_fares.mean()
    fares_by_class[this_class] = fare_for_class
print (fares_by_class)

print("十一、運算index代表(依哪行資訊)分組,value代表要運算的值，aggfunc代表如何運算")
passenger_survival = titanic_survival.pivot_table(index="Pclass", values="Survived", aggfunc=np.mean)
print (passenger_survival)

print("十二、預設運算為平均數")
passenger_age = titanic_survival.pivot_table(index="Pclass", values="Age")
print(passenger_age)

print("十三、以Embarked分組，對資料(fare及Survived)作運算和")
port_stats = titanic_survival.pivot_table(index="Embarked", values=["Fare","Survived"], aggfunc=np.sum)
print(port_stats)



# dropna： 去掉含有NaN的值
# drop  ：去掉含有NaN的行列
# fillna：將含有NaN的值以（0，平均值，中值等）代替

print("十四、去掉含有NaN的值的列標題那(行)")
drop_na_columns = titanic_survival.dropna(axis=1)
print (drop_na_columns)
new_titanic_survival = titanic_survival.dropna(axis=0,subset=["Age", "Sex"])
print("十五、列印Age、Sex兩行並去掉含有NaN的值")
print (new_titanic_survival)
print("十六、列印Age行第83個(列)元素")
row_index_83_age = titanic_survival.loc[83,"Age"]
print (row_index_83_age)
print("十七、列印Pclass行第766個(列)元素")
row_index_1000_pclass = titanic_survival.loc[766,"Pclass"]
print (row_index_1000_pclass)

print("十八、資料排序(反序)")
new_titanic_survival = titanic_survival.sort_values("Age",ascending=False)
print (new_titanic_survival[0:10])
print("十九、資料排序(正序)")
new_titanic_survival = titanic_survival.sort_values("Age",ascending=True)
print (new_titanic_survival[0:10])
print("二十、 【待研究】 (猜測解決別名問題(drop=True))")
titanic_reindexed = new_titanic_survival.reset_index(drop=True)
print(titanic_reindexed.iloc[0:10])


#定義 hundredth_row(column)
#.iloc[0] 和 .iloc[[0]] 的差別就是一個取出的型態是 Series ，另一個是 DataFrame。
def hundredth_row(column):
    hundredth_item = column.iloc[99]
    return hundredth_item

print("二十一、印出每一行的第99個元素")
hundredth_row = titanic_survival.apply(hundredth_row)
print (hundredth_row)


#pd.isnull(column) 判斷行內元素是否有null值
print("定義各行Null值得數量")
def not_null_count(column):
    column_null = pd.isnull(column)
    null = column[column_null]
    return len(null)

print("二十二、列印各行Null值得數量")
column_null_count = titanic_survival.apply(not_null_count)
print (column_null_count)

print("定義Pclass欄位1、2、3分別回傳First Class、Second Class、Third Class")
def which_class(row):
    pclass = row['Pclass']
    if pd.isnull(pclass):
        return "Unknown"
    elif pclass == 1:
        return "First Class"
    elif pclass == 2:
        return "Second Class"
    elif pclass == 3:
        return "Third Class"

print("二十三、使用定義which_class將Pclass欄位列印回傳結果")
classes = titanic_survival.apply(which_class, axis=1)
print (classes)


print("定義年齡小於18歲回傳Ture")
def is_minor(row):
    if row["Age"] < 18:
        return True
    else:
        return False

print("二十四、使用定義列印每一列年齡大於18歲為True否則為False")
minors = titanic_survival.apply(is_minor, axis=1)
print (minors)


print("定義將Age小於18回傳minor、大於18回傳adult、NaN回傳unknown")
def generate_age_label(row):
    age = row["Age"]
    if pd.isnull(age):
        return "unknown"
    elif age < 18:
        return "minor"
    else:
        return "adult"

print("二十五、使用定義列印年齡NaN為unknown小於18歲為minor大於18則為adult")
age_labels = titanic_survival.apply(generate_age_label, axis=1)
print (age_labels)


print("二十六、計算平均數")
titanic_survival['age_labels'] = age_labels
age_group_survival = titanic_survival.pivot_table(index="age_labels", values="Survived")
print (age_group_survival)