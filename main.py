from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from time import sleep
import re


url='https://www.pelando.com.br/'
site = uc.Chrome()
site.get(url=url)
sleep(5)
site.refresh()
sleep(5)

html = site.find_element(By.TAG_NAME,'html')
for i in range(0,30):
    html.send_keys(Keys.END)
    sleep(2)

sleep(2)
page = site.page_source
soup=BeautifulSoup(page,'html.parser')
table = soup.find('ul',class_='sc-cb8be5d8-1 cFepSf')
products = table.find_all('li',class_='sc-cb8be5d8-2 hliMah')

cont_=0
for i in products:
    
    try:
        tag_a = i.find('a',class_='sc-iYqbYc dtFNsU')
        name = i.find('a',class_='sc-iYqbYc dtFNsU')
        price = i.find('div',class_='sc-dlDPRo kvggRW')
        temp = i.find('span',class_=re.compile(r'sc-egpspN [a-z]+',flags=re.I))
    

        if tag_a and name and price and temp:
            link = tag_a.get('href')
            link= url+link
            name = name.get_text(' ',strip=True)
            price=price.get_text(' ',strip=True)
            temp = int(temp.get_text(' ',strip=True).replace('º',''))
            cont_+=1
    except Exception as e:        
        pass

    
print(f'{cont_} encontrados ')
site.close()
