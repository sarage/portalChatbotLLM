from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class Retriever:

    def __init__(self, path='data/docs.txt'):
        self.model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
        with open(path, encoding='utf-8') as f:
            self.docs = [x.strip() for x in f.read().split('\n\n') if x.strip()]
        self.index = self._build_index()

    def _build_index(self):
        embeddings = self.model.encode(self.docs)
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(np.array(embeddings))
        return index

    def search(self, query, k=3):
        q_vec = self.model.encode([query])
        D, I = self.index.search(np.array(q_vec), k)
        return [self.docs[i] for i in I[0]]
