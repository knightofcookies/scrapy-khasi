def count_words(string):
    string1 = string.strip()
    count = 1
    for char in string1:
        if char == " ":
            count += 1
    return count


with open("combined_corpus.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    if count_words(line) <= 5:
        filename = f"length_wise_corpus/{count_words(line)}_word_corpus.txt"
    else:
        filename = "length_wise_corpus/longer_sentence_corpus.txt"
    with open(filename, "a") as f:
        f.write(line)
