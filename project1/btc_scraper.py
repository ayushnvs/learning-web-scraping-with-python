import bs4
from bs4 import BeautifulSoup
import requests
import re
import time
import csv

def scraping_coinmarketcap():
	html_data = requests.get("https://coinmarketcap.com/currencies/bitcoin/").text

	soup = BeautifulSoup(html_data, "lxml")

	currency_data = soup.find_all("div", {'class': 'priceValue'})
	data = currency_data[0].text
	Time = time.asctime()
	return [data, Time]

if __name__ == "__main__":
    while True:
        print("Scraping Started...")
        try:
            data = scraping_coinmarketcap()
            print("Scraping Done.\nWriting data to file...")
            with open("currency_data/BTC.csv", "a", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(data)
            print("Writing Completed.")
            print("Waiting for 10 minutes...")
            sleep_time = 10
            time.sleep(sleep_time*60)
        except requests.exceptions.ConnectionError:
            print("ConnectionError: Failed to establish new connection!")
            print("Retrying in 5 seconds...")
            sleep_time = 5
            time.sleep(sleep_time)