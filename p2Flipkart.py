import urllib3
from bs4 import BeautifulSoup
import pandas as pd

products = []  # List to store name of the product
prices = []  # List to store price of the product
ratings = []  # List to store rating of the product

http = urllib3.PoolManager()
r = http.request('GET', 'https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')

#print (r.data.decode('utf-8'))

rData=r.data

soup = BeautifulSoup(rData, 'html.parser')

for a in soup.findAll('div', attrs={'class':'_1UoZlX'}):
    try:
        name = a.find('div', attrs={'class':'_3wU53n'}) 
        price = a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
        rating = a.find('div', attrs={'class':'hGSR34'})
        products.append(name.text)
        prices.append(price.text)
        ratings.append(rating.text)
    except AttributeError:
        pass
    

df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
print(df)
df.to_csv('productsnew.csv', index=False, encoding='utf-8')