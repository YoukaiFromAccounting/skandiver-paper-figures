#!usr/bin/python
#Simple script to merge individual fastas into large multifasta file
import os
import sys
from tqdm import tqdm

def combine_fna_files(directory_path, output_file):
    files_to_combine = [filename for filename in os.listdir(directory_path) if filename.endswith(".fna")]
    progress = tqdm(total=len(files_to_combine), unit="file", desc="Combining Files")

    #Open the output file in append mode to avoid overwriting previous content
    with open(output_file, 'a') as combined_file:
        #Iterate over files, append content to output file
        for filename in files_to_combine:
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r') as current_file:
                content = current_file.read()
                combined_file.write(content)
                progress.update(1)

    progress.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 merge_fna.py input_directory output_file")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_file = sys.argv[2]

    combine_fna_files(input_directory, output_file)
    print("Files have been combined from", input_directory,"to", output_file)
