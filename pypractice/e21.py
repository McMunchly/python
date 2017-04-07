# prints out a full web article into a text document

import requests
from bs4 import BeautifulSoup

filename = input("Input name of file: ")

filename = filename + ".txt"

base_url = "http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

all_p_cn_text_body = soup.select("div")

with open(filename, 'w') as open_file:
  for elem in all_p_cn_text_body[7:]:
    open_file.write(elem.text)


