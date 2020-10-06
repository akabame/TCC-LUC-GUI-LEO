import pandas as pd
dir_path = '/home/tccllb'
urls_lidas = open("{}/todas_urls.txt".format(dir_path),"r", encoding="utf-16")
todas=urls_lidas.readlines()
todas = [sub.replace('\n','') for sub in todas]
df = pd.DataFrame({'Urls':todas})
df=df.drop_duplicates(keep='first')
urls_lidas.close()
urls_lidas = open("{}/ja_lidos.txt".format(dir_path),"r")
urls_lidas = urls_lidas.readlines()
ja_lidos = [sub.replace('\n','') for sub in urls_lidas]
ja_lidos = set(ja_lidos)
urls_lidas = open("{}/todas_urls.txt".format(dir_path),"w", encoding="utf-16")
for i in df['Urls']:
    if i in ja_lidos:
        pass
    else:
        urls_lidas.write(str(i)+"\n")
