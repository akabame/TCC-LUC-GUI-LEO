import numpy as np
from tqdm import tqdm
import pandas as pd
import random
from scipy.stats import norm
from scipy import spatial
import networkx as nx
from os import listdir
import time
import os
from tqdm import tqdm
import json
import math

#load no array do model w2v
print('loading do array w2v')
larray = np.load('w2v_tfidf_array.npy',allow_pickle=True)

print('loading do grafo')
#load grafo
G=nx.read_edgelist('grafo_before_pagerank_corrigido')

#dicionario
sim_doc = {}

def dist_euc(vet1,vet2):
    soma = 0
    for i in range(len(vet1)):
        soma = soma + ((vet2[i] - vet1[i])**2)
        
    return math.sqrt(soma)

count = 0

for i in tqdm(range(200),'Calculando'):
    try:
        #documento aleatorio
        doc1 = random.randint(1,839242)
        doc2 = random.randint(1,839242)
    
        #similaridade de cossenos entre docs
        cos_sim = 1 - spatial.distance.cosine(larray[doc1][1],larray[doc2][1])
    
        #distancia euclidiana
        distEuc = dist_euc(larray[doc1][1],larray[doc2][1])

    #    dijkstra entre documentos
        lista=nx.dijkstra_path(G, larray[doc1][0], larray[doc2][0])
    
    #    distancia total dijkstra
        dist_grafo = len(lista)
    
         #dict p/ comparação
        sim_doc[larray[doc1][0]+'___'+larray[doc2][0]] = cos_sim,distEuc,dist_grafo
    except Exception as e:
        count = count + 1
        i = i - 1
        print(e)
        continue

#print(sim_doc)
print(count)
with open('correlacao_tfidf_bruta.txt', 'w') as outfile:
    json.dump(sim_doc, outfile)


