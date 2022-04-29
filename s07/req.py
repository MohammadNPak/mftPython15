

import requests

with open("digikala_index.html",'w',encoding='utf8') as f:
    data = requests.get("https://digikala.com").text
    f.write(data)
