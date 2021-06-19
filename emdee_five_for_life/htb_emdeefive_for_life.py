import requests
from bs4 import BeautifulSoup as bs
import hashlib
import re


s = requests.Session()

url = input("url (http://xx.xx.xx.xx:xxxxx/) >")

r = s.get(url)

soup = bs(r.text, "html.parser")
content = soup.find_all("h3")[0].contents[0]

# print(content)

res = hashlib.md5(content.encode())

Hash = res.hexdigest()


r = s.post(url = url, data = {"hash": Hash})
res2 = re.findall(r"align='center'>(HTB{.+})<\/p>", r.text)
print(res2[0])




