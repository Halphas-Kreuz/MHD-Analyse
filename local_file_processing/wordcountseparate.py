import os 

def wordcount(input_file_path,output_dir):
    #with open
    with open(input_file_path) as f:
        content = f.read()
    
    wordlist = content.split()

    wordfreq = [wordlist.count(p) for p in wordlist]
    result =  dict(list(zip(wordlist, wordfreq)))
    sorted_result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))  # Step 3: Sort by frequency  
        

    input_file_name = os.path.basename(input_file_path)
    output_file_name = os.path.splitext(input_file_name)[0] + ".txt"
    output_file_path = os.path.join(output_dir, output_file_name)

    with open (output_file_path, "w") as f:
        for key, value in sorted_result.items():
            f.write('%s:%s\n' % (key, value))
    
    print(f"data saved into {output_file_path}")

def process_folder(input_dir, output_dir):

    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            input_file_path = os.path.join(input_dir, filename)
            wordcount(input_file_path, output_dir)

input_dir = './output'
output_dir = './wordcount'
os.makedirs(output_dir, exist_ok=True)

process_folder(input_dir, output_dir)