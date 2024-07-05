import datetime
import os
import asyncio
from playwright.async_api import async_playwright, Browser
from bs4 import BeautifulSoup


async def translate(browser: Browser, url: str) -> None:

    page = await browser.new_page(viewport={"width": 1280, "height": 720})

    await page.goto(url)
    await asyncio.sleep(2)

    text = ""

    soup = BeautifulSoup(await page.content(), "html.parser")
    spans = soup.find_all("span", class_="ryNqvb")
    for span in spans:
        text = text + " " + span.get_text()
    text = text.strip()
    text = text + "\n"

    return text


async def main() -> None:
    with open("../cleaning/merged.txt", "r", encoding="utf-8") as f:
        orig_lines = f.readlines()

    file_path = "kha_to_en.txt"
    if os.path.exists(file_path):
        os.remove(file_path)

    async with async_playwright() as playwright:
        for line in orig_lines:
            browser = await playwright.firefox.launch(headless=True)
            url = f"https://translate.google.com/?sl=kha&tl=en&text={line}&op=translate"
            txt = await translate(
                browser=browser,
                url=url,
            )
            with open("kha_to_en.txt", "a", encoding="utf-8") as f:
                f.write(txt)
            await browser.close()


if __name__ == "__main__":
    start = datetime.datetime.now()
    asyncio.run(main())
    end = datetime.datetime.now()
    print(end - start)
