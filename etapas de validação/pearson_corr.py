import numpy as np 
import pandas as pd
from scipy import stats
import json

cos = []
euc = []
grafo = []

#nome do json com os resultados da etapa 2 e 4
with open('correlacao_bruta_2.txt') as json_file:
    data = json.load(json_file)


for i in data:
    cos.append(data[i][0])
    euc.append(data[i][1])
    grafo.append(data[i][2])    

cos = np.array(cos)
euc = np.array(euc)
grafo = np.array(grafo)
cos_grafo = stats.pearsonr(cos, grafo)
euc_grafo = stats.pearsonr(euc, grafo)
print('correlação sim_cosseno com grafo: '+str(round(cos_grafo[0],4)))
print('p-value:'+str(round(cos_grafo[1],4)))
print('correlação dist_euc com grafo: '+str(round(euc_grafo[0],4)))
print('p-value:'+str(round(euc_grafo[1],4)))


