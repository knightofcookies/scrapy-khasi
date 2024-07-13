with open("translated_parallel_corpus.tsv", "r", encoding="utf-8") as fp:
    lines = fp.readlines()

count = 0
for line in lines:
    count += line.count("\t\t\t\t\t")

print(count)
print(len(lines))
