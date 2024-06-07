import re

regex = r"^\"\s(\bJanuary|February|March|April|May|June|July|August|September|October|November|December)(\b\s+\d{1,2},\s+\d{4})"

new_lines = []
# Read the CSV file (replace 'your_file.csv' with your actual file path)
with open(
    "../../khasi_news/data/syllad/syllad_2024-06-07T09-48-05+00-00.csv",
    "r",
    encoding="utf-8",
) as f:
    lines = f.readlines()

for line in lines:
    new_lines.append(re.sub(regex, "\"", line).strip()+"\n")

with open("syllad_without_dates.csv", "w", encoding="utf-8") as f:
    f.writelines(new_lines)
