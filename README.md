# RU-TEXT-CLEANER

## Библиотека подготовки русского текста для решения NLP- и иных задач

Основным форматом использования билиотеки является:
```Python
from ru_text_cleaner import TextCleaner

text_cleaner = TextCleaner()

string = 'Какая-то неФорМатИроВаннАЯ строка'

formated_text = text_cleaner.clean_text(string)
```

В этом случае Вы получите следующий результат в переменной `formated_text`:

```Python
какаять неформатированный строка
```
Функция `clean_text()` принимает на вход строку и возвращает строку.

Во время инициатизации объекта класса `TextCleaner()` можно вручную указать, какое конкретно форматирование текста будет производиться:

```Python
spaces=True # убирает многократные пробелы в тексте
punctuation=True # убирает знаки пунктуации в строке
html=True # убирает HTML-теги
emoji=True # убирает эмодзи
lower=True # переводит текст в нижний регистр
stop_words=True # убирает стоп-слова (союзы, предлоги и так далее)
morpheme=True # преобразует слова в их начальные формы (автоматически переводит текст в нижний регистр)
```
_По умолчанию все переменные установлены в значение `True`._

При этом можно отдельно испортировать функции `to_lower_text`, `clean_emoji`, `clean_spaces`, `clean_html`, `clean_punctuation`, `clean_stopwords`, `text_to_morphems` для выборочного форматирования текста. __Но в этом случае корректность полученного результата не гарантируется.__