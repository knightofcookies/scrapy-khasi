import datetime
import os
import asyncio
from deep_translator import GoogleTranslator


async def main() -> None:
    with open("../cleaning/merged.txt", "r", encoding="utf-8") as f:
        orig_lines = f.readlines()

    file_path = "kha_to_en.txt"
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
