# Задача N51. Напишите функцию same_by(characteristic, objects), которая проверяет, 
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, 
# если это так. Если значение характеристики для разных объектов отличается - то False. 
# Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - 
# это функция, которая принимает объект и вычисляет его характеристику.
# Ввод:                                      Вывод:
# values = [0, 2, 10, 6]                     same 
# if same_by(lambda x: x % 2, values):
#     print(‘same’) 
# else:
#     print(‘different’)
          

def same_by(characteristic, objects):
    result = []
    for obj in objects:
        result.append(characteristic(obj))
    return not all(result)


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same') 
else:
    print('different')

# С делением на 3
def same_by(characteristic, objects):
    result = []
    for obj in objects:
        result.append(characteristic(obj))
    return not all(result)


values = [0, 3, 9, 6]
if same_by(lambda x: x % 3, values):
    print('same') 
else:
    print('different')
