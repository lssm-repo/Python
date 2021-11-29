Import pandas as pd 

# Edit file path 
file = '/directory/file_name.xlsx'

# Save First Sheet to dataframe1 
df1 = pd.read_excel(file,0)
# Save Third Sheet to dataframe3 
df3 = pd.read_excel(file,2)

# Merge 2 sheets on Column Name
# Edit Column Name 
merge = pd.merge(df1, df3, on="Column Name")
print(merge)

# Output to excel file 
# Edit merge_file name
merge.to_excel("merge_file.xlsx")
