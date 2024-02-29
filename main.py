import smtp_email
import amazon_price_parser

THRESHOLD_PRICE = 8000

if __name__ == "__main__":
    threshold_price = THRESHOLD_PRICE
    URL = ("https://www.amazon.in/Elgi-Ultra-Grind-Gold-2-Litre/dp/B00P4GQYDM/"
           "ref=sr_1_3?crid=2ZA5KEQJJ19FL&keywords=elgi+ultra+wet+grinder+2+litre"
           "&qid=1706095334&sprefix=elgi%2Caps%2C192&sr=8-3")

    price_tracker = amazon_price_parser.AmazonPriceTracker(url=URL)
    price = price_tracker.get_price_info()

    if price > threshold_price:
        smtp_obj = smtp_email.SmtpEmailManager()
        smtp_obj.send_email_alert(price, URL, threshold_price)
