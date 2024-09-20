import re 
from bs4 import BeautifulSoup
import requests
import lxml

words = []
def cleaningnumber(input_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    lines = content.splitlines()
    for line in lines:
        words.append(line.split(':')[0])
    
    return words

input_file_path = './wordcount/split_wordcount/xag.txt'
cleaningnumber(input_file_path)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
cookies = {

    'lHlWnGsRs':'6LvnzKExJN54jRU4rNyZg%2ByN16A8BU41Y2GyFxwM1v8OpqiNFFt1xJ22bC%2FuNuZ2UjSfS8%2BLt77GDRtKPvHGTaBoI29I8aThv0eDqcjLvqf0%2FOVsZ9OaQ%2FpA98tZtEpiDb9iIpegmnUGo%2Fbgw%2FU2rZqpQ9uzfrnh%2FEABoMLzop6ckeNWri%2FgwsEyXW2DXXZsMP3SxJWEKy7S3sPOydw42x%2FGMvu9I0qJ3u5bFqddj43j1rUklJYTutBrVFn%2B0UU0u%2BJ%2BdPSLDJAjuBmtEc0RSOnXSumtB3l9o0j%2BbKUaYaNMc8vTpTzSG2j8h6qF4gShhY0dnB2P9byT61i06cd8J3u4tJwl2nRbq4q%2Fr8rTrRnFTIpm%2B2VVVTcRlJqsXppe%2BqhJsFLduOpu1M3m1vOHlLdRzCKxM%2F8ubIWwnKN1Fb5icf1CNKsMOFV7aQhy8TtWEDV2AjuShTpT3FN2HFjDj26r9Ph5BUbm3PZkJ37ro4x7lcYrfKDejyo78Gl4cMX8PwURPik9YK%2BEqVpqfID1vynLXLhFBf2NYUdvNgyYFouZ1%2B3ndtpNZ7llF1H8JU%2FTGeu%2FBalzMIHtqvF%2Bafjj6IiI8RDOMMUexR30QUO50yId5f%2FWZvHosn7zoJVM%2FWbOLr9OIsl0Gw8rNaxYfxQZNn47eOxx7MbE690wcAHLaHmQWnNTHrGqGlwveAsAvk2F5FiHr3rzkzjVlNf0Pfvuva5WjLcel2BUEtxCuDzh6JKQG8Eyuy4OZQtGfpQ%2B8x%2B%2BilcGwVge8uH7JjPjsJeJGTYtt1PDqYuvTgyf0e7qqQceMZqNpETGDExP4pUoa1cHbqGPJekBYKc9LuAkSmmMhNqzKT247SbiPDgSKMlF5%2BMRbLYomLP4DQt46YgV%2BLCy%2Fy0UXTbzPZv44Ba7difF2aWjP6wWTVskSnH9HiB6HeMQ1LHPt4KFTgNqhO0FARq8k4tQbofUys0l1suXkVI%2BfkplnlqjDiffHD%2F%2FDFDXZx3lNxF%2BNRW3hMap4zYPbnqwCXQjZJ5h6RY4qas4JGmyjpleeht9Pvo0xZfCvEnu0XehOAxrVEinr3kDi6WKTtbn35RHT%2FdKu1c7cz958uEEJTlONiqXDp9K03SyIPK9TYfrhXjLLIzE75Wq6xwUUAF8kbUxvwaWKJS6GttMiBeBI%2B6YHnj%2BOzAnoCIcZN8xp76Oy%2Fkn32sbbEVBB%2B%2BVqxgNGixeNiVzn1Pb4ltXrcGlR8MhaHFobEk3GqdGsm0dG7sRk%2Fx3ihcMcH0C8c1qnJNzc9Z4sgSJDiyYnDkWTNlfx4G5kcFjgrUplF%2FZwOuNwAFOX9c8iKM3jQ1xJ1eyhxiTMgQMp0BYZGnkmwWtqgVy9KL5LAnXjhXL%2FDvTtBmrn1tvIaZbjM%2BUk0B55%2FhOHPkj2tepu9wZF4xzxhOr3ZX%2FxIroxi5ft%2F0gQA5O2PdrcLN%2BLKYoOVgjSiqcghm3v7BDTipSPUUjDqt%2F8tBIrhtvh7rOfZLD8HIVllWDop6VB7b9ibBIZp2LWceYlYv5qddHbziwzSqCbvFEzDxUlqRL%2Biu%2FKOiHdg6QCKXCoULux18EmzXsIwGU%2F%2BaNQgeQMwTpKIC56N8vxqK7eov1DG0tgIKS%2FD02Kshw1mck0Z9aQywqy%2FgRGKTai%2B0zcywz4eVYPJr9RPT7JBRLvgxDr0gEGbxLLlf22J3eejwF24JpFWn5rMwjdSKtYvDMAbwlpPiIfLoTm9hAEZv8PNuetJry7iS4zgDIWDxoqPBBVDonBRCCqCnta7e5TgVm55TqSph6wwodEgiheshSlOybOkcyK4RNCUtE1bNVsAzjuz0k2RFI0vmfabMgp12jS%2FS9hyxQqgnx5MKa7e2GtFv3PRnz77TAaizOHe8U%2FxJbIqSq6QH4%2F0oRhA3va%2Bu6Plky81O36J9ap70sxqvT5FB6miz%2BxnmPIj%2B8XvxIo3aZZdC0ICn2Dqp0DWAB1ys4SJMxepeUrUirpBRPG8VxlHsBOQx%2F84yj1oOGzyxsAsGiHXZq3KEeufkjw7FAMBJDvIJmTLozxK3FmqbqKElStu1Yqp%2BXXtdLJGBqkyrvAIOdg0PNCEYmcVGWj01q4vKa0fWGavlAdRbc7UrvAIO3jejJiYAHH0Zc7SarlgkMV1%2FuWoxBnTgm%2B%2BeHmV%2B6kcAPSic82ss0eR8uRFu%2FVO0CTnLBFua%2FrRAVUpAwVTrTQcHGcOTU%2BVjhBYFr9BvISiPvOkmgluubHqxu6cg8ptzQZIm7%2F5mbIDMgQ%2BsDg9WYEkuDXY4h8JiNIZPbkoT7OUdvdJGcxhDCZtuEGpOVH1Rs%2BSWFYzY53i%2BISr1ddLXQqLRkCAVVzqXS%2Fq46ivwpzuH9kDXKbNj53WsD%2FAgkBwuzMIuLT85h7xbcARXoXAXXt1NV7BY7m0A9R0xwst6d%2FIqEOkkYM7LBYbKiR%2BXaySDBa2yTm57Lc7fDboS%2F9ebnZCNrtPhKcdDSRwQiGaIqA1KWq0A0AaydCfEa2D9wOz0DlqoiPe24%2BBpbi35ca0Y%2BYTXQMd1ITVf01c9oUof7%2BjmnVEdxBPOJHrAhrDWXHUY4vR3SsyE%2FUaH2cs5f4dd2LgYQG%2BzRySD0ttE%2BnRBzXO4dxRwKbF%2BGJ5p5vC%2Fda6bAt92cC1Iqrl46kCBhjU64Ds2Sc%2BCsYSaNYTd%2F%2FLa6WSEkCzot5bayKyM%2FusnbJFIBH3x2yO9nwF2IBxp8sNJEXYdTAe2lhDQo%2BvVrSW1oFCRRgv9BSU5KvXusasuLR315d5CfeCBrU0CS8kFgMPSpXTBL5a5dP%2FbwkdOEnN0S%2BkdzMYAZR49%2FCiiGXL8fwieXPI%2BwX5EEHvg5J8aZuUxkUshMKTOaIZbnWB09Eia4HB5fNSIK69AwPUG2TUB7U2EFv3GVnWLZxMYcL%2B8cogGp%2BlfJsLrXdchtvBoX9KoI6vHmTnqI7U548XFFR810GRVWlwXBmcuc5xuN2b83ie5tIwVc%2F%2F9lt%2FAn1K2oc0yfnQOkqPzyK6m848G3w3vEe%2B09sJGTQTbL59nzhFj%2BQOcrgraPQiC5vdLRExVCcZjZSVWRcNh7vNWw%2FjGxna7Y4aKZLC2Ol4wzsGwUtNgJzpdUbOyM27cNa3Ii06wgEB0jTBC3WMTkwXXFCwR4EDJehBaVhpU1Q8lstFYnvC%2Bkaik0b42Be62Z5ugC%2FUKQkt4kmV2oIh7rk2k2jZ0j39lKLs3SVMs7sR0A6RjpNWREBMyzJ5QT0IYQF2Y5LrYitea9MP2jladXgji3D%2FhESDnEbYqfPNt5K8S%2FV%2FFJ46uvTeCiEpPn4MfhCyzLa5eRr9edp2JezLUbDKzdEP4mgewpr7JKTjD5JAgnX2CtInBXBGivebgAWQhYI69UJzseGUuHlzGI6tZadsc5LQ7wuGMz%2BiQaOo5YnPQxrg%3D%3D--5UCjM9DI97mEyyJk1mNryBF03QuDyCS%2BmUWEyoC0UL8%3D',
    'lodr': 'dede2deen2defr2deit2dees2dear2dezh2deda2deel2dejp2dehr2delt2denl2depl2dept2deru2desv2desl2decs2detr2dehu2enfr2enit2enes2enzh2enjp2enko2ennl2enpl2enpt2enru2envi2',
}

def find_similar_words(raw):
    url = f"https://owb.langenscheidt.com/{raw}?directions=ar-%3Ede%2Ccs-%3Ede%2Cda-%3Ede%2Cde-%3Ear%2Cde-%3Ecs%2Cde-%3Eda%2Cde-%3Ede%2Cde-%3Ede%2Cde-%3Eel%2Cde-%3Een%2Cde-%3Ees%2Cde-%3Efr%2Cde-%3Ehr%2Cde-%3Ehu%2Cde-%3Eit%2Cde-%3Ejp%2Cde-%3Elt%2Cde-%3Enl%2Cde-%3Epl%2Cde-%3Ept%2Cde-%3Eru%2Cde-%3Esl%2Cde-%3Esv%2Cde-%3Etr%2Cde-%3Ezh%2Cel-%3Ede%2Cen-%3Ede%2Cen-%3Ees%2Cen-%3Efr%2Cen-%3Eit%2Cen-%3Ejp%2Cen-%3Eko%2Cen-%3Enl%2Cen-%3Epl%2Cen-%3Ept%2Cen-%3Eru%2Cen-%3Evi%2Cen-%3Ezh%2Ces-%3Ede%2Ces-%3Een%2Cfr-%3Ede%2Cfr-%3Een%2Chr-%3Ede%2Chu-%3Ede%2Cit-%3Ede%2Cit-%3Een%2Cjp-%3Ede%2Cjp-%3Een%2Cko-%3Een%2Clt-%3Ede%2Cnl-%3Ede%2Cnl-%3Een%2Cpl-%3Ede%2Cpl-%3Een%2Cpt-%3Ede%2Cpt-%3Een%2Cru-%3Ede%2Cru-%3Een%2Csl-%3Ede%2Csv-%3Ede%2Ctr-%3Ede%2Cvi-%3Een%2Czh-%3Ede%2Czh-%3Een&dictionaries=d8%2Cda%2C2bc"
    response = requests.get(url,headers=headers,cookies= cookies)

    if response.status_code != 200:
        print(f"Error fetching data for {raw}: {response.status_code}")
        return [("connection error")]

    soup = BeautifulSoup(response.content, 'html.parser')
    headword_spans = soup.find_all('span', class_='headword')
    similar_wordlist = []

    for headword in headword_spans:
        similar_word = headword.text.strip()
        print(similar_word)
        similar_wordlist.append(similar_word)

    return similar_wordlist

print(type(find_similar_words("test")))

raw_words = words
all_headwords = []
# for raw in raw_words:
#     temp = find_similar_words(raw)

with open('./headwordsxag.txt', 'w') as file:
    for raw in raw_words:
        temp = find_similar_words(raw)
        file.write(str(temp))
        file.write('\n') 
    print('done')