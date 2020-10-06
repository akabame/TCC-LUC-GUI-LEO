import os
from datetime import datetime
from gensim.models import Word2Vec
from scipy.stats import norm
from scipy import spatial
import numpy as np
from numpy import dot
from tqdm import tqdm

#carregando modelo w2v
model = Word2Vec.load("w2v_model_ascii")

dir_path = os.path.dirname(__file__)
#txts = dir_path + '\\scrap_text\\scrap_text'
#txts = 'C:\\Users\\Lucas\\Desktop\\bullshitices\\scrap_text\\scrap_text'
txts = '/home/tccllb/backup/scrap_text_ascii'
corpus = []
texto = []
linha = []
replaces = ['(',')','{','}','"',':',';',"'",'\n','”','“','.',',','\xa0','\u2061','!','?']
pfora = 0

for filename in tqdm(os.listdir(txts),'loading'):
    if filename == 'scrap_text':
        pass
    #nome do arquvio e vetor com dimensões
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
                vet = vet + model.wv[fim[word]]
            except:
                pfora = pfora + 1
                pass
    #dividindo vetor pelo numero de palavras
    try:
        for d in range(len(vet)):
            vet[d] = vet[d]/len(fim)
    except Exception as e:
        #print(e)
        continue
    #nome do arquivo
    tupla.append(filename[:-4])
    #vetor de dimensões
    tupla.append(vet)
    #documentos -> nome e vetor
    corpus.append(tupla)

nparray = np.array(corpus,dtype=object)
np.save('w2v_array',nparray)
#no load, adicionar parâmetro allow_pickle=True
    
