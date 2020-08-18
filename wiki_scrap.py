from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as soup
from selenium.webdriver.common.by import By
from datetime import datetime
import numpy as np
import os
import time
#import re
#dir_path = os.path.dirname(__file__)
dir_path = 'C:\\Users\\Lucas\\Desktop\\bullshitices'
#escreve info das paginas em txt
def escreve_txt(path,vetor,tipo):
    with open(path,tipo, encoding="utf-16") as outfile:
        for line in vetor:
            outfile.write(str(line))
    outfile.close()
    
def webScrapper(url):
    
    global driver
    
    driver.get("{}".format(url))
    #    now = datetime.now()
    source = driver.page_source
    html = soup(source, 'html.parser')
    
    box = html.find("div", {"id": "bodyContent"})
    deck = box.find("div", {"id": "mw-content-text"})
    card = deck.find("div", {"class": "mw-parser-output"})
    
    p = card.find_all('p')
    vet_txt = []
    vet_hyper = []
    nome = str(driver.current_url)
    nome = nome.split('/')[-1]
    #now = datetime.now()
    for i in p:
        for a in i.find_all('a', href=True):
            if str(a['href'][0]) == '/':
                vet_hyper.append(str(a['href'])+'\n')
        vet_txt.append(str(i.text))
    
    escreve_txt("{}\\scrap_text\\{}.txt".format(dir_path,nome),vet_txt,'w')
    escreve_txt("{}\\scrap_hyper\\{}_hyper.txt".format(dir_path,nome),vet_hyper,'w')
    escreve_txt("{}\\todas_urls.txt".format(dir_path,nome),vet_hyper,'a')
#    print(datetime.now()-now)
    return vet_hyper

#oções para navegador chrome
opts = Options()
opts.add_argument("--headless")
opts.add_argument("--log-level=3")
#opts.add_argument("--disable-gpu")

#chrome driver para navegar
#chr_d = '{}\\chromedriver.exe'.format(dir_path)
chr_d = 'C:\\Users\\Lucas\\Desktop\\bullshitices\\chromedriver.exe'

# driver = webdriver.Chrome(executable_path = chr_d, opts)
driver = webdriver.Chrome(options = opts,executable_path = chr_d)

#inicialização
try:
    urls_lidas = open("{}\\ja_lidos.txt".format(dir_path),"r")
    ja_lidos = urls_lidas.readlines()
#    ja_lidos = set(ja_lidos)
    urls_lidas.close()
#    print("!")
except:
    ja_lidos=0
    
if ja_lidos == 0:
    ja_lidos = []
    url = "https://pt.wikipedia.org/wiki/Matem%C3%A1tica"
    ja_lidos.append(url)
    novo_hyper = webScrapper(url)
    fila = novo_hyper
else:
    urls_lidas = open("{}\\todas_urls.txt".format(dir_path),"r", encoding="utf-16")
    fila = urls_lidas.readlines()
#    fila = set(fila)
    urls_lidas.close()
#ja_lidos=[]
tempo = datetime.now()
print('start') 
for i in range(100):
    print(i)
    url = fila.pop(0)
    if url in ja_lidos or url[0:6] != '/wiki/':
        continue
    ja_lidos.append(url)
    urls_lidas = open("{}\\ja_lidos.txt".format(dir_path),"a+")
    urls_lidas.write(url)
    try:
        novo_hyper = webScrapper("https://pt.wikipedia.org"+url)
        fila=fila+novo_hyper
    except:
        pass
    urls_lidas.close()
print(datetime.now()-tempo)
