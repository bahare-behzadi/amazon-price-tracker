import requests
from bs4 import BeautifulSoup
import smtplib


EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"
SMTP_AGENT = "smtp.gmail.com"
MY_APPROPRIATE_PRICE = 90.00  # your price
Link = ("YOUR FAVORITE PODUCT LINK")

header = {
        "User-Agent": "YOUR USER HTML AGENT",
        "Accept-Language": "en-US,en;q=0.9,en-CA;q=0.8",
}
response = requests.get(Link,headers=header)
response.raise_for_status()
amazon_soup = BeautifulSoup(response.text,  "html.parser")
print(amazon_soup)
price = amazon_soup.find("span", class_="aok-offscreen")
price_text = price.text
print(price_text)
price_text = price_text.split()[0]
price_text = price_text.replace(',', '.')
price_float = float(price_text)
print(price_float)
if price_float < MY_APPROPRIATE_PRICE:
      connection = smtplib.SMTP(SMTP_AGENT)
      connection.starttls()
      connection.login(EMAIL, PASSWORD)
      message = f"subject:❗❗ PRICE WARNING ❗❗\n\n The price is reduced 📧 REAL PRICE IS NOW {price_float} ‼️"
      connection.sendmail(from_addr=EMAIL,to_addrs=EMAIL,msg=message.encode("utf-8"))