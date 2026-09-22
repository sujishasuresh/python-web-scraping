import requests
from bs4 import BeautifulSoup

def scrape():

    url='https://quotes.toscrape.com/?utm_source=chatgpt.com/'
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    print(soup)
    title=soup.select_one('h1').text
    quote = soup.select_one('.quote .text').get_text(strip=True)
    author = soup.select_one('.quote .author').get_text(strip=True)



    print("Title: ",title)
    print("Quote:", quote)
    print("Author:", author)




if __name__== '__main__':
    scrape()