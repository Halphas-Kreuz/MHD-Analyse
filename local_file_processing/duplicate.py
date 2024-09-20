# %%
import re 
from bs4 import BeautifulSoup
import requests
import lxml
import time 

# %%
words = []
def SortList(input_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    lines = content.splitlines()
    for line in lines:
        words.append(line.split(' '))
    

    word_list = [(item[0].split(':')[0], int(item[0].split(':')[1])) for item in words]
    sorted_list = sorted(word_list, key=lambda x: (len(x[0]), x[0],x[1]))
    return sorted_list

sorted_list = SortList("./wordcount/aggregate_Cleaned.txt")

# %%
def find_containing_words(word_list):
    containing_words = set()
    
    words_only = [word for word, _ in word_list if len(word) > 3]  
    
    for word, _ in word_list:
        if len(word) > 4 and any(w in word and w != word for w in words_only if w != word):
            containing_words.add(word)
    
    return list(containing_words)

def not_contain_other_words(word_list):
    containing_words = find_containing_words(word_list)
    short_words = [word for word, _ in word_list if (len(word) <= 3 and len(word) >= 2) ]
    result = [word for word, _ in word_list if word not in containing_words]
    final_result = [(word, freq) for word, freq in word_list if word in short_words or word not in containing_words]
    return final_result

def save_results_to_file(results, filename):
    with open(filename, 'w') as file:
        for word, freq in results:
            file.write(f"{word}: {freq}\n")
            
cleaned = not_contain_other_words(sorted_list)
save_results_to_file(cleaned,"./noduplicate_words.txt")


