import datetime

start = datetime.datetime.now()

with open("translated_parallel_corpus.tsv", "r", encoding="utf-8") as fp:
    lines = fp.readlines()

lines.pop(0)
total = len(lines)
count = 0
lines_with_colon = []
new_lines = ["en\t\t\t\t\tkha\n"]
for line in lines:
    count += 1
    kha_sentence = line.split("\t\t\t\t\t")[1]
    if len(kha_sentence) > 4999:
        continue
    elif len(line) < 30:
        if line.count(":", 0, len(line)) > 0:
            lines_with_colon.append(line)
    elif line.count(":", 0, 30) > 0:
        lines_with_colon.append(line)
    else:
        new_lines.append(line)

    if count % 10000 == 0:
        print(f"{count}/{total} sentences cleaned...")

with open("cleaned_parallel_corpus.tsv", "w", encoding="utf-8") as fp:
    fp.writelines(new_lines)

with open("translated_parallel_corpus_with_colon.tsv", "w", encoding="utf-8") as fp:
    fp.writelines(lines_with_colon)

end = datetime.datetime.now()

print(end - start)

# with_colon.csv was manually edited to remove some exceptions
