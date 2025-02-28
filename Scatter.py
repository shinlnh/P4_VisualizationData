import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

data = pd.read_csv("diabetes.csv")
scatter_matrix(data)
plt.show()