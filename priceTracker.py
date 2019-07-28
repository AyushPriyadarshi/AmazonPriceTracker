import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/dp/B073Q5R6VR/ref=sr_1_1_sspa?keywords=macbook&qid=1564299746&s=gateway&sr=8-1-spons&psc=1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')

    price = soup1.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[2:8].replace(',', ''))

    if (converted_price < 70000):
        send_mail()
        print('Price Decreased , Mail sent')

    print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('aayush2618@gmail.com', 'muvatnectqjbszwr')

    subject = 'Price Fell Down!!'
    body = 'Price for your wished product has fallen! visit the link to check the product https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/dp/B073Q5R6VR/ref=sr_1_1_sspa?keywords=macbook&qid=1564299746&s=gateway&sr=8-1-spons&psc=1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'aayush2618@gmail.com',
        'bvcoe.ayushpriyadarshi@gmail.com',
        msg
    )

    server.quit()


while(True):
    check_price()
    time.sleep(60)
