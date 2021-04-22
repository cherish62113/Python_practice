#Series (collection of values)
#DataFrame (collection of Series objects)
#Panel (collection of DataFrame objects)


#A Series object can hold many data types, including
#float - for representing float values
#int - for representing integer values
#bool - for representing Boolean values
#datetime64[ns] - for representing date & time, without time-zone
#datetime64[ns, tz] - for representing date & time, with time-zone
#timedelta[ns] - for representing differences in dates & times (seconds, minutes, etc.)
#category - for representing categorical values
#object - for representing String values

#FILM - film name
#RottenTomatoes - Rotten Tomatoes critics average score
#RottenTomatoes_User - Rotten Tomatoes user average score
#RT_norm - Rotten Tomatoes critics average score (normalized to a 0 to 5 point system)
#RT_user_norm - Rotten Tomatoes user average score (normalized to a 0 to 5 point system)
#Metacritic - Metacritic critics average score
#Metacritic_User - Metacritic user average score



import pandas as pd
print("一、列印檔案內FILM、RottenTomatoes行第0~5列")
#讀取csv檔
fandango = pd.read_csv('fandango_score_comparison.csv')
series_film = fandango['FILM']
print(series_film[0:5])
series_rt = fandango['RottenTomatoes']
print (series_rt[0:5])

# Import the Series object from pandas
print("二、取FILM行的值，並列印值及值的類型")
from pandas import Series
film_names = series_film.values
print (type(film_names))
print (film_names)


print("三、列印RottenTomatoes行的值")
rt_scores = series_rt.values
print (rt_scores)
series_custom = Series(rt_scores , index=film_names)
# series_custom[['Minions (2015)', 'Leviathan (2014)']]

print("四、列印RottenTomatoes第5列-第9列的值")
# int index is also aviable
# series_custom = Series(rt_scores , index=film_names)
# series_custom[['Minions (2015)', 'Leviathan (2014)']]
fiveten = series_custom[5:10]
print(fiveten)



print("五、列印行標題(列元素)")
original_index = series_custom.index.tolist()
print (original_index)
print("六、對行標題排序，阿拉伯數字先(大到小)英文字(由a~z)")
sorted_index = sorted(original_index)
sorted_by_index = series_custom.reindex(sorted_index)
print (sorted_by_index)



print("七、列印對FILM排序的RottenTomatoes這行並列印出第0~9列")
sc2 = series_custom.sort_index()
print(sc2[0:10])
print("八、列印對RottenTomatoes的值做排序並列印出第0~9列")
sc3 = series_custom.sort_values()
print(sc3[0:10])





print("seriesu也被視為Numpy(一維)")
import numpy as np
print("九、將RottenTomatoes的值+RottenTomatoes的自己的值")
print (np.add(series_custom, series_custom))
print("十、再取其他運算")
print(np.sin(series_custom))
print(np.max(series_custom))


print("十一、列印RottenTomatoes大於50的值")
series_custom > 50
series_greater_than_50 = series_custom[series_custom > 50]
print(series_greater_than_50)

print("十二、附加條件需兩個條件都滿足")
criteria_one = series_custom > 50
criteria_two = series_custom < 75
both_criteria = series_custom[criteria_one & criteria_two]
print (both_criteria)


print("十三、RottenTomatoes的值+RottenTomatoes_User的值算平均")
rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])
rt_mean = (rt_critics + rt_users)/2
print(rt_mean)