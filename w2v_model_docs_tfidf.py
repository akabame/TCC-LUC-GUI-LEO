import os
from datetime import datetime
from gensim.models import Word2Vec
from scipy.stats import norm
from scipy import spatial
import numpy as np
from numpy import dot
from tqdm import tqdm
import json
import math

#carregando modelo w2v
model = Word2Vec.load("w2v_model_total")
print('w2v carregado')


#carregando recorrencia global
with open('ocorrencia_global.txt') as outfile1:
    glob = json.load(outfile1)
print('global carregado')
    
#carregando recorrencia local
with open('ocorrencia_local.txt') as outfile2:
    loc = json.load(outfile2)
print('local carregado')

dir_path = os.path.dirname(__file__)
#txts = dir_path + '\\scrap_text\\scrap_text'
#txts = 'C:\\Users\\Lucas\\Desktop\\bullshitices\\scrap_text\\scrap_text'
txts = '/home/tccllb/backup/scrap_text_total_ascii'
corpus = []
texto = []
linha = []
replaces = ['(',')','{','}','"',':',';',"'",'\n','”','“','.',',','\xa0','\u2061','!','?']
pfora = 0

for filename in tqdm(os.listdir(txts),'loading'):
    try:
        if filename == 'scrap_text':
            pass
        #nome do arquvio e vetor com dimensões
        tf_acc = 0
        tupla = []
        vet = 0
        file = open(txts+'/'+filename, 'r+')
        read_file = file.read()
        file.close()
        text = read_file
        for rep in replaces:
            text = text.replace(rep,' ').lower()
        fim = text.split(' ')
        for word in range(len(fim)):            
            fim[word] = fim[word].split('[')[0].split('\\')[0].split(' ')[0]
            if fim[word] != '':
                try:
                #incluir fator tf-idf aqui
                    tfidf = loc[filename][fim[word]] * math.log(839342/glob[fim[word]])
                    vet = vet + (model.wv[fim[word]] * tfidf)
                    tf_acc = tf_acc + tfidf
                except:
                    pfora = pfora + 1
                    pass
                
    except Exception as e:
        print(e)
    if tf_acc == 0:
        tf_acc = 1

    #nome do arquivo
    tupla.append(filename[:-4])
    #vetor de dimensões
    tupla.append(vet/tf_acc)
    #documentos -> nome e vetor
    corpus.append(tupla)

nparray = np.array(corpus,dtype=object)
np.save('w2v_tfidf_array',nparray)
#no load, adicionar parâmetro allow_pickle=True
    
