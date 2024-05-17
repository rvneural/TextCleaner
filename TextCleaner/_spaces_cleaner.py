from TextCleaner import *


def clean_spaces(self, text: str) -> str:
    return re.sub(r'[ +]', ' ', text)
