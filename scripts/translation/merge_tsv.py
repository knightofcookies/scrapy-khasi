with open("cleaned_colon.tsv", "r", encoding="utf-8") as fp:
    lines = fp.readlines()

with open("cleaned_parallel_corpus.tsv", "a", encoding="utf-8") as fp:
    fp.writelines(lines)
