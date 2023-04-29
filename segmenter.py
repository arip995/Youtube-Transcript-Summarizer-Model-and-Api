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
    for token in doc:
        if token.pos_ in ['PUNCT']:
            return text

    for i in range(1, len(doc) - 1):
        buff.append(doc[i].text.title() if doc[i].pos_ in ['PROPN'] else doc[i].text)
        # print(buff)
        if doc[i + 1].pos_ in ['PRON', 'PROPN']:
            res.append(' '.join(buff)[0].upper() + ' '.join(buff)[1:])
            buff.clear()

    buff.append(str(doc[-1]))
    res.append(' '.join(buff))

    return ". ".join(filter(f_func, res)) + "."
