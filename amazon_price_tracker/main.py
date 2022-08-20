import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

# Item url
ITEM_URL = "https://www.amazon.co.uk/Sportsroyals-Station-Strength-Training-Equipment/dp/B07SM8VJ6P/ref=sr_1_1_sspa?crid=34O0FRGX2B1HG&keywords=pull+up+station&qid=1660973276&sprefix=pull%2Caps%2C72&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyV0pQUk5UMzRWQTNDJmVuY3J5cHRlZElkPUEwMzY2MDc3MlpRQjlQRzdQS1FMUyZlbmNyeXB0ZWRBZElkPUExMDIwMjU3MzRKUjhVWTJHNjg3QSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
PURCHASE_PRICE = 100.00
# Get personal browser header ( http://myhttpheader.com/ )
headers = {
    "Accept-Language": "en-US,en-GB;q=0.9,en;q=0.8,ro;q=0.7,es;q=0.6",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/104.0.0.0 Safari/537.36"
}

# Request page
response = requests.get(url=ITEM_URL, headers=headers)
response.raise_for_status()
item_page = response.text

# Scrape
soup = BeautifulSoup(item_page, "lxml")
price = float(soup.find(name="span", class_="a-price-whole").getText())

if price <= PURCHASE_PRICE:
    connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
    connection.starttls()
    connection.login("YOUR_MAIL", "YOUR_PASSWORD")
    connection.sendmail(
        from_addr="YOUR_MAIL",
        to_addrs="YOUR_MAIL",
        msg="Discount YOUR_ITEM. Buy me now!",
    )
