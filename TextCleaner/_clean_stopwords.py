from TextCleaner import *


def clean_stopwords(self, text: str, language: str) -> str:
    stop_words = set(stopwords.words(language))
    words = text.split(' ')
    answer = ''
    for word in words:
        answer += word if word not in stop_words else ''
        answer += ' '

    return answer.strip()
