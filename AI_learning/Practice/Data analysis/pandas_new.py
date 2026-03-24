import pandas as pd
dicti={'name':['Deepak','Swati'],'Lastname':['Pandey','Dubey'],'Place':['Saibasa','Semari'],'Age':[22,38]}
print(dicti)
df=pd.DataFrame(dicti) 
dl=pd.DataFrame([{'Deepak':'Pandey','Swati':'Dubey'}]) # if you want to pass values directly to dataframe, pass in list
print(df)

df2=pd.read_excel("Super_store.xlsx")

df2['Unit Price'].sum()
print(f"Total Unit Price: {df2['Unit Price'].sum()}")
print(df2.head())


comb=pd.concat([df,df2],axis=1)
print(comb)





