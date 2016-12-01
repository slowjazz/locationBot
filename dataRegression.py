import numpy as np
import pandas as pd

data = pd.read_csv('crime.csv')
data = data[['Dispatch_Date_Time','Text_General_Code','Lon','Lat']]
headers = list(data.columns.values)

print headers