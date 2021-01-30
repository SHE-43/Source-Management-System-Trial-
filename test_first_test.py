import pandas as pd
import numpy as np

df = pd.DataFrame([[1,2,3],[5,5,5],[2,2,2],[4,3,2],[7,8,9]], columns = list("abc"))

df.iloc[0] = [9,9,9]

df= df.drop([2])

df = df.reset_index(drop=1)

df = df[0:0]

print(df)


path = r"C:\Users\ABC\Desktop\Source-Management-System-Trial--main\Source-Management-System-Trial--main\files_excel\SMS.xlsx"

df1 = pd.read_excel(path, dtype=object)
# print(df1.loc[df1["Customer ID"] == 10000])

# print(df1["Full Name"].str.contains("Avery").any())
print(df1[df1['Full Name'].str.contains('Avery', na = False)] )
print("\n")
# print(df1.str.contains("Avery").any())
print("\n")
# print(df1.isin([10000]).any(axis = 1))
print(df1.isin(["Av"]).any(axis = 1))
print("\n")
print(df1[df1.apply(lambda r: r.str.contains('Av', case=False).any(), axis=1)] )

print(df1.columns[df1.apply(lambda r: r.str.contains('Av', case=False).any(), axis=0)] )

print(df1.columns[df1.apply(lambda r: r.str.contains('Av', case=False).any(axis = 0))] )

print("\n")
print("\n")

print(df1.apply(lambda r: r.str.contains('C', case=False).any(), axis=1))
print(df1.apply(lambda r: r.str.contains('c', case=False).any(), axis=0))
# print("\n")

# print(df1.apply(lambda r: r.str.contains('C', case=False).any()))


arr = df1.values
# arr.dtype = object

# print(arr.contains("C"))
print(arr.dtype)
print(arr)
print(np.core.defchararray.find(arr.astype(str), 'C'))
print(df1[df1.apply(lambda r: r.str.contains('A', case=True).any(), axis=1)] )

print(df1[df1['Full Name'].str.contains('A', na = True)] )

df1.iloc[0,5] = np.nan

print(df1.iloc[:2])

print(df1[df1['Full Name'].str.contains('A', na = False)] )
print(df1[df1['Full Name'].str.contains('A', na = True, regex = False)] )
print("\n\n\n")
print(df1[df1['Full Name'].str.contains('Avery', na = True, regex = False)].index.values[0] )

i = df1[df1['Full Name'].str.contains('Avery', na = True, regex = False)].index.values[0] 



print([i] + df1.iloc[i].values.tolist())




