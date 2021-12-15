import bs4
from bs4 import BeautifulSoup
import lxml
import re
import threading
import requests
import time
import csv

links = []

def link_scraper(count):
    # Obtaining links
    
    url = f"https://gotytv.com/tvseries?page={count}"
    html_data = requests.get(url).text
    soup = BeautifulSoup(html_data, "lxml")
    link_content = soup.find_all("div", class_="col-4 col-lg-2 px-2")
    for content in link_content:
        links.append(content.a["href"])

def content_scraper(link):
    # Scraping data
    for link in links:
        series_html_data = requests.get(link).text

        series_soup = BeautifulSoup(series_html_data, "lxml")

        series_data = series_soup.find("div", class_="dtBosSlider")
        series_name = series_data.h1.text
        release_year, series_genre_rating = series_data.find_all("b")[0].text, ", ".join([genre.text for genre in series_data.find_all("b")[1:]])
        series_description = series_soup.find("div", class_="contentText").p.text

        # Searching for genre: Science Fiction
        pattern = r"^.*([Ff]antasy).*$"
        match = re.match(pattern, series_genre_rating) is not None
        if match:
            with open("gotytv_fantasy_thread.txt", "a") as f:
                f.write(f"{counter}. Name: {series_name}\n")
                f.write(f"    Release in: {release_year}\n")
                f.write(f"    Genre/Rating: {series_genre_rating}\n")
                f.write(f"    Description: {series_description}\n")
                f.write(f"    Link: {link}\n\n")
        else:
            pass

if __name__ == "__main__":
    print("Scraping Started...")
    start = time.time()
    link_thread = []
    content_thread = []
    for count in range(1, 5):
        t1 = threading.Thread(target=link_scraper, args=[count])
        t1.start()
        link_thread.append(t1)
    for threadl in link_thread:
        threadl.join()
    for counter, link in enumerate(links):
        t2 = threading.Thread(target=content_scraper, args=[link])
        t2.start()
        content_thread.append(t2)
    for threadc in content_thread:
        threadc.join()
    end = time.time()
    print("Completed!")
    print(f"Total time taken: {round(start-end, 2)} s")
    print("Done!")