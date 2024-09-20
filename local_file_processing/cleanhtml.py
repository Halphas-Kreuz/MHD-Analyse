import os
import re
from bs4 import BeautifulSoup

def clean_html_and_save(input_file_path, output_dir):

    with open(input_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, 'lxml')

    lemma_trs = []
    for tr in soup.find_all('tr'):
        ths = tr.find_all('th', string='Lemma')
        if ths:
            lemma_trs.append(tr)

    results = []
    for tr in lemma_trs:
        tds = tr.find_all('td')
        td_texts = [td.get_text() for td in tds]


        cleaned_texts = []
        for text in td_texts:
            cleaned_text = re.sub(r'[()\[\]*.,;:!|]', '', text)  
            cleaned_texts.append(cleaned_text)
        
        result = ' '.join(cleaned_texts)
        results.append(result)

    input_file_name = os.path.basename(input_file_path)
    output_file_name = os.path.splitext(input_file_name)[0] + ".txt"
    output_file_path = os.path.join(output_dir, output_file_name)


    with open(output_file_path, 'w', encoding='utf-8') as file:
        for result in results:
            file.write(result + '\n')

    print(f"data saved into {output_file_path}")

def process_folder(input_dir, output_dir):

    for filename in os.listdir(input_dir):
        if filename.endswith('.htm'):
            input_file_path = os.path.join(input_dir, filename)
            clean_html_and_save(input_file_path, output_dir)

# 示例使用
input_dir = './'
output_dir = './output'
os.makedirs(output_dir, exist_ok=True)

process_folder(input_dir, output_dir)