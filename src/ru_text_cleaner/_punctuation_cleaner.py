from . import *


def clean_punctuation(self, text: str) -> str:
    """
    Метод clean_puctuation убирает все знаки припинания из текста

    return ''.join(i for i in text if i not in string.punctuation) - возвращает текст без пунктуационных знаков 
    """
    return ''.join(i for i in text if i not in string.punctuation)

