import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("diabetes.csv")
data.hist()
plt.show()