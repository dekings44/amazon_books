import requests
from bs4 import BeautifulSoup


#get the webpage
url = 'https://www.amazon.co.uk/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_1?_encoding=UTF8&pg=1'

header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

page = requests.get(url, headers=header)

soup = BeautifulSoup(page.content, 'html.parser')

books = soup.find_all(id = 'gridItemRoot')

