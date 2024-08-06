with open("translated_parallel_corpus_2.tsv", "w", encoding="utf-8") as fp:
    fp.write("en\t\t\t\t\tkha\n")


for i in range(1, 2608 + 1):
    with open(f"chunks/part{i}.txt", "r", encoding="utf-8") as fp:
        en_lines = fp.readlines()

    with open(f"translated/part{i}_en_to_kha.txt", "r", encoding="utf-8") as fp:
        kha_lines = fp.readlines()

    assert len(kha_lines) <= len(en_lines)

    with open("translated_parallel_corpus_2.tsv", "a", encoding="utf-8") as fp:
        for i in range(0, len(kha_lines)):
            fp.write(f"{en_lines[i].strip()}\t\t\t\t\t{kha_lines[i].strip()}\n")
