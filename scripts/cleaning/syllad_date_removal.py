import pandas as pd
import re

# Read the CSV file (replace 'your_file.csv' with your actual file path)
data = pd.read_csv('../../khasi_news/data/syllad/syllad_2024-06-07T09-48-05+00-00.csv')

# Extract the relevant text after the date portion
data['content'] = data['content'].apply(lambda x: re.sub(r'^\w+ \d{1,2}, \d{4} ', '', x))

# Save the modified DataFrame to a new CSV file
data.to_csv('new_file.csv', index=False)
