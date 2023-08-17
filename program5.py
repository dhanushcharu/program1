import pandas as pd
data=pd.read_csv("D:/Dataset/Iris_PCA.csv")
print(data)

print(data.head(5))

print(data.tail(10))

print(data.info())

print(data.dtypes)

print(data.count())
