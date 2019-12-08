import networkx as nx
import numpy as np
from nltk.cluster.util import cosine_distance

# build similarity matrix
def _similarity_matrix(sentences):
    # Create an empty  matrix
    sim_matrix = np.zeros((len(sentences), len(sentences)))

    for sent1 in range(len(sentences)):
        for sent2 in range(len(sentences)):
            if sent1 != sent2:  # ignore if both are same sentences
                sim_matrix[sent1][sent2] = _find_sentence_sim(sentences[sent1], sentences[sent2])

    return sim_matrix

# Rank sentences based on similarity_matrix
def rank_sentences(lines):
    summarize_text = []

    sim_matrix = _similarity_matrix(lines)
    scores = nx.pagerank(nx.from_numpy_array(sim_matrix))

    #sort sentences based on ranking
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(lines)), reverse=True)

    for i in range(len(lines)):
        summarize_text.append(ranked_sentences[i][1])
    print("\n\n".join(summarize_text))

def _find_sentence_sim(sentence1, sentence2):

    list_all_words = list(set(sentence1 + sentence2))
    sentence_vector1 = [0] * len(list_all_words)
    sentence_vector2 = [0] * len(list_all_words)

    # build the vector for the first sentence
    for word in sentence1:
        sentence_vector1[list_all_words.index(word)] += 1
    
    # build the vector for the second sentence
    for word in sentence2:
        sentence_vector2[list_all_words.index(word)] += 1
    
    return 1 - cosine_distance(sentence_vector1, sentence_vector2)