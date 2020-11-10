from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('dataset.csv')
df.head()

# Normalization
cols_to_norm = ['Penicilin', 'Streptomycin ', 'Neomycin']
df[cols_to_norm] = MinMaxScaler().fit_transform(df[cols_to_norm])

# Plotting

plt.bar(df["Bacteria "], df["Penicilin"].values,
        label="Penicilin", align='center', width=0.7)
plt.bar(df["Bacteria "], df["Streptomycin "].values,
        label="Streptomycin", align='center', width=0.7)
plt.bar(df["Bacteria "],  df["Neomycin"].values,
        label="Neomycin", align='center', width=0.7)
for i in range(len(df["Bacteria "])):

    plt.annotate("+Ve" if df["Gram Staining "][i] == "positive" else "-Ve", xy=(df["Bacteria "][i], max(
        df["Penicilin"].values[i], df["Streptomycin "].values[i], df["Neomycin"].values[i])), ha='center', va='bottom')

plt.xticks(rotation=-90)
plt.ylabel("Normalized Value")
plt.xlabel("Bacteria")
plt.title("Minimum Inhibitory Concentration (MIC) of the antibiotic\nAssignment 1: Visualization Design")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.subplots_adjust(bottom=0.4)
plt.savefig('plot.png')
plt.show()
