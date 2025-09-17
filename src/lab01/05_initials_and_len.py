name=input('ФИО:')
n1,n2,n3=name.split()
print(f'Инициалы: {n1[0]+n2[0]+n3[0]}.')
print(f'Длина (символов): {len(name)}')