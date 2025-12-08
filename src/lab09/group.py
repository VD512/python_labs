import csv
from pathlib import Path
from typing import List, Dict
from src.lab08.models import Student
from src.lab04.io_txt_csv import ensure_parent_dir, write_csv


class Group:
    def __init__(self, storage_path: str):
        """Инициализация группы студентов"""
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self) -> None:
        """Приватный метод: убеждается, что файл хранилища существует.
        Если нет - создает пустой файл с заголовком"""
        if not self.path.exists():
            ensure_parent_dir(self.path)
            write_csv([], self.path, header=("fio", "birthdate", "group", "gpa"))

    def _read_all(self) -> List[Dict[str, str]]:
        """Приватный метод: читает все записи из CSV файла"""
        if not self.path.exists():
            return []

        with self.path.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)

    def _write_all(self, rows: List[Dict[str, str]]) -> None:
        """Приватный метод: записывает все записи в CSV файл"""
        if rows:
            header = tuple(rows[0].keys())
            tuple_rows = [tuple(row.values()) for row in rows]
            write_csv(tuple_rows, self.path, header=header)
        else:
            write_csv([], self.path, header=("fio", "birthdate", "group", "gpa"))

    def list(self) -> List[Student]:
        """Возвращает список всех студентов в группе как объекты Student"""
        rows = self._read_all()
        students = []
        for row in rows:
            try:
                row_copy = row.copy()
                row_copy["gpa"] = float(row_copy["gpa"])
                student = Student.from_dict(row_copy)
                students.append(student)
            except (ValueError, KeyError) as e:
                print(f"Warning: Skipping invalid record: {row}. Error: {e}")
        return students

    def add(self, student: Student) -> None:
        """Добавляет нового студента в группу"""
        rows = self._read_all()

        student_dict = student.to_dict()
        student_dict["gpa"] = str(student_dict["gpa"])
        rows.append(student_dict)
        self._write_all(rows)

    def find(self, substr: str) -> List[Student]:
        """Ищет студентов по подстроке в имени"""
        rows = self.list()
        return [r for r in rows if substr.lower() in r.fio.lower()]

    def remove(self, fio: str) -> None:
        """Удаляет студента по имени"""
        rows = self._read_all()

        rows = [r for r in rows if r["fio"] != fio]

        self._write_all(rows)

    def update(self, fio: str, **fields) -> bool:
        """Обновляет поля студента по имени"""
        rows = self._read_all()
        updated = False

        for row in rows:
            if row["fio"] == fio:
                for key, value in fields.items():
                    if key in row:
                        if key == "gpa":
                            row[key] = str(value)
                        else:
                            row[key] = str(value)
                updated = True
                break

        if updated:
            self._write_all(rows)
        return updated
