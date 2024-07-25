from datasets import load_dataset

dataset = load_dataset("wikipedia", "20220301.simple", trust_remote_code=True)

# print(dataset.column_names)

dataset_list = dataset["train"].to_list()

# print(dataset_list[0])

lines = []

for item in dataset_list:
    id_ = item["id"]
    url = item["url"]
    title = item["title"]
    text = item["text"]

    new_line = f"""<20220301_page>\n
<20220301_id> {id_} </20220301_id>\n
<20220301_url> {url} </20220301_url>\n
<20220301_title> {title} </20220301_title>\n
<20220301_text>\n{text}\n</20220301_text>\n
</20220301_page>"""
    new_line = new_line.strip()

    lines.append(new_line + "\n")

with open("simple_english_wikipedia_20220301.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
