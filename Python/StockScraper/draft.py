import bs4
import requests
from bs4 import BeautifulSoup


def parsePrice(quote=''):    
    r = requests.get('https://finance.yahoo.com/quote/'+quote+'?p='+quote)
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

def runProgram():
    qt = input('Which quote do you want to check the price? ')
    print("The current stock price for "+ qt + " is: U$"+parsePrice(qt))

runProgram()
