import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'Past amazon prodat URL'

headers = {'user-agent': 'Your User agent'}

def check_price():
    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content, 'html.parser')

    # get title of our product
    title=soup.find(id='productTitle').get_text()
    # it's track price from amazon page
    price=soup.find(id='priceblock_ourprice').get_text()

    # as we know in indian price we use comma so that's why i use replace method
    converted_price=int(price[1:7].replace(',', ''))

    print('Your Product is : ',title.strip())
    print('Price is ', price)

    if converted_price < 28000:
        print('Price is fell down check your mail')
        send_mail()
        print('Now price is ', price)

    elif converted_price > 30000:
        print('Price is high ')

    else:
        print('Not changes in price')
        send_mail()




def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    server.login('your mail id', 'password')

    subject = 'Price is fell down'
    body = 'Check the amazon link : paste URL'

    msg = f"Subject : {subject} \n\n {body}"

    server.sendmail(
        'Your ID', 'write mail id where u send mail', msg )

    print('Mail has been send')
    server.quit()

check_price()