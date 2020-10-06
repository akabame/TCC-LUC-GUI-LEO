from gensim.models import Word2Vec
model = Word2Vec.load('w2v_model')
print(len(model.wv.vocab))
