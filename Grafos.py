from collections import defaultdict
import networkx as nx
from os import listdir
import time
import os
from tqdm import tqdm
dir_path=os.path.dirname(__file__)
cd_path=dir_path+'/home/tccllb/backup/scrap_hyper2'
aresta=[]




G = nx.Graph()
total_paginas=[]
antes=time.time()
for i in tqdm(os.listdir(cd_path),'loading'):
    try:
        txt = open("{}/{}".format(cd_path,i),"r", encoding="utf-16")
        txt_lido = txt.readlines()
        arrumado=i.replace('_hyper.txt','')
        G.add_node(arrumado)
        for j in txt_lido:
            total_paginas.append(j[6:-1].replace('/',','))
            aresta.append((arrumado,j[6:-1]))
            G.add_edge(arrumado, j[6:-1])
    except:
        print(i)
        pass
print(time.time()-antes)
nx.write_edgelist(G,'grafo_before_pagerank')
