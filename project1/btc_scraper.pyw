import bs4
from bs4 import BeautifulSoup
import requests
import re
import time
import csv

def scraping_coinmarketcap():
    html_data = requests.get("https://coinmarketcap.com/").text

    soup = BeautifulSoup(html_data, "lxml")

    currency_data = soup.find_all("tbody")

    currency = currency_data[0].find("tr")

    pattern = re.compile(r"^.*Bitcoin.*Buy(\$.*\...)(\d+\.\d\d%.*)$")
    match = re.match(pattern, currency.text)
    Time = time.asctime()

    return [match[1], Time]

if __name__ == "__main__":
    while True:
        # print("Scraping Started...")
        try:
            data = scraping_coinmarketcap()
            with open("currency_data/BTC.csv", "a", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(data)
            # print("Scraping Done.")
            # print("Waiting for 10 minutes...")
            sleep_time = 10
            time.sleep(sleep_time*60)
        except requests.exceptions.ConnectionError:
            # print("ConnectionError: Failed to establish new connection!")
            # print("Retrying in a minute...")
            sleep_time = 1
            time.sleep(sleep_time*60)