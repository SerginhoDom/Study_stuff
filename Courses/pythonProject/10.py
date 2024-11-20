import pandas as pd

df = pd.read_csv('input.csv')

unicue_values = df.nunique()

if unicue_values.get('1') < 2:
    print(0)
else:
    print(unicue_values.get('1') - 2)
