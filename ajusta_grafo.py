import networkx as nx
from tqdm import tqdm
import json
G=nx.read_edgelist('grafo_before_pagerank')
with open('remove_file.txt') as json_file:
    data = json.load(json_file)
cont=0
for i in tqdm(data,'arquivos a remover'):
    try:
        G.remove_node(i.replace('.txt',''))
    except Exception as e:
        cont+=1
        print(e)
nx.write_edgelist(G,'grafo_before_pagerank_corrigido')
print(cont)
