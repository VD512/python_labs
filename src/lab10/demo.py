from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList


def main1():
    stack = Stack()

    print("Добавление элемента в стек:")

    for i in range(3, 0, -1):
        stack.push(i)
        print(stack)

    print(f"\nКоличество эл-ов в стеке: {len(stack)}")
    print()

    top_element = stack.peek()
    print(f"Верхний элемент (peek): {top_element}")
    print()

    print("Извлекаем элементы из стека:")

    while not stack.is_empty():
        popped = stack.pop()
        print(f"извлечено: '{popped}', осталось: {stack}")

    print()
    print(f"Стек пуст: {stack.is_empty()}")


def main2():
    queue = Queue()
    print("Добавляем элементы в очередь:")

    for i in range(3, 0, -1):
        queue.enqueue(i)
        print(queue)

    print()

    first_element = queue.peek()
    print(f"Первый элемент (peek): {first_element}")
    print()

    print("Обрабатываем элементы из очереди:")

    while not queue.is_empty():
        item = queue.dequeue()
        print(f"взяли: '{item}', осталось: {queue}")

    print()
    print(f"Очередь пуста: {queue.is_empty()}")


def main3():
    lst = SinglyLinkedList()

    print("\n1. Добавляем элементы в список:")
    lst.append("яблоко")
    lst.append("банан")
    lst.append("апельсин")
    print(f"   Список: {lst}")

    print("\n2. Добавляем 'виноград' в начало:")
    lst.prepend("виноград")
    print(f"   Список: {lst}")

    print("\n3. Вставляем 'груша' после первого элемента:")
    lst.insert(2, "груша")
    print(f"   Список: {lst}")

    print("\n4. Итерируемся по списку:")
    for fruit in lst:
        print(f"   - {fruit}")

    print("\n5. Удаляем 'груша':")
    lst.remove("груша")
    print(f"   Удалили. Теперь список: {lst}")

    print("\n6. Список элементов:")
    for fruit in lst:
        print(f"   - {fruit}")

    print(f"\n7. Размер списка: {len(lst)} элемента ")

    print(f"\n8. Строковое представление: {lst}")


if __name__ == "__main__":
    main1()
    main2()
    main3()
