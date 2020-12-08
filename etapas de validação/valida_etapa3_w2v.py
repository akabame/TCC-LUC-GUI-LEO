from datetime import datetime
from gensim.models import Word2Vec
from scipy.stats import norm
from scipy import spatial
import numpy as np
from numpy import dot
from tqdm import tqdm
import pandas as pd
import random
import statistics

def same_words(inter,df1,df2,tamanho):
    lista=set(inter)
    vetor1={}
    vetor2={}
    for i in df1.columns.tolist():
        vetor1[i]=[]
        vetor2[i]=[]
    for index,row in df1.iterrows():
        for i in df1.columns.tolist():
            if row[i][0] in lista and len(vetor1[i])<tamanho:
                vetor1[i].append(row[i][0])
    for index,row in df2.iterrows():
        for i in df2.columns.tolist():
            if row[i][0] in lista and len(vetor2[i])<tamanho:
                vetor2[i].append(row[i][0])
    return quantos_iguais(vetor1,vetor2)

def quantos_iguais(df,df2):
    iguais=[]
    for i in df:
        cont=0
        tupla_list=[]
        atual=df2[i]
        for nome in atual:
            tupla_list.append(nome)
        for j in df[i]:
            if j in tupla_list:
                cont=cont+1
        iguais.append(cont/len(df[i]))
    return iguais

#Validação etapa3: w2v

def load(model):
    print('loading ' + model)
    w2v = Word2Vec.load(model)
    
    v = w2v.wv.vocab
    nomes = []
#    dim = {}
    
    for i in tqdm(v,'criando dict e separando nomes'):
        nomes.append(i)
#       dim[i] = w2v.wv[i]
    print('')  
    return nomes,w2v

p1,model1 = load('w2v_model_ascii')
p2,model2 = load('w2v_model_ascii3')
       
#pega palavras comuns a ambos modelos
p_comum_total = list(set(p1) & set(p2))

#seleciona 300 palavras aleatorias da lista
p_comum = random.sample(p_comum_total, 300)
#p_comum = ['carro','janela','russia','oceano','copo','girafa','boia','unha','lapide','cerveja']
#p_comum = model1.wv.index2entity[:300]

#p_comum = ['banho','gado','desfrutar','atlas','esculpir','arquiteto','protesto','decolar','elegante','grito','cerdas','cana','conversa','cemiterio','bebida','chaves','dicas','dado','cardeais','arma','alterar','arqueologia','barbear','barulhento','antenas','aguarde','casulo','arroz','gato','cronometragem','laranja','linha','luva','lixo','lua','macaco','musica','museo','ninho','navio','noiva','novela','noite','ovelha','ovo','peixe','polonia','palito','pintura','queijo','quantidade','qualidade','rua','rato','sapo','sopa','sitio','saco','taxi','tatuagem','tapete','trajeto','trecho','uva','ultrapassar','ultimo','uniao','zebra','zelo','voltagem','volta','velocidade','vasco','xicara','xerife','vaca','voo','trem','tiro','tropa','troia','templo','tragedia','viagem','valor','vento','vinho','validade']

df1 = pd.DataFrame()
df2 = pd.DataFrame()

count = 0
viz = 100
for i in tqdm(p_comum,'buscando palavras similares'):
    df1[i] = model1.wv.most_similar(positive=[p_comum[count]],topn=viz)
    df2[i] = model2.wv.most_similar(positive=[p_comum[count]],topn=viz)
    count = count + 1

result = same_words(p_comum_total,df1,df2,50)
print(statistics.mean(result))
print(p_comum)
print(result)





    
    
    
    

