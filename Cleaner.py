import spacy
import Distill

try:
    nlp = spacy.load('en_core_web_sm')
except ImportError:
    print("Spacy's English Language Modules aren't present \n Install them by doing \n python -m spacy download en_core_web_sm")

#Takes in text read by the parser file and then does the text cleaning.
def _base_clean(text):
    text = Distill.tokenize(text)
    text = Distill.remove_stopwords(text)
    text = Distill.remove_tags(text)
    text = Distill.lemmatize(text)
    return text

#Takes in text that has been cleaned by the _base_clean and uses set to reduce the repeating words giving only a single word that is needed.
def _reduce_redundancy(text):
    return list(set(text))

#Takes in text and uses Spacy Tags on it, to extract the relevant Noun, Proper Noun words that contain words related to tech and JD.
def _get_target_words(text):
    target = []
    sent = " ".join(text)
    doc = nlp(sent)
    for token in doc:
        if token.tag_ in ['NN', 'NNP']:
            target.append(token.text)
    return target

def Cleaner(text):
    sentence = []
    sentence_cleaned = _base_clean(text)
    sentence.append(sentence_cleaned)
    sentence_reduced = _reduce_redundancy(sentence_cleaned)
    sentence.append(sentence_reduced)
    sentence_targetted = _get_target_words(sentence_reduced)
    sentence.append(sentence_targetted)
    return sentence
