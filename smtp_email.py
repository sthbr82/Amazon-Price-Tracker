import smtplib
import os

EMAIL = os.environ.get("EMAIL")
PASSWD = os.environ.get("PASSWD")
TO_ADDR = os.environ.get("TO_ADDR")

class SmtpEmailManager:
    def __init__(self):
        self.email = EMAIL
        self.passwd = PASSWD

    def send_email_alert(self, price, url, limit):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.passwd)
            connection.sendmail(from_addr=self.email,
                                to_addrs="sthbr82@gmail.com",
                                msg="Subject:Amazon Low price alert\n\n"
                                    f"Item price Rs{price} is below the {limit}\n"
                                    f"for the item {url}")

