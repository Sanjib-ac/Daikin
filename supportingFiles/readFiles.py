"""Read the test stand files"""
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os

path = os.path.join(os.getcwd(), "Data")
print(f'Current path: {path}')
# for count, filename in enumerate(os.listdir(path)):
#     print(count, filename)

fileName = '0331250-00100.csv'
f = path + '\\' + fileName
df = pd.read_csv(f, delimiter=',')
print(df.columns)