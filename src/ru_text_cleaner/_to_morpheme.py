from src.ru_text_cleaner import *


def text_to_morphems(self, text: str) -> str:
    morph = pymorphy2.MorphAnalyzer(lang='ru')
    mor = ''
    for i in text.split(' '):
        mor += morph.parse(i)[0].normal_form
        mor += ' '
    return mor
