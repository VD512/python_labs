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

'''возвращает отсортированный список уникальных значений'''
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

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