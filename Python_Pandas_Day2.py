# import pandas as pd
# print("讀取檔案")
# food_info = pd.read_csv("food_info.csv")
# print("一、將文件內的行名(列標題)放入col_name變數並列印")
# col_names = food_info.columns.tolist()
# print(col_names)
# print("二、列印3列(分別為【列標題】第0列，第1列，第2列)")
# print(food_info.head(3))


# print("三、列印Iron_(mg)這一行")
# print (food_info["Iron_(mg)"])
# print("四、直接取值做運算")
# print("除法")
# div_1000 = food_info["Iron_(mg)"] / 1000
# print (div_1000)
# print("加法")
# add_100 = food_info["Iron_(mg)"] + 100
# print(add_100)
# print("減法")
# sub_100 = food_info["Iron_(mg)"] - 100
# print(sub_100)
# print("乘法")
# mult_2 = food_info["Iron_(mg)"]*2
# print(mult_2)




# print("五、也可以直接取兩個值直接做運算")
# print(food_info["Water_(g)"])
# print(food_info["Energ_Kcal"])
# water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
# print(water_energy)

# print("六、新增資料(並不影響原檔案)")
# print(food_info["Iron_(mg)"])
# iron_grams = food_info["Iron_(mg)"] / 1000  
# food_info["Iron_(g)"] = iron_grams
# print(food_info["Iron_(mg)"])
# print(food_info["Iron_(g)"])


# print("七、較複雜的取值運算")
# weighted_protein = food_info["Protein_(g)"] * 2
# weighted_fat = -0.75 * food_info["Lipid_Tot_(g)"]
# initial_rating = weighted_protein + weighted_fat
# print(initial_rating)


print("八、取最大值並做運算，新增資料並不影響原檔案")
max_calories = food_info["Energ_Kcal"].max()
normalized_calories = food_info["Energ_Kcal"] / max_calories
normalized_protein = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
normalized_fat = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()
food_info["Normalized_Protein"] = normalized_protein
food_info["Normalized_Fat"] = normalized_fat
print(normalized_protein)






# print("九、 inplace=True 不額外新增資料，直接使用原資料做運算修改")
# print (food_info["Sodium_(mg)"])
# food_info.sort_values("Sodium_(mg)", inplace=True)
# print (food_info["Sodium_(mg)"])

# print("十、將資料進行排序 ascending=False 為降序")
# food_info.sort_values("Sodium_(mg)", inplace=True, ascending=False)  
# print (food_info["Sodium_(mg)"])
# print("十一、將資料進行排序 ascending=False 為升序")
# food_info.sort_values("Sodium_(mg)", inplace=True, ascending=True)
# print (food_info["Sodium_(mg)"])