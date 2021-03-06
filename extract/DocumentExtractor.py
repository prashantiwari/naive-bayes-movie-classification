import numpy as np
import re

# assumption: we are working with a document
from extract.Tokenizer import Tokenizer


class DocumentExtractor():

    # def __init__(self, doc_generator, wordSplit):
    #     self._generator = doc_generator
    #     self._tokenizer = Tokenizer()

    # Data type for each, will assume an np array
    def bag_of_words_term_freq(self, vocab, doc_tokens):
        term_freq_in_doc_vector = np.zeros(len(vocab))
        # term_freq_in_doc_vector = [0]*len(vocab)

        # assume vocab is constant?
        for term in doc_tokens:
            if term in vocab:
                index_in_vocab = np.where(vocab == term)
                term_freq_in_doc_vector[index_in_vocab] += 1
            # TODO: What if term is not in vocab, then perform laplace smoothing
            # else:
            #     term_freq_vector[term] += 1
        return term_freq_in_doc_vector

    def bag_of_words_term_freq_dict(self, vocab, doc_tokens):
        # term_freq_in_doc_vector = np.zeros(len(vocab))
        term_freq_in_doc_dict = dict.fromkeys(vocab, 0)

        # assume vocab is constant?
        for term in doc_tokens:
            if term in vocab:
                term_freq_in_doc_dict[term] += 1
            # TODO: What if term is not in vocab, then perform laplace smoothing
            # else:
            #     term_freq_vector[term] += 1
        return term_freq_in_doc_dict.values()

    def bag_of_words_term_freq_set(self, vocab, doc_tokens):
        # term_freq_in_doc_vector = np.zeros(len(vocab))
        term_freq_in_doc_dict = [0] * len(vocab)

        # assume vocab is constant?
        for term in doc_tokens:
            if term in vocab:
                term_freq_in_doc_dict[vocab.index(term)] += 1
                # TODO: What if term is not in vocab, then perform laplace smoothing
                # else:
                #     term_freq_vector[term] += 1
        return term_freq_in_doc_dict

    # def extract_term_counts_with_generator(self):
    #     for doc in self._generator:
    #         self.extract_term_counts(doc)

    @staticmethod
    def extract_term_counts(term, doc):
        tokens = Tokenizer().tokenize_sentence(doc)
        normalizedTerm = term
        tf_in_doc = tokens.count(normalizedTerm)
        return term, tf_in_doc, len(tokens)

    @staticmethod
    def count_terms(doc):
        tokens = Tokenizer().tokenize_sentence(doc)
        return len(tokens)

    @staticmethod
    def count_unique_terms(doc):
        tokens = set(Tokenizer().tokenize_sentence(doc))
        return len(tokens)

# if __name__ == "__main__":