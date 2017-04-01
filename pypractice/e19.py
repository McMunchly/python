# prints out a full web article in the terminal

import requests
from bs4 import BeautifulSoup

base_url = "http://www.gamasutra.com/view/news/294378/Report_Glu_Mobile_cuts_25_jobs_and_shutters_Portland_studio.php"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

all_p_cn_text_body = soup.select("div")

for elem in all_p_cn_text_body[7:]:
  print(elem.text)
