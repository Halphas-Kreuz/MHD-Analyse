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

sorted_list = SortList("./wordcount/aggregate_wordcount.txt")

def save_results_to_file(results, filename):
    with open("./test.txt", 'w') as file:
        for i in results:
            file.write(i + '\n')