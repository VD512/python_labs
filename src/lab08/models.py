from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        """Валидация даты рождения и среднего балла"""
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                f"Некорректная дата рождения. Ожидаемый формат: ГГГГ-ММ-ДД"
            )

        if not (0 <= self.gpa <= 5):
            raise ValueError(f"Некорректный средний балл. Ожидаемый диапазон: 0-5")

    def age(self) -> int:
        """Вычисление возраста в полных годах"""

        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth_date.year

        if today.month < birth_date.month or (
            today.month == birth_date.month and today.day < birth_date.day
        ):
            age -= 1
        return age

    def to_dict(self) -> dict:
        """Сериализация (запись информации о человеке в словарь)"""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        """Десериализация (запись информации о человеке из словаря)"""
        return cls(
            fio=d["fio"], birthdate=d["birthdate"], group=d["group"], gpa=d["gpa"]
        )

    def __str__(self):
        """Красивый вывод в строчку информации о человеке"""
        return f"Student: {self.fio}, Group: {self.group}, GPA: {self.gpa}, Age: {self.age()}"
