import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("cleaned_parallel_corpus.tsv", sep="\t\t\t\t\t", engine="python")

train_df, test_df = train_test_split(df, test_size=0.1, random_state=42)

train_df["en"].to_csv("en_train.txt", index=False, header=False)
train_df["kha"].to_csv("kha_train.txt", index=False, header=False)

test_df["en"].to_csv("en_eval.txt", index=False, header=False)
test_df["kha"].to_csv("kha_eval.txt", index=False, header=False)
