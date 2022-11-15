import urllib3
from bs4 import BeautifulSoup
import pandas as pd

products = []  # List to store name of the product
prices = []  # List to store price of the product
ratings = []  # List to store rating of the product
images = []
productLinks =[]

http = urllib3.PoolManager()
r = http.request('GET', 'https://www.flipkart.com/search?q=trimer&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off')

print (r.data.decode('utf-8'))

rData=r.data
exit()
soup = BeautifulSoup(rData, 'html.parser')

for a in soup.findAll('div', attrs={'class':'_3liAhj _1R0K0g'}):
    try:
        name = a.find('a', attrs={'class':'_2cLu-l'}) 
        price = a.find('div', attrs={'class':'_1vC4OE'})
        rating = a.find('div', attrs={'class':'hGSR34'})
        image = a.find('img', attrs={'class':'_1Nyybr'})
        
        if image == None or rating == None or price == None or name == None:
            continue
        
        products.append(name.text)
        prices.append(price.text)
        ratings.append(rating.text)
        images.append(image['src'])
        productLinks.append("https://www.flipkart.com" + name['href'])
        
    except AttributeError:
        pass
    

df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings, 'Image Link': images, 'Product Link':productLinks })
#print(len(products), len(prices), len(ratings), len(images), len(productLinks))
print(df)
df.to_csv('productsnew11.csv', index=False, encoding='utf-8')