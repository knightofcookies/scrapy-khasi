import os

output_file = "temp_corpus.txt"

if os.path.exists(output_file):
    os.remove(output_file)

for i in range(1, 2001):
    with open(f"translated/part{i}_en_to_kha.txt", "r", encoding="utf-8") as fp:
        kha_lines = fp.readlines()

    with open(output_file, "a", encoding="utf-8") as fp:
        fp.writelines(kha_lines)
