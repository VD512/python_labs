## Лабораторная работа 10

## Стек (Stack)

Стек — это структура данных, работающая по принципу "последним пришёл — первым вышел" (LIFO, Last In First Out). Представляет собой список элементов, организованных по принципу LIFO.

# Основные операции:
push(item) — добавить элемент на вершину стека — O(1)
pop() — извлечь верхний элемент — O(1)
peek() — посмотреть верхний элемент без извлечения — O(1)
is_empty() — проверить, пуст ли стек — O(1)

# Применение:
Рекурсивные вызовы функций
Отмена операций (undo)

## Очередь (Queue)

Очередь — это структура данных, работающая по принципу "первым пришёл — первым вышел" (FIFO, First In First Out). Представляет собой список элементов, организованных по принципу FIFO.

# Основные операции:
enqueue(item) — добавить элемент в конец очереди — O(1)
dequeue() — извлечь первый элемент — O(1)
peek() — посмотреть первый элемент без извлечения — O(1)
is_empty() — проверить, пуста ли очередь — O(1)

# Применение:
Планирование задач
Обработка запросов
Алгоритмы обхода графов

## Связный список (Linked List)

Связный список — это структура данных, состоящая из узлов, каждый из которых содержит данные и ссылку (указатель) на следующий узел в последовательности.

## Односвязный список (Singly Linked List):

Каждый узел содержит данные и указатель на следующий узел
Первый узел называется "головой" (head)
Последний узел указывает на None

# Основные операции:
append(value) — добавить элемент в конец — O(1) (при наличии tail)
prepend(value) — добавить элемент в начало — O(1)
insert(idx, value) — вставить элемент по индексу — O(n)
remove(value) — удалить элемент по значению — O(n)
remove_at(idx) — удалить элемент по индексу — O(n)

# Преимущества:
Динамический размер
Эффективная вставка и удаление в начале — O(1)

# Недостатки:
Доступ к элементу по индексу — O(n)
Дополнительная память на хранение указателей

### Задание А
```python
from collections import deque
from typing import Any


class Stack:
    """Стек (LIFO) на базе list"""

    def __init__(self):
        """Cоздание внутреннего хранилища стека"""
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        """Добавить элемент на вершину стека"""
        self._data.append(item)

    def pop(self) -> Any:
        """Снять верхний элемент стека и вернуть его"""
        if self.is_empty():
            raise IndexError("Невозможно извлечь элемент из пустого стека")
        return self._data.pop()

    def peek(self) -> Any | None:
        """Вернуть верхний элемент без удаления"""
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """Проверить, пуст ли стек"""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Вернуть количество элементов в стеке"""
        return len(self._data)


class Queue:
    """Очередь (FIFO) на базе collections.deque."""

    def __init__(self):
        """Инициализация пустой очереди"""
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Добавить элемент в конец очереди"""
        self._data.append(item)

    def dequeue(self) -> Any:
        """Взять элемент из начала очереди и вернуть его"""
        if self.is_empty():
            raise IndexError("Невозможно извлечь элемент из пустой очереди")
        return self._data.popleft()

    def peek(self) -> Any | None:
        """Вернуть первый элемент без удаления"""
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """Проверить, пуста ли очередь"""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Вернуть количество элементов в очереди"""
        return len(self._data)

```
![Картинка 1](C:\Users\dasha\Desktop\python_labs\images\lab10\stack.png)
![Картинка 2](C:\Users\dasha\Desktop\python_labs\images\lab10\queue.png)

### Задание В
```python
from typing import Any


class Node:
    """Узел односвязного списка."""

    def __init__(self, value: Any):
        self.value = value
        self.next: "Node" | None = None


class SinglyLinkedList:
    """Односвязный список."""

    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size = 0

    def append(self, value: Any) -> None:
        """Добавить элемент в конец списка за O(1)."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value: Any) -> None:
        """Добавить элемент в начало списка за O(1)."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        """Вставить элемент по индексу idx."""
        if idx < 0 or idx > self._size:
            raise IndexError("Индекс вне диапазона")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        new_node = Node(value)
        current = self.head
        for _ in range(idx - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def remove_at(self, idx: int) -> None:
        """Удалить элемент по индексу idx."""
        if idx < 0 or idx >= self._size:
            raise IndexError("Индекс вне диапазона")

        if idx == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        node_to_remove = current.next
        current.next = node_to_remove.next

        if node_to_remove == self.tail:
            self.tail = current

        self._size -= 1

    def remove(self, value: Any) -> None:
        """Удалить первое вхождение значения value."""
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return

        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next

        if current.next is not None:
            node_to_remove = current.next
            current.next = node_to_remove.next

            if node_to_remove == self.tail:
                self.tail = current

            self._size -= 1

    def __iter__(self):
        """Возвращает итератор по значениям в списке."""
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        """Возвращает количество элементов."""
        return self._size

    def __repr__(self) -> str:
        """Возвращает строковое представление."""
        values = list(self)
        return f"SinglyLinkedList({values})"

```
![Картинка 3](C:\Users\dasha\Desktop\python_labs\images\lab10\list.png)