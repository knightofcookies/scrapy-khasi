with open("../scripts/translation/cleaned_parallel_corpus.tsv", "r", encoding="utf-8") as fp:
    lines_1 = fp.readlines()


with open("translated_parallel_corpus_2.tsv", "r", encoding="utf-8") as fp:
    lines_2 = fp.readlines()

lines = lines_1 + lines_2
lines = sorted(lines, key=len)

with open("unified.tsv", "w", encoding="utf-8") as fp:
    fp.writelines(lines)
