import pandas as pd

df = pd.read_pickle('Instagram_data.p')

df_reset = df.iloc[0:0]

print(df_reset)
#df_reset.to_pickle('Instagram_data.p')
'''
make sure to change the original pickle file name first!!
'''