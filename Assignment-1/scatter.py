# Data Visualization assignment 1
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("dataset.csv")
data.columns.values[5] = "gram"
plt.grid()
data = data[(data.gram == "positive")]

vac1 = data["Penicilin"] / 20
vac2 = data["Streptomycin "]
vac3 = data["Neomycin"]
labels = data["Bacteria "]


plt.scatter(labels, vac1, edgecolors='red', facecolors='none',
            marker='o', label='Penicilin positive')
plt.scatter(labels, vac2, edgecolors='red', facecolors='none',
            marker='s', label='Streptomycin positive')
plt.scatter(labels, vac3, edgecolors='red', facecolors='none',
            marker='^', label='Neomycin positive')
plt.xticks(rotation=90)


data = pd.read_csv("dataset.csv")
data.columns.values[5] = "gram"

data = data[(data.gram == "negative")]

vac1 = data["Penicilin"] / 20
vac2 = data["Streptomycin "]
vac3 = data["Neomycin"]
labels = data["Bacteria "]


plt.scatter(labels, vac1, edgecolors='b', facecolors='none',
            marker='^', label='Penicilin negative')
plt.scatter(labels, vac2, edgecolors='b', facecolors='none',
            marker='o', label='Streptomycin negative')
plt.scatter(labels, vac3, edgecolors='b', facecolors='none',
            marker='s', label='Neomycin negative')
plt.xticks(rotation=90)


plt.legend()
plt.show()
