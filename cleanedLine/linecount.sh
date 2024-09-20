#!/bin/bash

# Replace "/path/to/your/folder" with the actual path to your folder
folder="./"

# Initialize variables to store the total line and word counts
total_lines=0
total_words=0
num_files=0

# Iterate through each file in the folder
for file in "$folder"/*; do
  # Check if the file is a regular file (not a directory or other type)
  if [[ -f "$file" ]]; then
    # Use wc -l and wc -w to count lines and words
    lines=$(wc -l < "$file")
    words=$(wc -w < "$file")

    # Accumulate the totals
    total_lines=$((total_lines + lines))
    total_words=$((total_words + words))
    num_files=$((num_files + 1))

    # Print the individual file results
    echo "$file: $lines lines, $words words"
  fi
done

# Calculate the averages
if [[ $num_files -gt 0 ]]; then
  avg_lines=$((total_lines / num_files))
  avg_words=$((total_words / num_files))
  echo "Average lines: $avg_lines"
  echo "Average words: $avg_words"
else
  echo "No files found."
fi