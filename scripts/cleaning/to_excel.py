import pandas as pd

df = pd.read_csv("merged.txt", sep="\0\t\t\t\t\t\t", header=None, engine="python")
# print(df.info())
df.to_excel("khasi_corpus.xlsx", "Sheet1", index=False)
