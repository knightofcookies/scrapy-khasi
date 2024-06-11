def split_csv(input_file, output_file1, output_file2):
    with open(input_file, "r") as infile:
        lines = infile.readlines()
        midpoint = len(lines) // 2

        with open(output_file1, "w") as outfile1:
            outfile1.writelines(lines[:midpoint])

        with open(output_file2, "w") as outfile2:
            outfile2.writelines(lines[midpoint:])


# Example usage:
split_csv(
    "../../raw_datasets/mawphor_2.csv",
    "../../raw_datasets/mawphor_part_C.csv",
    "../../raw_datasets/mawphor_part_D.csv",
)
