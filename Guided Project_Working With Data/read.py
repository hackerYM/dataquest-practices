
import pandas as pd

contents = pd.read_csv('data/CRDC2013_14content.csv')

print(contents.columns)
print(contents['NAME'].head(10))