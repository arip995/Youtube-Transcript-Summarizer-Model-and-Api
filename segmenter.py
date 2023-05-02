import spacy
from typing import List


def f_func(data: str) -> bool:
    if len(data.split()) not in [1, 2]:
        return True
    return False


def split_sentences(text: str) -> str:
    nlp = spacy.load('en_core_web_sm')
    buff: List[str] = list()
    res: List[str] = list()
    doc = nlp(text.ljust(len(text) + 1, " ").rjust(len(text) + 2, " "))
    for token in doc.sents:
        if len(token) == len(doc):
            return text
        
    for i in range(1, len(doc) - 1):
        buff.append(doc[i].text.title() if doc[i].pos_ in ['PROPN'] else doc[i].text)   # noqa: E501
        # print(buff)
        if doc[i + 1].pos_ == 'PRON':
            if doc[i].pos_ in ['SCONJ', 'AUX', 'ADP']:
                continue
            res.append(' '.join(buff)[0].upper() + ' '.join(buff)[1:])
            buff.clear()
        
        elif doc[i + 1].pos_ == 'PROPN':
            if doc[i].pos_ in ['CCONJ', 'SCONJ', 'AUX', 'ADP']:
                continue
            res.append(' '.join(buff)[0].upper() + ' '.join(buff)[1:])
            buff.clear()
        
        elif doc[i + 1].pos_ == 'ADP':
            if doc[i].pos_ in ['SCONJ', 'CCONJ', 'VERB', 'ADJ', 'NOUN']:
                continue
            res.append(' '.join(buff)[0].upper() + ' '.join(buff)[1:])
            buff.clear()
        
        elif doc[i + 1].pos_ == 'ADJ':
            if doc[i].pos_ in ['SCONJ', 'CCONJ', 'VERB']:
                continue
            res.append(' '.join(buff)[0].upper() + ' '.join(buff)[1:])
            buff.clear()
        
        elif doc[i + 1].pos_ in ['PART', 'NUM']:
            continue

    buff.append(str(doc[-1]))
    res.append(' '.join(buff)[0].upper() + ' '.join(buff)[1:])

    return ". ".join(filter(f_func, res)) + "."
