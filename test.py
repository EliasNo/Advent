import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


# Import needed data
df = pd.read_csv (r'C:\Users\EliasNordlinder\OneDrive - Numberskills AB\Dokument\Input.txt', header=None)
df.head()

# Start coding
def Christmas_Function(df):
    # Function to solve Christmas
     for i in (df):
        output = (df/3).apply(np.floor)-2
        return output

output = Christmas_Function(df)
sum = output.sum()
print(sum)