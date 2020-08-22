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

def internet_lenta(count):
    
    global driver
    
    source = driver.page_source
    html = soup(source, 'html.parser')
    
    box = html.find("div", {"id": "bodyContent"})
    deck = box.find("div", {"id": "mw-content-text"})
    card = deck.find("div", {"class": "mw-parser-output"})
    
    p = card.find_all('p')
    if len(p) == 0 and count < 10:
        time.sleep(0.1)
        p = internet_lenta(count+1)
    else:
        print('muito lenta') 
        return p
    return p
    
def webScrapper(url):
    
    global ja_lidos
    global driver
    
    driver.get("{}".format(url))
    #    now = datetime.now()
    source = driver.page_source
    nome = str(driver.current_url)
    nome = nome.split('/wiki/')[-1]
#    print(nome[0:6])
    if '/wiki/'+nome in ja_lidos:
        return 0,0     
    html = soup(source, 'html.parser')
    
    box = html.find("div", {"id": "bodyContent"})
    deck = box.find("div", {"id": "mw-content-text"})
    card = deck.find("div", {"class": "mw-parser-output"})
    
    p = card.find_all('p')
    if len(p) == 0:
        p = internet_lenta(0)    
    vet_txt = []
    vet_hyper = []

    #now = datetime.now()
    for i in p:
        for a in i.find_all('a', href=True):
            if str(a['href'][0]) == '/':
                vet_hyper.append(str(a['href']+'\n'))
        vet_txt.append(str(i.text))
    
    escreve_txt("{}\\scrap_text\\{}.txt".format(dir_path,nome),vet_txt,'w')
    escreve_txt("{}\\scrap_hyper\\{}_hyper.txt".format(dir_path,nome),vet_hyper,'w')
    escreve_txt("{}\\todas_urls.txt".format(dir_path,nome),vet_hyper,'a')
#    print(datetime.now()-now)
    return vet_hyper,nome

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
    ja_lidos = set(ja_lidos)
    urls_lidas.close()
#    print("!")
except:
    ja_lidos=0
    
if ja_lidos == 0:
    ja_lidos = set()
    url = "https://pt.wikipedia.org/wiki/Matem%C3%A1tica"
    novo_hyper,url = webScrapper(url)
    ja_lidos.add('/wiki/'+url)
    fila = novo_hyper
else:
    urls_lidas = open("{}\\todas_urls.txt".format(dir_path),"r", encoding="utf-16")
    fila = urls_lidas.readlines()
#    fila = set(fila)
    urls_lidas.close()
#ja_lidos=[]
tempo = datetime.now()
print('start')
urls_a = []
urls_d = []
for i in range(100):
    try:
#        print(i)
        url = fila.pop(0).replace('\n','')
        urls_a.append(url)
        if url in ja_lidos or url[0:6] != '/wiki/':
            continue
        urls_lidas = open("{}\\ja_lidos.txt".format(dir_path),"a+")
        try:
            novo_hyper,url = webScrapper("https://pt.wikipedia.org"+url)
            if novo_hyper == 0:
                continue
            url = '/wiki/' + url
            urls_d.append(url)
            ja_lidos.add(url)
            fila=fila+novo_hyper
            urls_lidas.write(url+'\n')
        except Exception as e:
            print(e)
            print(url)
            pass
        urls_lidas.close()
    except Exception as e:
        print(e)
        print('erro zuado')
        continue        
print(datetime.now()-tempo)

