import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.cli import download
from string import punctuation
from heapq import nlargest


def text_summarizer(text: str, percentage: float) -> str:
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    tokens = [token.text for token in doc if token.text not in punctuation and token.text not in STOP_WORDS]
    freq_of_word = dict()
    
    for word in doc:
        
        if word.text not in freq_of_word.keys():
            freq_of_word[word.text] = 1
        else:
            freq_of_word[word.text] += 1
                    
    max_freq = max(freq_of_word.values())
    
    for word in freq_of_word.keys():
        freq_of_word[word] = freq_of_word[word] / max_freq
        
    sent_tokens = [sent for sent in doc.sents]
    sent_order = {str(sent): i for sent, i in zip(sent_tokens, range(len(sent_tokens)))}
    sent_scores = dict()
    for sent in sent_tokens:
        for word in sent:
            if word.text.lower() in freq_of_word.keys():
                if sent not in sent_scores.keys():                            
                    sent_scores[sent] = freq_of_word[word.text.lower()]
                else:
                    sent_scores[sent] += freq_of_word[word.text.lower()]
    
    len_tokens = int(len(sent_tokens)*percentage)
    summary = nlargest(n=len_tokens, iterable=sent_scores, key=sent_scores.get)
    final_summary = [str(word) for word in summary]
    final_summary.sort(key=lambda x: sent_order.get(x))
    return ' '.join(final_summary)
