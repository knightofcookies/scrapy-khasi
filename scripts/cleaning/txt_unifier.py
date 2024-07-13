from typing import List
import os


def join_text_files_by_lines(dir_list: List[str], new_file_name: str):
    lines = []
    for dir_ in dir_list:
        for filename in os.listdir(dir_):
            with open(os.path.join(dir_, filename), "r", encoding="utf-8") as file:
                lines += file.readlines()

    with open(new_file_name, "w", encoding="utf-8") as f:
        f.writelines(lines)

dirs_en = ["../translation/translated", "../translation/translated_2"]
dirs_kha = ["../translation/chunks_for_translation", "../translation/chunks_for_translation_2"]

join_text_files_by_lines(dirs_en, "en.txt")
join_text_files_by_lines(dirs_kha, "kha.txt")
