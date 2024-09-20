import requests

# Define the URL with parameters
url = "https://api.woerterbuchnetz.de/dictionaries/Lexer/lemmata/lemma/dac*/100/json?term=dac&_type=query&q=dac"

# Set headers
headers = {
    "Host": "api.woerterbuchnetz.de",
    "Sec-Ch-Ua": "Not;A=Brand;v=24, Chromium;v=128",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "de-DE,de;q=0.9",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36",
    "Sec-Ch-Ua-Platform": "macOS",
    "Origin": "https://woerterbuchnetz.de",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://woerterbuchnetz.de/",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

# Send the GET request
response = requests.get(url, headers=headers)

# Check for successful response
if response.status_code == 200:
  # Response data is in JSON format, access it using response.json()
  data = response.json()
  print(data)
else:
  print(f"Error: {response.status_code}")