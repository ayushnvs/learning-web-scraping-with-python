import bs4
from bs4 import BeautifulSoup
import lxml
import ssl
import requests
import urllib
import csv
import re
import time
import threading

series_links = []

def scraping_series_links():
    print("Obtaining links...")
    count = 2
    while count < 320:
        print(count)
        try:
            url = f"https://gotytv.com/tvseries?page={count}"
        except:
            break
        html_data = requests.get(url).text
        soup = BeautifulSoup(html_data, "lxml")
        link_content = soup.find_all("div", class_="col-4 col-lg-2 px-2")
        for content in link_content:
            series_links.append(content.a["href"])
        count += 1
    print("Completed...")
    
def scraping_series_data(series_links):
    count = 1
    print("Scraping Series Data...")
    for link in series_links:
        # print(link)
        series_html_data = requests.get(link).text

        series_soup = BeautifulSoup(series_html_data, "lxml")

        series_data = series_soup.find("div", class_="dtBosSlider")
        series_name = series_data.h1.text
        release_year, series_genre_rating = series_data.find_all("b")[0].text, ", ".join([genre.text for genre in series_data.find_all("b")[1:]])
        series_description = series_soup.find("div", class_="contentText").p.text

        # Searching for genre: Science Fiction
        pattern = r"^.*([sS]cience\s[Ff]iction).*$"
        match = re.match(pattern, series_genre_rating) is not None
        if match:
            with open("gotytv_science_fiction.txt", "a") as f:
                f.write(f"{count}. Name: {series_name}\n")
                f.write(f"   Release in: {release_year}\n")
                f.write(f"   Genre/Rating: {series_genre_rating}\n")
                f.write(f"   Description: {series_description}\n")
                f.write(f"   Link: {link}\n\n")
            count += 1
        else:
            pass
    print("Completed...")

start = time.time()
scraping_series_links()
scraping_series_data(series_links)
end = time.time()
print("Completed!")
print(f"Total time taken: {round(start-end, 2)} s")
print("Done!")