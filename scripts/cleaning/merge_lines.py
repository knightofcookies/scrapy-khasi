import os

DIRECTORY = "chunks"

for name in os.listdir(DIRECTORY):
    with open(os.path.join(DIRECTORY, name), "r", encoding="utf-8") as file:
        lines = file.readlines()

    merged_lines = []
    for line in lines:
        if line[0].isdigit():
            if merged_lines:
                merged_lines[-1] = merged_lines[-1].strip() + line
        else:
            merged_lines.append(line)

    with open(f"merged_chunks/{name}", "w", encoding="utf-8") as file:
        file.writelines(merged_lines)


def merge_lines_ending_with_abbreviation(lines_):
    flag = True
    while flag:
        new_lines_ = []
        i = 0
        count = 0
        while i < len(lines_):
            line_: str = lines_[i].strip()
            if any(line_.endswith(abbreviation) for abbreviation in abbreviations):
                if i + 1 < len(lines_):
                    count += 1
                    next_line = lines_[i + 1].strip()
                    new_lines_.append(line_ + next_line)
                    i += 2
                else:
                    new_lines_.append(line_)
                    i += 1
            else:
                new_lines_.append(line_)
                i += 1
        if count == 0:
            return new_lines_
        else:
            lines_ = new_lines_


for name in os.listdir("merged_chunks"):
    with open(os.path.join("merged_chunks", name), "r", encoding="utf-8") as file:
        lines = file.readlines()

    abbreviations = [
        "Dr.",
        "Mr.",
        "Mrs.",
        "Ms.",
        "etc.",
        "Rev.",
        "Adv.",
        "Ex.",
        "Eng.",
        "Sri.",
        "Shri.",
        "Addl.",
        "Dy.",
        "Case.",
        "Most.",
        "Rq.",
        "Admn.",
        "Misc.",
        "Retd.",
        "No.",
        "St.",
        "Tbn.",
        "Prof.",
        "Asst.",
        "Hony.",
        "Hon.",
        "Fr.",
        "sq."
    ] + [f"{chr(i)}." for i in range(65, 91)]

    merged_lines = merge_lines_ending_with_abbreviation(lines)

    with open(os.path.join("merged_chunks", name), "w", encoding="utf-8") as file:
        for line in merged_lines:
            file.write("%s\n" % line)