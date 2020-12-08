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
larray = np.load('w2v_array_total.npy',allow_pickle=True)


#documentos selecionados
docs = []
for i in range(200):
    var = random.randint(0,839242)
    #var = random.randint(0,337284)
    if var in docs:
        i = i-1
        continue
    docs.append(random.randint(0,839242))
   # docs.append(random.randint(0,337284))
    

#dicionario para verificar pareamento
dict2 = {}
docs2 = docs.copy()

for i in docs:
    dict2[i] = []
    docs2.pop(0)
    for j in docs2:
        if i != j:
            dict2[i].append(j)

dict3 = {}

for i in dict2:
    for j in dict2[i]:
        #similaridade de cossenos entre docs
        cos_sim = 1 - spatial.distance.cosine(larray[i][1],larray[j][1])
        dict3[larray[i][0] + '__' + larray[j][0]] = cos_sim

         
df = pd.Series(dict3).to_frame()
df = df.rename(columns={0: 'cos'})

#print(sim_doc)
with open('estudo_cos.txt', 'w') as outfile:
    json.dump(dict3, outfile)


