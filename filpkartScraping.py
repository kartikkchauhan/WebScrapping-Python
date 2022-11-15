from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(executable_path='chromedriver')
products = []  # List to store name of the product
prices = []  # List to store price of the product
ratings = []  # List to store rating of the product
driver.get("https://www.flipkart.com/search?q=bestmobile")
soup = BeautifulSoup(driver.page_source, 'lxml')

for a in soup.findAll('div', attrs={'class':'bhgxx2 col-12-12'}):
    try:
        name = a.find('div', attrs={'class':'_3wU53n'}) 
        price = a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
        rating = a.find('div', attrs={'class':'_31qSD5'})
        products.append(name.text)
        prices.append(price.text)
        ratings.append(rating.text)
    except AttributeError:
        pass
    

df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
print(df)
for x in products:
  print(x)
  break
df.to_csv('products.csv', index=False, encoding='utf-8')
