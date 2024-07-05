def count_characters(f_path):
    try:
        with open(f_path, "r", encoding="utf-8") as file:
            content = file.read()
            num_characters = len(content)
            return num_characters
    except FileNotFoundError:
        return "File not found. Please provide a valid file path."


file_path = "../cleaning/merged.txt"
result = count_characters(file_path)
if isinstance(result, int):
    print(f"Number of characters in the file: {result}")
else:
    print(result) # 141M characters => 2.35 lakh INR for Cloud Translate Basic
