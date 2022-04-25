import pickle
import pandas as pd
import re

# obtaining the number of rows
movies_id = 1

df = pd.read_csv("Knn.csv")

var = df.loc[df['movieId'] == movies_id]
##var['recommendation'].values.tolist()
recommendation = var['recommendation'].values.tolist()
##var['recommendation'].to_string(index=False)
recommendations = recommendation[0].replace('[', '').replace(']', '').replace('"',"'")
# value = re.split('; |, ’|, “', recommendations)
# print(value[1])
for i in range(10):
    print(recommendations.split(", '")[i].replace("'",''))






