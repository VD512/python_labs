### Задание A

``` python
import pytest #библиотека pytest для создания и запуска тестов
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize( #параметризация для запуска одного теста с разными наборами данных
    "source, expected", #параметры: source - входной текст, expected - что должно получиться
    [
        ("ПрИвЕт\nМИр\t", "привет мир"), #разлиные тест-кейсы
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
    ],
)
def test_normalize_basic(source, expected):
    '''функция теста для normalize, берет данные из параметризации'''
    assert normalize(source) == expected #проверяем что normalize(source) возвращает expected


@pytest.mark.parametrize( #параметризация для запуска одного теста с разными наборами данных
    "source,expected", #параметры: source - входной текст, expected - что должно получиться
    [
        ("привет мир", ["привет", "мир"]), #разлиные тест-кейсы
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
    ],
)
def test_tokenize_basic(source, expected):
    '''функция теста для tokenize, берет данные из параметризации'''
    assert tokenize(source) == expected #проверяем что tokenize(source) возвращает expected


def test_count_freq_and_top_n():
    '''тест проверяет вместе функции count_freq и top_n'''
    tokens = ["a", "b", "a", "c", "b", "a"]
    freq = count_freq(tokens)
    assert freq == {"a": 3, "b": 2, "c": 1} #обычный
    assert top_n(freq, 2) == [("a", 3), ("b", 2)] # обычный
    assert top_n(freq, 0) == [] #n=0
    assert top_n(freq, 5) == [("a", 3), ("b", 2), ("c", 1)] #n > количество элементов словаря
    assert count_freq([]) == {} #пустой список
    assert top_n({}, 5) == [] #пустой словарь


def test_top_n_tie_breaker():
    '''тест проверяет top_n с одинаковыми частотами'''
    freq = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(freq, 3) == [("aa", 2), ("bb", 2), ("cc", 1)]

```

### Задание B

``` python
import json, csv
from pathlib import Path
import pytest #библиотека pytest для создания и запуска тестов
from src.lab05.json_csv import json_to_csv, csv_to_json


def write_json(path: Path, obj): #вспомогательная функция для записи JSON файла
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def read_csv_rows(path: Path): #вспомогательная функция для чтения CSV файла
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_json_to_csv_roundtrip(tmp_path: Path):
    '''тест конвертации из JSON в CSV'''
    src = tmp_path / "people.json" #создаем временный путь к исходному JSON файлу
    dst = tmp_path / "people.csv"  #создаем временный путь к целевому CSV файлу
    data = [ #тестовые данные - список словарей
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    write_json(src, data) #записываем тестовые данные в JSON файл
    json_to_csv(str(src), str(dst)) #вызов тестируемой функции
    rows = read_csv_rows(dst) #читаем результат CSV файла
    assert len(rows) == 2 #проверяем что в CSV 2 строки данных
    assert set(rows[0]) >= {"name", "age"} #проверяем что в первой строке есть заголовки


def test_csv_to_json_roundtrip(tmp_path: Path):
    '''тест конвертации из CSV в JSON'''
    src = tmp_path / "people.csv" #создаем временный путь к исходному CSV файлу
    dst = tmp_path / "people.json" #создаем временный путь к целевому JSON файлу
    src.write_text("name,age\nAlice,22\nBob,25\n", encoding="utf-8") #cоздаем CSV файл вручную как текст

    csv_to_json(str(src), str(dst)) #вызов тестируемой функции
    obj = json.loads(dst.read_text(encoding="utf-8")) #читаем результат JSON файла
    assert isinstance(obj, list) #результат должен быть списком
    assert len(obj) == 2 #в списке должно быть 2 элемента
    assert set(obj[0]) == {"name", "age"} #у первого элемента должны быть ключи "name" и "age"


def test_json_to_csv_empty_file(tmp_path: Path):
    '''Тест: пустой JSON файл должен вызывать ошибку'''
    src = tmp_path / "empty.json" #cоздаем путь к пустому JSON файлу
    dst = tmp_path / "output.csv" #cоздаем путь к целевому CSV файлу

    src.write_text("", encoding="utf-8") #cоздаем пустой файл

    with pytest.raises(ValueError): 
        json_to_csv(str(src), str(dst)) #функция json_to_csv должна выбросить ValueError


def test_csv_to_json_empty_file(tmp_path: Path):
    '''Тест: пустой CSV файл должен вызывать ошибку'''
    src = tmp_path / "empty.csv" #cоздаем путь к пустому CSV файлу
    dst = tmp_path / "output.json" #cоздаем путь к целевому JSON файлу


    src.write_text("", encoding="utf-8") #cоздаем пустой CSV файл

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst)) #функция csv_to_json должна выбросить ValueError


def test_csv_to_json_only_headers(tmp_path: Path):
    '''Тест: CSV только с заголовками должен вызывать ошибку'''
    src = tmp_path / "headers_only.csv"  #CSV файл только с заголовками
    dst = tmp_path / "output.json" #целевой JSON файл

    src.write_text("name,age\n", encoding="utf-8")  #cоздаем CSV файл ТОЛЬКО с заголовком "name,age" и переносом строки

    with pytest.raises(ValueError): 
        csv_to_json(str(src), str(dst)) #функция csv_to_json должна выбросить ValueError


def test_missing_csv_raises():
    '''Тест: несуществующий CSV файл должен вызывать FileNotFoundError'''
    with pytest.raises(FileNotFoundError):
        csv_to_json("nope.csv", "out.json") #функция csv_to_json должна выбросить FileNotFoundError


def test_missing_json_raises():
    '''Тест: несуществующий JSON файл должен вызывать FileNotFoundError'''
    with pytest.raises(FileNotFoundError):
        json_to_csv("nope.json", "out.csv") #функция json_to_csv должна выбросить FileNotFoundError

```
![Картинка 1](./images/lab07/pytest.png)
![Картинка 2](./images/lab07/black.png)
