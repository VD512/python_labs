from src.lab08.models import Student
from src.lab09.group import Group


def main():
    group = Group("data/lab09/students.csv")

    print("Список всех студентов:")
    students = group.list()
    for student in students:
        print(student)
    print()
    print("Добавление новеньких:")
    new_students = [
        ("Федорова Ольга", "2002-09-08", "БИВТ-20-2", 4.9),
        ("Лебедев Сергей", "2004-04-12", "БИВТ-22-3", 4.0),
        ("Григорьева Татьяна", "2003-12-30", "БИВТ-21-1", 4.6),
    ]

    for fio, date, grp, gpa in new_students:
        student = Student(fio, date, grp, gpa)
        group.add(student)
        print(f"Добавлен: {fio}")
    print()
    print("Список с новенькими:")
    students = group.list()
    for student in students:
        print(student)
    print()
    print("Поиск всех, кто Иван и тд:")
    found_students = group.find("Иван")
    for s in found_students:
        print(s)
    print()
    print("Отчисление:")
    group.remove("Сидоров Алексей")
    print("Сидоров Алексей отчислен")
    print()

    print("Обновление информации о студенте:")
    if group.update("Васильев Дмитрий", gpa=5.0, group="БИВТ-20-2"):
        print("Данные обновлены")
    print()
    print("Окончательный список студентов:")
    students = group.list()
    for s in students:
        print(s)


if __name__ == "__main__":
    main()
