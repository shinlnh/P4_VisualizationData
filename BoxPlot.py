import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("diabetes.csv")
data.plot(kind='box',subplots =True,layout=(3,3),sharex=False)
plt.show()