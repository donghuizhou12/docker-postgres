import sys 
import pandas as pd
print('argument', sys.argv)
print('Hello pipeline!')
print(sys.argv[0])
month=int(sys.argv[1])
print(month)
df =pd.DataFrame({'A':[1,2,3], 'B':[4,5,6]})
df['month']=month
print(df.head())
df.to_parquet (f'output_{month}.parquet')
print(df.month.dtype,df.columns)
# for dc in df.columns:
#     print(dc.dtype)
print(type(df.columns))