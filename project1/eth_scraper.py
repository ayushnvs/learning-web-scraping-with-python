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

    currency = currency_data[0].find_all("tr")

    pattern = re.compile(r"^.*Ethereum.*Buy(\$.*\...)(\d+\.\d\d%.*)$")
    match = re.match(pattern, currency[1].text)
    Time = time.asctime()

    return [match[1], Time]

if __name__ == "__main__":
    while True:
        print("Scraping Started...")
        try:
            data = scraping_coinmarketcap()
            with open("currency_data/ETH.csv", "a", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(data)
            print("Scraping Done...")
            sleep_time = 10
            print("Waiting for 10 minutes...")
            time.sleep(sleep_time*60)    
        except requests.exceptions.ConnectionError:
            print("ConnectionError: Failed to establish new connection!")
            sleep_time = 1
            print("Retrying in a minute...")
            time.sleep(sleep_time*60)    