from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as soup
from selenium.webdriver.common.by import By
from datetime import datetime

#torna chrome driver headless
opts = Options()
opts.add_argument("--headless")
#opts.add_argument("--disable-gpu")

#chrome driver para navegar
chr_d = 'C:\\Users\\Lucas\\Desktop\\bullshitices\\chromedriver.exe'
# driver = webdriver.Chrome(executable_path = chr_d, opts)
driver = webdriver.Chrome(options = opts,executable_path = chr_d)

driver.get("https://pt.wikipedia.org/wiki/Matem%C3%A1tica")
now = datetime.now()
source = driver.page_source
html = soup(source, 'html.parser')

box = html.find("div", {"id": "bodyContent"})
deck = box.find("div", {"id": "mw-content-text"})
card = deck.find("div", {"class": "mw-parser-output"})

p = card.find_all('p')
#now = datetime.now()
with open('C:\\Users\\Lucas\\Desktop\\bullshitices\\matematica.txt','a',encoding='utf-8') as arquivo:
#arquivo = open('C:\\Users\\Lucas\\Desktop\\bullshitices\\matematica.txt','a')
    for i in p:
        arquivo.write(str(i.text))       
arquivo.close()
print(datetime.now()-now)

