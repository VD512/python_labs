## Лабораторная работа 8

### Задание А
```python
from dataclasses import dataclass #декоратор для автоматического создания методов класса
from datetime import datetime, date #классы для работы с датами и временем

#декоратор @dataclass автоматически генерирует методы:
#__init__ - конструктор для создания объектов
#__repr__ - строковое представление для разработчиков
#__eq__ - сравнение объектов по значениям полей
@dataclass
class Student: #создаем класс студент
    #задаем поля класса
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self): #этот метод вызывается автоматически после __init__
        """Валидация даты рождения и среднего балла"""
        try: #пытаемся преобразовать строку с датой в объект datetime
            datetime.strptime(self.birthdate, "%Y-%m-%d") #если формат не соответствует "%Y-%m-%d", вызовется ValueError
        except ValueError:
            raise ValueError(
                f"Некорректная дата рождения. Ожидаемый формат: ГГГГ-ММ-ДД"
            )

        if not (0 <= self.gpa <= 5): #проверяем, что средний балл находится в допустимом диапазоне 0-5
            raise ValueError(f"Некорректный средний балл. Ожидаемый диапазон: 0-5")

    def age(self) -> int:
        """Вычисление возраста в полных годах"""
        #преобразуем строку с датой рождения в объект date
        #datetime.strptime() создает объект datetime из строки по заданному формату
        #.date() преобразует datetime в date (убирает время)
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today() #получаем текущую дату
        age = today.year - birth_date.year #вычисляем разницу в годах
        
        #если день рождения в этом году еще не наступил, вычитаем 1 год
        if today.month < birth_date.month or (
            today.month == birth_date.month and today.day < birth_date.day
        ):
            age -= 1
        return age

    def to_dict(self) -> dict:
        """Сериализация (запись информации о человеке в словарь)"""
        #создаем словарь с данными студента
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod #декоратор, указывающий что это метод класса
    def from_dict(cls, d: dict):
        """Десериализация (запись информации о человеке из словаря)"""
        #создаем новый объект Student, передавая значения из словаря
        return cls(
            fio=d["fio"], birthdate=d["birthdate"], group=d["group"], gpa=d["gpa"]
        )

    def __str__(self):
        """Красивый вывод в строчку информации о человеке"""
        #этот метод вызывается при print(student) или str(student)
        return f"Student: {self.fio}, Group: {self.group}, GPA: {self.gpa}, Age: {self.age()}"

```
![Картинка 1](./images/lab08/class.png)

### Задание B

```python
import json
from typing import List
from models import Student


def students_to_json(students: List[Student], path: str):
    """Сохраняет список студентов в JSON-файл"""
    #преобразуем каждый объект Student в словарь с помощью метода to_dict()
    #получаем список словарей
    data = [student.to_dict() for student in students]
    #открываем файл для записи
    with open(path, "w", encoding="utf-8") as f:
        #записываем данные в JSON файл
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str) -> List[Student]:
    """Читает JSON-файл и создает список студентов"""
    #открываем файл для чтения
    with open(path, "r", encoding="utf-8") as f:
        #читаем и преобразуем JSON данные в список словарей
        data = json.load(f)
    #преобразуем каждый словарь в объект Student с помощью метода from_dict()
    students = [Student.from_dict(item) for item in data]

    return students

```
![Картинка 2](./images/lab08/students_input.png)
![Картинка 3](./images/lab08/students_output.png)
