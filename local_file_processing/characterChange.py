import re 

def clean_mhg_text(text, replacements):
    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text)
    return text

replacements = {
    r'â':'a',
    r'ë':'e',
    r'ė':'e',
    r'ê':'e',
    r'î':'i',
    r'û':'u',
    r'ô':'o',
    r'-':'',
    r'æ':'ä',
    r'œ':'ö',

}


with open('./wordcount/aggregate_wordcount.txt', 'r') as f:
    text = f.read()
cleaned_text = clean_mhg_text(text, replacements)
with open('./wordcount/aggregate_cleanedwordcount.txt', 'w') as f:
     f.write(cleaned_text)