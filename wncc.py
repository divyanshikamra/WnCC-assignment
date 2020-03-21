from bs4 import BeautifulSoup
import requests

i= requests.get('https://www.indiatoday.in/technology')
soup = BeautifulSoup( i.text, 'lxml' )

news_box = soup.find('ul' , {'class' : 'itg-listing'})
all_news= news_box.find_all('a' )

for news in all_news:
    print(news.text)
    print()

    
