import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

data = pd.read_csv("diabetes.csv")
sn.heatmap(data.corr(),annot=True)
plt.show()