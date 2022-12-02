import smtplib
import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.amazon.com/Lenovo-IdeaPad-Touchscreen-i3-1115G4-Bluetooth/dp/B09Z6PH29P/ref=sr_1_5?keywords=lenovo%2Blaptop&qid=1662233345&sr=8-5&th=1"

headers = {
    "Accept-Language":"en-GB,en;q=0.9,bg-BG;q=0.8,bg;q=0.7",
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
response = requests.get(url=url, headers=headers)
website = response.text
soup = BeautifulSoup(website, "lxml")
#print(soup.prettify())

price= soup.find(name="span", attrs={"class":"a-offscreen"}).text
real_price = float(price.split("$")[1])
print(real_price)
if real_price > 500:
    server = smtplib.SMTP("smtp")
    server.login(user="simeon@abv.bg", password="saodkaosdkaifhua201")
    server.sendmail(from_addr="simeon_sg@abv.bg", to_addrs="simeon_sg@abv.bg", msg="Lenovo bellow 500 $ GO for it!")
    server.quit()
