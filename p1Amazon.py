import urllib3
from bs4 import BeautifulSoup
import pandas as pd

products = []  # List to store name of the product
prices = []  # List to store price of the product
ratings = []  # List to store rating of the product
images = []
productLinks =[]

http = urllib3.PoolManager()
r = http.request('GET', 'https://www.amazon.in/s?k=best+mobile&ref=nb_sb_noss_2')

#print (r.data.decode('utf-8'))

rData=r.data

soup = BeautifulSoup(rData, 'html.parser')

for a in soup.findAll('div', attrs={'class':'s-include-content-margin s-border-bottom'}):
    try:
        name = a.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'}) 
        price = a.find('span', attrs={'class':'a-price-whole'})
        rating = a.find('span', attrs={'class':'a-icon-alt'})
        image = a.find('img')
        link = a.find('a', attrs={'class' : 'a-link-normal a-text-normal'})
        
        if image == None or rating == None or price == None or name == None or link == None :
            continue
        
        products.append(name.text)
        prices.append(price.text)
        ratings.append(rating.text)
        images.append(image['src'])
        productLinks.append("https://www.amazon.in" + link['href'])
        
    except AttributeError:
        pass
    

df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings, 'Image Link': images, 'Product Link':productLinks })
#print(len(products), len(prices), len(ratings), len(images))
print(df)
df.to_csv('productsnew1.csv', index=False, encoding='utf-8')