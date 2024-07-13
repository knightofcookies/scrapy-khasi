def check_file_length_equalities(dir1, dir2, start, end):
    count = 0
    for i in range(start, end + 1):
        with open(f"{dir1}/part{i}.txt", "r", encoding="utf-8") as fp:
            len1 = len(fp.readlines())
        with open(f"{dir2}/part{i}_kha_to_en.txt", "r", encoding="utf-8") as fp:
            len2 = len(fp.readlines())
        if len1 != len2:
            print(f"{dir1}/part{i}.txt")
        else:
            count += 1
    print(f"{count} files okay")


check_file_length_equalities(
    "chunks_for_translation", "translated", 1, 634
)
check_file_length_equalities(
    "chunks_for_translation_2", "translated_2", 1, 131
)
