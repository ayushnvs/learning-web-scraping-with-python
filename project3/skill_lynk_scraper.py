import bs4 
from bs4 import BeautifulSoup
import requests
import lxml
import re

url = "https://skill-lync.com/careers/jobs"

html_data = requests.get(url).text

soup = BeautifulSoup(html_data, "lxml")

job_card = soup.find_all("div", class_="card")

print(job_card, len(job_card))

print(soup.prettify())