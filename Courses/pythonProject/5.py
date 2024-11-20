import numpy as np
import pandas as pd

df = pd.read_csv('input.csv')

unicue_values = df.nunique()

if unicue_values.get('Unnamed: 0') == 0:
    print(False)
else:
    print(True)


