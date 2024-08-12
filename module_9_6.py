#  Домашнее задание по теме "Генераторы"
# Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.

def all_variants(text):
    if not text:
        yield ""  # Если text пустая строка то возвращаем пустую строку
    else:
        for var in all_variants(text[1:]):  # Генерируем все подварианты для строки text[1:]
            # (т.е. строки без первого символа)
            yield var
            yield text[0] + var


a = all_variants("abc")
for i in a:
    print(i)
