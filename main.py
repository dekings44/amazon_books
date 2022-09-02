import requests
from bs4 import BeautifulSoup
import numpy as np
from time import sleep
from random import randint
import pandas as pd


#get the webpage


header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

#declaring the list of empty variables, So that we can append the data overall

book_rank = []
book_title = []
book_author = []
book_state =[]
book_price = []


#creating an array of values and passing it in the url for dynamic webpages
pages = np.arange(1,5,1)

#the whole core of the script
for page in pages:
    page = requests.get("https://www.amazon.co.uk/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_1?_encoding=UTF8&pg="+str(page), headers=header)
    soup = BeautifulSoup(page.text, 'html.parser')
    data = soup.find_all('div', {'id' : 'gridItemRoot'})
    sleep(randint(2,6))

    print(len(data))
    # print(acc_data[0])
    for store in data:
        rank = store.find('span', {'class' : 'zg-bdg-text'}).text
        book_rank.append(rank)

        title = store.find('div', {'class' : '_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y'}).text
        book_title.append(title)

        author = store.find('div', {'class' : '_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y'}).text
        book_author.append(author)
        
        state = store.find('span', {'class' : 'a-size-small a-color-secondary a-text-normal'}).text
        book_state.append(state)
        
        price = store.find('span', {'class' : '_cDEzb_p13n-sc-price_3mJ9Z'}).text
        book_price.append(price)
        
        

