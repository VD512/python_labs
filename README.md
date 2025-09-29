## Лабораторная работа 1
### Задание 1
```python
name=input('Имя:')
age=int(input('Возраст:'))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```
![Картинка 1](./images/lab01/01_greeting.png)

### Задание 2
```python
a=float(input("a:").replace(',','.'))
b=float(input('b:').replace(',','.'))
print(f'sum={round(a+b,2)}; avg={round((a+b)/2,2)}')
```
![Картинка 2](./images/lab01/02_sum_avg.png)

### Задание 3
```python
price,discount,vat=map(float,input().split())
base=price*(1-discount/100)
vat_amount=base*(vat/100)
total=base+vat_amount
print(f'База после скидки: {base:.2f} P')
print(f'НДС: {vat_amount:.2f} P')
print(f'Итого к оплате: {total:.2f} P')
```
![Картинка 3](./images/lab01/03_discount_vat.png)

### Задание 4
```python
m=int(input())
hours,minutes=m//60,m%60
print(f'{hours}:{minutes:02d}')
```
![Картинка 4](./images/lab01/04_minutes_to_hhmm.png)

### Задание 5
```python
name=input('ФИО:')
fio=name.split()
initials=[x[0].upper() for x in fio]
print(f'Инициалы: {''.join(initials)}.')
print(f'Длина (символов): {len(name.replace(' ',''))+2}')
```
![Картинка 5](./images/lab01/05_initials_and_len.png)

### Задание 6
```python
n=int(input('Количество человек: '))
k_t=0
k_f=0
for x in range(n):
    info=input('')
    surname,name,age,tf=info.split()
    if tf=='True':
        k_t+=1
    if tf=='False':
        k_f+=1
print(k_t, k_f)
```
![Картинка 6](./images/lab01/06_n_people.png)

## Лабораторная работа 2
### Задание 1
```python
'''возвращает кортеж с минимальным и максимальным значениями списка'''
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    '''проверяем список на наличие элементов'''
    if len(nums)==0:
        return ValueError
    mx=-float('inf')
    mn=float('inf')
    for x in nums:
        if x>mx:
            mx=x
        if x<mn:
            mn=x
    return(mn,mx)
```
![Картинка 1](./images/lab02/min_max.png)

```python
'''возвращает отсортированный список уникальных значений'''
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))
```
![Картинка 2](./images/lab02/unique_sorted.png)

```python
'''расплющивает список списков/кортежей в один список по строкам'''
def flatten(mat: list[list | tuple]) -> list:
    res=[]
    for x in mat:
        '''проверяем тип элементов матрицы, если не список или кортеж - ошибка '''
        if not isinstance(x,(list,tuple)):
            return TypeError
        for y in x:
            res.append(y)
    return res        
```
![Картинка 3](./images/lab02/flatten.png)

## Задание 2

```python
'''меняет строки и столбцы местами'''
def transpose(mat: list[list[float | int]]) -> list[list]:
    '''если матрица нулевая - остается без изменений'''
    if len(mat)==0:
        return mat
    len_line=len(mat[0])
    len_column=len(mat)
    '''проверяю матрицу на прямоугольность'''
    for line in mat:
        if len(line)!=len_line:
            return ValueError
    '''создаю новую матрицу, меняя количество строк и столбцов'''
    new_mat=[[0 for x in range(len_column)] for y in range(len_line)]
    '''добавляю в новую матрицу значения оригинальной'''
    for x in range(len_column):
        for y in range(len_line):
            new_mat[y][x]=mat[x][y]
    return new_mat
```
![Картинка 4](./images/lab02/transpose.png)

```python
'''считает сумму по каждой строке'''
def row_sums(mat: list[list[float | int]]) -> list[float]:
    same_len=len(mat[0])
    sum_mat=[]
    '''проверяем матрицу на прямоугольность и записываю суммы строк в отдельный список'''
    for line in mat:
        if len(line)!=same_len:
            return ValueError
        sum_mat.append(sum(line))
    return sum_mat
```
![Картинка 5](./images/lab02/row_sums.png)

```python
'''считает сумму по каждому столбцу'''
def col_sums(mat: list[list[float | int]]) -> list[float]:
    same_len=len(mat[0])
    sum_mat=[0]*same_len
    '''проверяем матрицу на прямоугольность'''
    for line in mat:
        if len(line)!=same_len:
            return ValueError
    '''суммирую элементы по столбцам и записываю суммы в отдельный список'''
    for x in range(same_len):
        for y in range(len(mat)):
            sum_mat[x]+=mat[y][x]
    return sum_mat
```
![Картинка 6](./images/lab02/col_sums.png)

## Задание 3

```python
'''форматирует данные студента из кортежа в строку'''
def format_record(rec: tuple[str, str, float]) -> str:
    full_name=rec[0].strip().split()
    '''проверяем наличие 2 или 3 слов в имени и форматирую , в иных случаях - ошибка'''
    if len(full_name)==3: 
        initials=f'{full_name[0][0].upper()}{full_name[0][1:]} {full_name[1][0].upper()}.{full_name[2][0].upper()}.'
    elif len(full_name)==2:
        initials=f'{full_name[0][0].upper()}{full_name[0][1:]} {full_name[1][0].upper()}.'
    else:
        return ValueError
    
    group=rec[1].strip()
    '''проверяем наличие группы, при отсутствии - ошибка'''
    if len(group)==0:
        return ValueError

    gpa=rec[2]
    '''проверяем, принадлежит ли GPA типу float, если нет - ошибка'''
    if not isinstance(gpa,float):
        return TypeError
    
    '''записываем все отформатированные данные в одну строку'''
    result=f'{initials}, гр. {group}, GPA {gpa:.2f}'
    return result
```
![Картинка 7](./images/lab02/format_record.png)
