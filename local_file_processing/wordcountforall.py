import os
from collections import Counter

def wordcount(input_file_path):
    # Read the content of the file
    with open(input_file_path) as f:
        content = f.read()
    
    # Split content into words
    wordlist = content.split()
    
    # Use Counter to count frequencies
    wordfreq = Counter(wordlist)
    
    return wordfreq

def process_folder(input_dir, output_file_path):
    # Initialize an aggregate Counter
    aggregate_word_count = Counter()

    # Process each .txt file in the directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            input_file_path = os.path.join(input_dir, filename)
            # Update aggregate word count with current file's word count
            aggregate_word_count.update(wordcount(input_file_path))
    
    # Sort the aggregate word count by frequency in descending order
    sorted_word_count = dict(sorted(aggregate_word_count.items(), key=lambda item: item[1], reverse=True))
    
    # Write the sorted aggregate word count to the output file
    with open(output_file_path, "w") as f:
        for key, value in sorted_word_count.items():
            f.write('%s:%s\n' % (key, value))
    
    print(f"Aggregated data saved into {output_file_path}")

# Directory paths
input_dir = './output'
output_file_path = './wordcount/aggregate_wordcount.txt'
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

# Process the folder and write aggregated word counts to a file
process_folder(input_dir, output_file_path)
