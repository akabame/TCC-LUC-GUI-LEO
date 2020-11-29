import os
import json
from tqdm import tqdm

dir_path = os.path.dirname(__file__)
#txts = dir_path + '\\scrap_text\\scrap_text'
#txts = 'C:\\Users\\Lucas\\Desktop\\bullshitices\\scrap_text\\scrap_text'
txts = '/home/tccllb/backup/scrap_text_total_ascii'
corpus = []
texto = []
linha = []
replaces = ['(',')','{','}','"',':',';',"'",'\n','”','“','.',',','\xa0','\u2061','!','?']
pfora = 0
count_doc = {}

for filename in tqdm(os.listdir(txts),'loading'):
    try:
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
        palavras_existentes = []
        palavra_reps = {}
        for word in range(len(fim)):            
            fim[word] = fim[word].split('[')[0].split('/')[0].split(' ')[0]
            if fim[word] != '':
                try:
                    palavra_reps[fim[word]] = palavra_reps[fim[word]] + 1
                except:
                    palavra_reps[fim[word]] = 1
        count_doc[filename] = palavra_reps
    except Exception as e:
        print(e)
        continue

with open('ocorrencia_local.txt', 'w') as outfile:
    json.dump(count_doc, outfile)
    
