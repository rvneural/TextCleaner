import string


def clean_punctuation(text: str) -> str:
    """
    Метод clean_puctuation убирает все знаки припинания из текста

    return ''.join(i for i in text if i not in string.punctuation) - возвращает текст без пунктуационных знаков 
    """
    text = text.replace('-', ' ')
    text = text.replace('–', ' ')
    text = text.replace('—', ' ')
    text.replace('«', ' ')
    text.replace('»', ' ')
    return ''.join(i for i in text if i not in string.punctuation)

