import os
import pandas as pd
import re

# Remember to replace : with \n
# Take care of unpaired quotes

directory = "../../datasets/raw_datasets"
sentence_set = []
regex = r"(http|https|ftp):\/\/(\S*)"

for name in os.listdir(directory):
    df = pd.read_csv(os.path.join(directory, name))
    content = df["content"]
    for text in content:
        if isinstance(text, str):
            text = re.sub(regex, "", text, re.IGNORECASE)
            text = re.sub(regex, "", text, re.IGNORECASE) # use twice, just works
            text = re.sub(regex, "", text, re.IGNORECASE) # use thrice, works even better
            text = text.replace("https.stems", "") # not removed by regex
            text = text.replace("https//", "") # not removed by regex
            # text = text.replace(":", ".") # tends to mess up time like 2:00 pm
            text = text.replace("|", ".")
            text = text.replace('”', '"')
            sentences = text.split('.')
            for sentence in sentences:
                # if sentence.count('"') == 1:
                #     sentence = sentence.replace('"', " ")
                sentence = sentence.strip()
                if sentence != "":
                    sentence += ".\n"
                    sentence_set.append(sentence)

with open("../../datasets/dot_split/combined_corpus.txt", "w") as f:
    f.writelines(sentence_set)
