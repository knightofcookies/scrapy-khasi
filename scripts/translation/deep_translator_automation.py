import datetime
import os
import asyncio
import sys
from deep_translator import GoogleTranslator

# Add {"khasi": "kha"} to the Google Translate dict in constants.py in deep_translator


async def main() -> None:
    if len(sys.argv) < 2:
        return

    with open(f"to_translate{sys.argv[1]}", "r", encoding="utf-8") as f:
        orig_lines = f.readlines()

    file_path = f"translated/{sys.argv[1]}_kha_to_en.txt"
    if os.path.exists(file_path):
        os.remove(file_path)

    kha_to_en_translator = GoogleTranslator(source="en", target="kha")
    for line in orig_lines:
        txt = kha_to_en_translator.translate(line)
        with open("kha_to_en.txt", "a", encoding="utf-8") as f:
            f.write(txt + "\n")


if __name__ == "__main__":
    start = datetime.datetime.now()
    asyncio.run(main())
    end = datetime.datetime.now()
    print(end - start)