import pandas as pd

df = pd.read_csv("pc_eval.csv")

kha_lines = []
en_lines = []

for en_line in df["english"]:
    en_lines.append(en_line.strip() + "\n")

for kha_line in df["khasi"]:
    kha_lines.append(kha_line.strip() + "\n")

with open("en_eval.txt", "w", encoding="utf-8") as fp:
    fp.writelines(en_lines)

with open("kha_eval.txt", "w", encoding="utf-8") as fp:
    fp.writelines(kha_lines)
