with open("translated_parallel_corpus_with_colon.tsv", "r", encoding="utf-8") as fp:
    lines = fp.readlines()

new_lines = []
to_clean = []
for line in lines:
    en_line, kha_line = line.split("\t\t\t\t\t", 1)
    if (
        kha_line.lower().startswith("shillong")
        or kha_line.lower().startswith("nongstoiñ")
        or kha_line.lower().startswith("jowai")
        or kha_line.lower().startswith("nongpoh")
        or kha_line.lower().startswith("tura")
        or kha_line.lower().startswith("mawkyrwat")
        or kha_line.lower().startswith("amlarem")
        or kha_line.lower().startswith("batei")
        or kha_line.lower().startswith("new delhi")
        or kha_line.lower().startswith("mawsynram")
        or kha_line.lower().startswith("guwahati")
        or kha_line.lower().startswith("khliehriat")
        or kha_line.startswith(":")
    ):
        if (
        en_line.lower().startswith("shillong")
        or en_line.lower().startswith("nongstoiñ")
        or en_line.lower().startswith("jowai")
        or en_line.lower().startswith("nongpoh")
        or en_line.lower().startswith("tura")
        or en_line.lower().startswith("mawkyrwat")
        or en_line.lower().startswith("amlarem")
        or en_line.lower().startswith("batei")
        or en_line.lower().startswith("new delhi")
        or en_line.lower().startswith("mawsynram")
        or en_line.lower().startswith("guwahati")
        or en_line.lower().startswith("khliehriat")
        or en_line.startswith(":")
        ):
            split = en_line.split(":", 1)
            if len(split) > 1:
                en_line = split[1]
        split = kha_line.split(":", 1)
        if len(split) > 1:
            kha_line = split[1]
        new_lines.append(en_line.strip() + "\t\t\t\t\t" + kha_line.strip() + "\n")
    else:
        to_clean.append(line)

with open("cleaned_colon.tsv", "w", encoding="utf-8") as fp:
    fp.writelines(new_lines)

with open("to_clean.tsv", "w", encoding="utf-8") as fp:
    fp.writelines(to_clean)
