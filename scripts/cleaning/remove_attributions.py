import pandas

df = pandas.read_csv("parallel_corpus/kha.tsv", sep="\t")
df.pop("attribution")
df.to_csv("parallel_corpus/pc.csv", index=False)
