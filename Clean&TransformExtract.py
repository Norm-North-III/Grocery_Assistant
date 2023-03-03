import pandas as pd
import datetime as dt
df = pd.read_excel("DataExtractCostco1&2.xlsx",header=None,names=["Product_ID","Product","Price","Store","Date"],)
df
df.head
df.size
df.shape
df["Product_ID"].apply(type)
r_date = str(input(f"What is the date listed on the receipt \nEnsure format is MM/DD/YYYY \n"))
r_month = int(r_date.split("/")[0])
r_day = int(r_date.split("/")[1])
r_year = int(r_date.split("/")[2])
r_date = dt.date(r_year,r_month,r_day)
print(r_date)
df["Date"] = r_date
df.reindex()
df
df.loc[2]