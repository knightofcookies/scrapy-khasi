import os

with open("unified.tsv", "r", encoding="utf-8") as fp:
    lines = fp.readlines()

if os.path.exists("custom.tsv"):
    os.remove("custom.tsv")

# if os.path.exists("kha_custom.txt"):
#     os.remove("kha_custom.txt")

with open("custom.tsv", "a", encoding="utf-8") as fp:
    fp.writelines(lines[200001:500001])

# for i in range(200001, 500001):
#     line = lines[i]
#     en_line, kha_line = line.split("\t\t\t\t\t")
    # with open("en_custom.txt", "a", encoding="utf-8") as fp:
    #     fp.write(en_line.strip() + "\n")
    #     with open("kha_custom.txt", "a", encoding="utf-8") as fp2:
    #         fp2.write(kha_line.strip() + "\n")
