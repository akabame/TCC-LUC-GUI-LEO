import os
from datetime import datetime
from gensim.models import Word2Vec
from scipy.stats import norm
#from numpy import dot
from tqdm import tqdm

dir_path = os.path.dirname(__file__)
#txts = dir_path + '\\scrap_text\\scrap_text'
#txts = 'C:\\Users\\Lucas\\Desktop\\bullshitices\\scrap_text\\scrap_text'
txts = 'C:\\Users\\Lucas\\Desktop\\bullshitices\\bullshittext'
corpus = []
texto = []
linha = []
replaces = ['(',')','{','}','"',':',';',"'",'\n','”','“','.',',','\xa0','\u2061']
now = datetime.now()
for filename in tqdm(os.listdir(txts),'loading'):
    if filename == 'scrap_text':
        pass
    vet = []
    file = open(txts+'\\'+filename, 'r+',encoding='utf-16')
    read_file = file.read()
    file.close()
    text = read_file
    for rep in replaces:
        text = text.replace(rep,' ').lower()
    fim = text.split(' ')
    for word in range(len(fim)):            
        fim[word] = fim[word].split('[')[0].split('\\')[0].split(' ')[0]
        if fim[word] != '':
            vet.append(fim[word])
    corpus.append(vet)
    
print('dicionario duração: '+ str(datetime.now()-now))

now = datetime.now()
#parametros (corpo vetorizado,min_count = 5 ou 3(pesado), size = 500, workers = processos,window = 5 ,sg = 1 -> algoritmo)
#tqdm    
model = Word2Vec(corpus, min_count=5,size= 500,workers=4, window =3, sg = 1)
model.save('w2v_model')
print('w2v modelo duração: '+ str(datetime.now()-now))



