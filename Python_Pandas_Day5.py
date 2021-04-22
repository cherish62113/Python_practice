#載入Pandas模組
import pandas as pd
print("一、讀取檔案並列印檔案資料類型")
fandango = pd.read_csv('fandango_score_comparison.csv')
print (type(fandango))
print("\n\n")

print("二、印FILM行 drop：不去掉含有NaN的列")
fandango_films = fandango.set_index('FILM', drop=False)
print(fandango_films.index)

print("三、列印指定列數(不加loc)預設也是列印列數")
x=fandango_films["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]
print(x)
print("\n\n")
y=fandango_films.loc["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]
print(y)
print("\n\n")
print("只指定列印 Kumiko, The Treasure Hunter (2015)這列的資訊")
z=fandango_films.loc['Kumiko, The Treasure Hunter (2015)']
print(z)
print("\n\n")

print("四、指定列印")
movies = ['Kumiko, The Treasure Hunter (2015)', 'Do You Believe? (2015)', 'Ant-Man (2015)']
print(fandango_films.loc[movies])

#When selecting multiple rows, a DataFrame is returned, 
#but when selecting an individual row, a Series object is returned instead
#The apply() method in Pandas allows us to specify Python logic
#The apply() method requires you to pass in a vectorized operation 
#that can be applied over each Series object.
import numpy as np

# returns the data types as a Series
types = fandango_films.dtypes
print (types)
print("\n\n")
# filter data types to just floats, index attributes returns just column names
print("五、只列印列標題的行內的元入資料型態為float64")
float_columns = types[types.values == 'float64'].index
print(float_columns)
print("\n\n")
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]
print (float_df)
print("\n\n")
# `x` is a Series object representing a column
print("六、對lambda x 做標準差")
deviations = float_df.apply(lambda x: np.std(x))
rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_user.apply(lambda x: np.std(x), axis=1)