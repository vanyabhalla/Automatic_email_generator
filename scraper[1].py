import requests
from bs4 import BeautifulSoup
import smtplib
import time

# set the headers and user string
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}

# send a request to fetch HTML of the page
URL = 'https://www.amazon.in/Polycom-Voxbox-ultra-compact-Speakerphone-technology/dp/B07CSQGF3M/ref=sr_1_14?dchild=1&fst=as%3Aoff&qid=1588401713&refinements=p_n_is_cod_eligible%3A4931671031&rnid=4931670031&s=electronics&sr=1-14'

def check_price():
    page=requests.get(URL,headers=headers)

    # create the soup object
    soup = BeautifulSoup(page.content, 'html.parser')

    # change the encoding to utf-8
    soup.encode('utf-8')

    #print(soup.prettify())

    title = soup.find(id= "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
    #print(price)

    #converting the string amount to float
    converted_price = float(price[0:5])
    if(converted_price < 19500):
        send_mail()

    #using strip to remove extra spaces in the title
    print(converted_price)
    print(title.strip())
    if(converted_price > 19500):
        send_mail()
    

# function that sends an email if the prices fell down
def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('email@gmail.com', 'pwd')

  subject = 'Price Fell Down'
  body = "Check the amazon link  https://www.amazon.in/Polycom-Voxbox-ultra-compact-Speakerphone-technology/dp/B07CSQGF3M/ref=sr_1_14?dchild=1&fst=as%3Aoff&qid=1588401713&refinements=p_n_is_cod_eligible%3A4931671031&rnid=4931670031&s=electronics&sr=1-14"

  msg = f"Subject: {subject}\n\n{body}"
  
  server.sendmail(
    'sender@gmail.com',
    'receiver@yahoo.co.in',
    msg
  )
  #print a message to check if the email has been sent
  print('Hey Email has been sent')
  # quit the server
  server.quit()

#loop that allows the program to regularly check for prices
while(True):
  check_price()
  time.sleep(60 * 60)

