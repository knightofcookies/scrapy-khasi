import winsound
import datetime
import os
import asyncio
import sys
from deep_translator import GoogleTranslator

# Add {"khasi": "kha"} to the Google Translate dict in constants.py in deep_translator


async def main() -> None:
    if len(sys.argv) < 2:
        return

    with open(f"chunks_for_translation/{sys.argv[1]}.txt", "r", encoding="utf-8") as f:
        orig_lines = f.readlines()

    index = 0
    file_path = f"translated/{sys.argv[1]}_kha_to_en.txt"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            index = len(f.readlines())

    if not os.path.exists("translated/"):
        os.mkdir("translated")

    kha_to_en_translator = GoogleTranslator(source="kha", target="en")

    while index < len(orig_lines):
        line = orig_lines[index]
        txt = kha_to_en_translator.translate(line)
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(txt + "\n")
        index += 1


if __name__ == "__main__":
    start = datetime.datetime.now()
    asyncio.run(main())
    end = datetime.datetime.now()
    print(end - start)
    winsound.Beep(2500, 1000)
