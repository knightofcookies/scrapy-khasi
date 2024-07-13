with open("translated_parallel_corpus.tsv", "w", encoding="utf-8") as fp:
    fp.write("en\t\t\t\t\tkha\n")


for i in range(1, 635):
    with open(f"chunks_for_translation/part{i}.txt", "r", encoding="utf-8") as fp:
        kha_lines = fp.readlines()

    with open(f"translated/part{i}_kha_to_en.txt", "r", encoding="utf-8") as fp:
        en_lines = fp.readlines()

    assert len(en_lines) == len(kha_lines)

    with open("translated_parallel_corpus.tsv", "a", encoding="utf-8") as fp:
        for i in range(0, len(en_lines)):
            fp.write(f"{en_lines[i].strip()}\t\t\t\t\t{kha_lines[i].strip()}\n")

for i in range(1, 132):
    with open(f"chunks_for_translation_2/part{i}.txt", "r", encoding="utf-8") as fp:
        kha_lines = fp.readlines()

    with open(f"translated_2/part{i}_kha_to_en.txt", "r", encoding="utf-8") as fp:
        en_lines = fp.readlines()

    assert len(en_lines) == len(kha_lines)

    with open("translated_parallel_corpus.tsv", "a", encoding="utf-8") as fp:
        for i in range(0, len(en_lines)):
            fp.write(f"{en_lines[i].strip()}\t\t\t\t\t{kha_lines[i].strip()}\n")
