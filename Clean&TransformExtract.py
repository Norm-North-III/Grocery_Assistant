import pandas as pd
df = pd.read_excel("DataExtractCostco1&2.xlsx",header=None,names=["Product_ID","Product","Price","Store","Date"])
df
df.head
df.size
df.shape
df["Product_ID"].apply(type)