# Data Visualization assignment 1
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("dataset.csv")


data.columns.values[5] = "gram"

vac1 = data["Penicilin"] / 20
vac2 = data["Streptomycin "]
vac3 = data["Neomycin"]
labels = data["Bacteria "]
# libraries

# multiple line plot
plt.plot(labels, vac1,  marker='o', linewidth=2,
         color='blue', label="Penicilin")
plt.plot(labels, vac2, linewidth=2, marker='o',
         color='red', label="Streptomycin")
plt.plot(labels, vac3, linewidth=2, marker='o',
         color='green',  label="Neomycin")
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.4)
plt.legend()
plt.show()
