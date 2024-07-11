import winsound
import datetime
import os
import asyncio
import pickle
import concurrent.futures
from typing import List
from deep_translator import GoogleTranslator

# Add {"khasi": "kha"} to the Google Translate dict in constants.py in deep_translator

THREAD_LIMIT = 25

START = 1  # Delete pickle_dump if you change this
END = 100  # Delete pickle_dump if you change this

PICKLE_DUMP_PATH = "pickle_dump"


def translate_chunk(chunk: str, complete_index: int) -> None:

    source = "kha"
    target = "en"

    with open(f"chunks_for_translation/{chunk}.txt", "r", encoding="utf-8") as f:
        orig_lines = f.readlines()

    index = 0
    file_path = f"translated/{chunk}_{source}_to_{target}.txt"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            index = len(f.readlines())
    if index < 0:
        index = 0

    if not os.path.exists("translated/"):
        os.mkdir("translated")

    translator = GoogleTranslator(source=source, target=target)

    while index < len(orig_lines):
        line = orig_lines[index]
        txt = translator.translate(line)
        if txt is not None:
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(txt + "\n")
        index += 1

    with open(PICKLE_DUMP_PATH, "rb+") as fp:
        complete = pickle.load(fp)
        complete[complete_index] = True
        pickle.dump(complete, fp)


async def main() -> None:
    if not os.path.exists(PICKLE_DUMP_PATH):
        complete: List[bool] = [False * (END - START + 1)]
        with open(PICKLE_DUMP_PATH, "wb") as fp:
            pickle.dump(complete, fp)

    with open(PICKLE_DUMP_PATH, "rb") as fp:
        complete = pickle.load(fp)

    pool = concurrent.futures.ThreadPoolExecutor(max_workers=THREAD_LIMIT)

    chunk_index = 0
    while chunk_index < (END - START + 1):
        if not complete[chunk_index]:
            pool.submit(translate_chunk, f"part{START+chunk_index}.txt", chunk_index)
        chunk_index += 1

    pool.shutdown(wait=True)


if __name__ == "__main__":
    start = datetime.datetime.now()
    asyncio.run(main())
    end = datetime.datetime.now()
    print(end - start)
    winsound.Beep(2500, 1000)
