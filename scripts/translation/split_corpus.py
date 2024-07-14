with open("cleaned_parallel_corpus.tsv", "r", encoding="utf-8") as fp:
    lines = fp.readlines()

kha_lines = []
en_lines = []

for line in lines:
    en_line, kha_line = line.split("\t\t\t\t\t")
    en_lines.append(en_line.strip() + "\n")
    kha_lines.append(kha_line.strip() + "\n")

with open("en.txt", "w", encoding="utf-8") as fp:
    fp.writelines(en_lines)

with open("kha.txt", "w", encoding="utf-8") as fp:
    fp.writelines(kha_lines)
