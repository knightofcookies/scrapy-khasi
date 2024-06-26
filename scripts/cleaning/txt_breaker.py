def split_text_file_by_lines(filename, num_lines):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Calculate the approximate number of lines per part
    lines_per_part = len(lines) // num_lines

    # Split the lines into chunks
    chunks = [lines[i:i + lines_per_part] for i in range(0, len(lines), lines_per_part)]

    # Save each chunk to separate files (e.g., part1.txt, part2.txt, ..., part25.txt)
    for i, chunk in enumerate(chunks, start=1):
        with open(f'chunks/part{i}.txt', 'w') as output_file:
            output_file.writelines(chunk)

# Usage
split_text_file_by_lines('../../datasets/dot_split/combined_corpus.txt', 1000)
