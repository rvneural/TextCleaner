from TextCleaner import *


def clean_stopwords(self, text: str) -> str:
    stop_words = set(stopwords.words('russian'))
    words = text.split(' ')
    answer = ''
    for word in words:
        answer += word if word not in stop_words else ''
        answer += ' '

    return answer.strip()
