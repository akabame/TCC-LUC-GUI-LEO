from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as soup
from selenium.webdriver.common.by import By
from datetime import datetime
#import re

def escreve_txt(path,vetor):
    with open(path,'a', encoding="utf-16") as outfile:
        for line in vetor:
            outfile.write(str(line))
    outfile.close()

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
vet_txt = []
vet_hyper = []
#now = datetime.now()
for i in p:
    for a in i.find_all('a', href=True):
        if str(a['href'][0]) == '/':
            vet_hyper.append(str(a['href'])+'\n')
    vet_txt.append(str(i.text))

escreve_txt("C:\\Users\\Lucas\\Desktop\\bullshitices\\matematica.txt",vet_txt)
escreve_txt("C:\\Users\\Lucas\\Desktop\\bullshitices\\matematica_hyper.txt",vet_hyper)
        
print(datetime.now()-now)

