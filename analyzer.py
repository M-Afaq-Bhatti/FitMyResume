import spacy
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

def calculate_similarity(resume_text, job_desc_text):
    texts = [preprocess(resume_text), preprocess(job_desc_text)]
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform(texts)
    sim_score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return sim_score
