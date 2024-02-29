import requests
import lxml
from bs4 import BeautifulSoup


class AmazonPriceTracker:
    def __init__(self, url=""):
        self.headers = {
            "Request": "LineGET/HTTP/1.1",
            "upgrade-insecure-requests": "1",
            "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36(KHTML,like Gecko) Chrome/120.0.0.0"
                          "Safari/537.36 OPR/106.0.0.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                      "image/avif,image/webp,image/apng,*/*;q=0.8,"
                      "application/signed-exchange;v=b3;q=0.7",
            "sec-ch-ua": "\"Not_A Brand\";v=\"8\",\"Chromium\";v=\"120\",\"Opera\";v=\"106\"",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "Accept-Encoding": "gzip,deflate,br",
            "Accept-Language": "en-US,en;q=0.9",
            "x-forwarded-proto": "https",
            "x-https": "on"
        }
        self.url = url

    def get_price_info(self):
        response = requests.get(self.url, headers=self.headers)
        amazon_web_page = response.text
        soup = BeautifulSoup(amazon_web_page, "lxml")
        item_price = soup.find(name="span", class_="a-price-whole")
        price = int(item_price.text.strip(".").replace(",", ""))
        return price
