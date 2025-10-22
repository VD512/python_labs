from re import *
'''функция приводит строки в "нормальный" вид'''
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        '''приводим к нижнему регистру'''
        text=text.casefold()
    if yo2e:
        '''заменяем ё на е'''
        text=text.replace('ё','е').replace('Ё','Е')
    '''убираем управляющие символы'''
    text=text.replace('/t',' ').replace('/r',' ').replace('/n',' ')
    '''убираем лишние пробелы'''
    text=' '.join(text.split())
    return (text)

'''функция разбивает строчки на "слова"'''
def tokenize(text: str) -> list[str]:
    '''шаблон для нужных нам подстрок'''
    pattern=r'\w+(?:-\w+)*'
    rez=findall(pattern,text)
    return rez

'''функция создает словарь частот'''
def count_freq(tokens: list[str]) -> dict[str, int]:
    rez={}
    for words in tokens:
        rez[words]=rez.get(words,0)+1
    return rez

'''функция создает топ n частот'''
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    dict_items=list(freq.items())
    '''создаем список сортированный по второму значению'''
    sorted_items=sorted([[-items[1],items[0]]for items in dict_items])
    rez=[]
    '''возвращаем значения на свое место'''
    for items in sorted_items:
        rez.append(((items[1],-items[0])))
    return rez[:n]
