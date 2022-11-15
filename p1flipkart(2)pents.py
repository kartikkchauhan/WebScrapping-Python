import urllib3
from bs4 import BeautifulSoup
import pandas as pd

products = []  # List to store name of the product
prices = []  # List to store price of the product
ratings = []  # List to store rating of the product
images = []
productLinks =[]



http = urllib3.PoolManager()
r = http.request('GET', 'https://www.flipkart.com/search?q=pents&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')

#print (r.data.decode('utf-8'))

rData=r.data

soup = BeautifulSoup(rData, 'html.parser')

for a in soup.findAll('div', attrs={'class':'IIdQZO _1R0K0g _1SSAGr'}):
    try:
        name = a.find('div', attrs={'class':'_2mylT6'}) 
        price = a.find('div', attrs={'class':'_1vC4OE'})
        #rating = a.find('div', attrs={'class':'hGSR34'})
        #image = a.find('img', attrs={'class':'_3togXc'})
        link = a.find('a', attrs={'class':'_3dqZjq'})

        if price == None or name == None or link == None:
            continue
        
        products.append(name.text)
        prices.append(price.text)
        #ratings.append(rating.text)
        #images.append(image['src'])
        productLinks.append("https://www.flipkart.com" + link['href'])
    except AttributeError:
        pass
    

#print(prices[0])
#print(ratings[0])
#print(images[0])
#print(productLinks[0])
df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': productLinks})
print(df)
#df.to_csv('productsnew.csv', index=False, encoding='utf-8')
