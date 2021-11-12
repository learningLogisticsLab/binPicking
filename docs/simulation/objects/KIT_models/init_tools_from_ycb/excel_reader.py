import pandas as pd
path = "object_categories_db.xlsx"

df = pd.read_excel(path, sheet_name="database_real", engine="openpyxl")
print(df.head())

id=66
# given object id, get the mass from excel
mass = int(df.mass[id][:3])/1000
print(mass)




