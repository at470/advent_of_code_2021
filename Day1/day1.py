import pandas as pd
import numpy as np

#part 1
#count how many positive differences there are
print("Part 1")

df = pd.read_csv("/Users/akikot/Day1/input.csv", names=["data"]) #add header name for data

df["offset_1"] = df["data"].shift(1) #lead by 1

df["delta_1"] = df["data"] - df["offset_1"]

#add a grouping column
df['group'] = 'data'

#count the number of entries
df_print = df.groupby(df['group'])['delta_1'].agg([('negative_count' , lambda x : x[x < 0].count()) 
	, ('positive_count' , lambda x : x[x > 0].count())])


#df_print = df.head(10) #print top 10 rows of dataframe

#print(df)

print(df_print['positive_count'])

print("End of Part 1")


#part 2
#same again but with lag 4
print("Part 2")

df["offset_3"] = df["data"].shift(3) #lead by 4

df["delta_3"] = df["data"] - df["offset_3"]


#count the number of entries
df_print = df.groupby(df['group'])['delta_3'].agg([('negative_count' , lambda x : x[x < 0].count()) 
	, ('positive_count' , lambda x : x[x > 0].count())])

#print(df)

print(df_print['positive_count'])

print("End of Part 2")