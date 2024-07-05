import csv
import random

def shuffle_csv(input_file, output_file):
    try:
        with open(input_file, 'r', newline='', errors='ignore') as infile:
            reader = csv.reader(infile)
            rows = list(reader)
            random.shuffle(rows)

        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(rows)

        print(f"CSV file shuffled. Shuffled content saved to {output_file}")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

# Example usage:
input_file_path = 'parallel_corpus/pc.csv'  # Replace with your input CSV file path
output_file_path = 'parallel_corpus/shuffled_output.csv'  # Replace with your desired output CSV file path
shuffle_csv(input_file_path, output_file_path)
