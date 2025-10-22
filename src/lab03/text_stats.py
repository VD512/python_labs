import sys

'''импортируем созданные ранее функции'''
from src.lib.text import normalize, tokenize, count_freq, top_n


'''функция считает слова, их частоты и выводит топ'''
def top_of_words(*, table: bool = True):
    '''читаем текст до EOF'''
    text = sys.stdin.read()
    '''проверяем текст на пустоту'''
    if text=='':
        return 'пустой текст'
    '''приводим текст в нормальный вид, разбиваем на слова и считаем их частоты'''
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    word_counts = count_freq(tokens)
    top = top_n(word_counts,5)
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(set(tokens))}")
    '''выводим топ слов красивой табличкой'''
    if table:
        max_len=max(len(x) for x,y in top)
        if max_len<5:
            max_len=5
        first_line='слово'+' '*(max_len-5)+'| частота'
        print(first_line)
        print('-'*len(first_line))
        for word, count in top:
            print(f'{word}'+' '*(max_len-len(word))+f'| {count}')
    else:
        print("Топ-5:")
        for word, count in top:
            print(f"{word}:{count}")
    return None

top_of_words()