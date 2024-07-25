# import nltk
# nltk.download('punkt')

from typing import List
from nltk import sent_tokenize
from datasets import load_dataset

dataset = load_dataset("wikipedia", "20220301.simple", trust_remote_code=True)

dataset_list = dataset["train"].to_list()

sentences: List[str] = []
sentences_cleaned: List[str] = []

for item in dataset_list:
    text = item["text"]
    sentences.extend(sent_tokenize(text=text, language="english"))

for s in sentences:
    s_list = s.split("\n")
    nsl = []
    for sl in s_list:
        if sl.count('|') == 0:
            nsl.append(sl.strip() + '\n')
    sentences_cleaned.extend(nsl)

with open("simple_wikipedia_sentences.txt", "w", encoding="utf-8") as f:
    f.writelines(set(sentences_cleaned))
