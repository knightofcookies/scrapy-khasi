import pandas as pd

with open("en.txt", "r", encoding="utf-8") as fp:
    en_lines = fp.readlines()

with open("kha.txt", "r", encoding="utf-8") as fp:
    kha_lines = fp.readlines()
    
assert len(en_lines) == len(kha_lines)

with open("translated_parallel_corpus.csv", "w", encoding="utf-8") as fp:
    fp.write("en,kha\n")
    for i in range(0, len(en_lines)):
        fp.write(f"{en_lines[i].strip},{kha_lines[i].strip}")
