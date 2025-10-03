'''форматирует данные студента из кортежа в строку'''
def format_record(rec: tuple[str, str, float]) -> str:
    '''проверяем кортеж на наличие всех трех данных, если нет - ошибка'''
    if len(rec)!=3:
        return ValueError
    '''проверяем является ли первый элемент строкой, если нет - ошибка'''
    if isinstance(rec[0],str):
        full_name=rec[0].strip().split()
        '''проверяем наличие 2 или 3 слов в имени и форматирую , в иных случаях - ошибка'''
        if len(full_name)==3: 
            initials=f'{full_name[0][0].upper()}{full_name[0][1:]} {full_name[1][0].upper()}.{full_name[2][0].upper()}.'
        elif len(full_name)==2:
            initials=f'{full_name[0][0].upper()}{full_name[0][1:]} {full_name[1][0].upper()}.'
        else:
            return ValueError
    else:
        return TypeError
    
    '''проверяем является ли второй элемент строкой, если нет - ошибка'''
    if isinstance(rec[1],str):
        group=rec[1].strip()
        '''проверяем наличие группы, при отсутствии - ошибка'''
        if len(group)==0:
            return ValueError
    else:
        return TypeError

    gpa=rec[2]
    '''проверяем, принадлежит ли GPA типу float, если нет - ошибка'''
    if not isinstance(gpa,float):
        return TypeError
    
    '''записываем все отформатированные данные в одну строку'''
    result=f'{initials}, гр. {group}, GPA {gpa:.2f}'
    return result