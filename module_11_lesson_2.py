"""
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).

"""
import inspect

from idna import intranges_contain


def introspection_info(obj):

    itog = {}

    itog['type'] = type(obj).__name__
    itog['attributes'] = []
    itog['methods'] = []

    for name in dir(obj):
        if not callable(getattr(obj, name)):
            itog['attributes'].append(name)
        else:
            itog['methods'].append(name)

    obj_module = inspect.getmodule(obj)

    if obj_module is None:
        itog['module'] = __name__
    else:
        itog['module'] = obj_module.__name__


    return itog

number_info = introspection_info(42)
print(number_info)

str_info = introspection_info('My string')
print(str_info)

func_info = introspection_info(abs)
print(func_info)