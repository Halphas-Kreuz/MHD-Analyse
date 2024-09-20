import os 

with open("./result/MHD_NoDuplicate.txt") as MHD_NoDuplicate:
    MHD_NoDuplicate_list = MHD_NoDuplicate.readlines()

with open("./result/indexlist01.txt") as index:
   indexlist = index.readlines()

summary = []
for i in range(len(MHD_NoDuplicate_list)):
    if i < len(indexlist):
        value = str(MHD_NoDuplicate_list[i]).strip().split(":")[0] + ":" + indexlist[i]
    else:
        value = str(MHD_NoDuplicate_list[i]).strip().split(":")[0] + ":" +  str("0")
    
    summary.append(str(value))

initial_dict = {}
for i in summary:
    parts = i.split(":")
    word = parts[0].strip()  
    readable = int(parts[1].strip())  
    initial_dict[word] = readable

# print(analyzedict)

file_path = ("./wordcount")
scores = {}
for filename in os.listdir(file_path):
    if filename.endswith('.txt'):  # 假设文件扩展名为 .txt
        file_full_path = os.path.join(file_path, filename)
        
        # 初始化总分数
        total_score = 0
        
        # 打开并读取文件
        with open(file_full_path, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                word = parts[0].strip()
                frequency = int(parts[1].strip())
                
                if word in initial_dict:
                    score = initial_dict[word] * frequency
                    total_score += score
        
        # print(f"{filename}: RESULT =  {total_score}")
        scores[filename] = total_score

with open("./result/Scorecount.txt") as Scorecount:
    Scorecount_list = Scorecount.readlines()

TextWordCount = {}
for i in Scorecount_list:
    parts = i.strip().split(":")
    textname = parts[0].strip()
    ScoreForEachText = int(parts[1].strip())
    TextWordCount[textname] = ScoreForEachText

def calculate_ratios(dict1, dict2):
    ratios = {}
    for filename, value1 in dict1.items():
        if filename in dict2:
            value2 = dict2[filename]
            ratio = value1 / value2
            ratios[filename] = ratio
    
    sorted_ratios = sorted(ratios.items(), key=lambda x: x[1], reverse=True)
    
    # 输出并保存结果
    for filename, ratio in sorted_ratios:
        print(f"{filename}: ratio is {ratio:.5f}")

    return sorted_ratios


calculate_ratios(scores, TextWordCount)

# print(scores)
# print(TextWordCount)