#Create DataFrame Using pandas and write the contents of that DataFrame in xlsx file using ExecelWriter

import pandas as pd 

data = [{'Name':'PPA','Duration':4,'Fees':393939},{'Name':'LB','Duration':4,'Fees':3939},{'Name':'ANG','Duration':9,'Fees':5432}]
df = pd.DataFrame(data)

print(df)


writer = pd.ExcelWriter("File.xlsx",engine='xlsxwriter')

df.to_excel(writer,sheet_name="Sheet1")

writer.save()