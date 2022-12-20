"""
GB Программист, "Знакомство с языком Python( семинары)", #2.  

lineup_factorials - выводит последовательный список факториалов.  

lineup_floats - выводит отредактированный список.  

lineup_multiplied - выводит произведение элементов списка.  

shake_lineup - перемешивает список.  

float_sum_signs - выводит сумму цифр рационального числа.  

factorial_recursion - считаем факториал.  

validate_input_float - принимаем от пользователя вещественное число
"""


__all__ = ['factorial_recursion', 'validate_input_float']
__version__ = "#2"
__author__ = "anton6733@gmail.com"


# standart imports
import datetime
import os
import random
import sys
from pathlib import Path
from typing import List, Tuple

# local imports
from homework_sem1 import Break, validate_input


def validate_input_float(
    limits: Tuple[int, int] = (- sys.maxsize, sys.maxsize),
    accepts_zero=False, short_note: str = ""
) -> float:
    """
    Принимаем с клавиатуры вещественное число

    limits - предел допустимых значений (не меньше, не больше)

    accepts_zero - если да - ноль не проходит

    short_note - описание задачи вызова.

    """
    """
    correct - основа костыля TryParse из шарпа.  
    msg - приглашение ко вводу.  
    tmp - буфер для инпута.  
    output - выводное значение.  
    multiplier - костыль для отрицательных инпутов.  
    accepts_zero - если False - ноль не пропускаем.
    separator - приводим разделитель к порядку
    """

    # Была мысль принять float как два инта и потом их соединить, но
    # во-первых возникла проблема сжирания предварительных нулей,
    # во-вторых нужно было обращаться к вопросу разнознаковых частей.
    if short_note:
        print(short_note)
    output: float
    tmp: str
    msg = "Input number?"
    correct = False
    separator = '.'
    while not correct:
        tmp = input(msg)
        multiplier = -1 if tmp.startswith('-') else 1
        tmp = tmp.replace(',', separator)
        tmp = tmp.removeprefix('-')
        one_point = tmp.count(separator) == 1
        if not one_point:
            msg = "better luck next time. Input number."
            continue
        if tmp.startswith(separator):
            tmp = '0'+tmp
        if tmp.endswith(separator):
            tmp += '0'
        try:
            output = float(tmp) * multiplier
        except:
            msg = "Input number?"
            continue
        if output > limits[1] or output < limits[0]:
            msg = f"Between {limits[0]} and {limits[1]-1}. Try again."
        elif not accepts_zero and output == 0:
            msg = " Zero is not accepted. Try again"
        else:
            correct = True
    return output


def float_summarize_signs(number: float) -> int:
    """
    Находим сумму знаков вещественного числа.

    number - число-объект расчёта
    """
    """
    number_strf - приводим число к целому, чтобы потом выделять знаки безо 
    всяких точек.
    output - вывод
    """
    # математическое решение споткнулось о плавающуюююююююююююъй точку.
    output = 0
    number_strf = str(number)
    for char in number_strf:
        if char.isdigit():
            output += int(char)
    return output


def factorial_recursion(base: int) -> int:
    """рекурсивно считаем факториал числа 

    Вызывает ValueError если base < 0

    base - считаем до этого числа включительно
    """
    if base < 0:
        raise ValueError("base - неотрицательное число")
    if base == 0:
        return 1
    if base == 1:
        return 1
    for i in range(base, 0, -1):
        return i*factorial_recursion(i-1)


def lineup_factorials(N: int = 0, base: int = 1) -> List[int]:
    """создаёт список  факториалов от  base до N включительно

    N- предел последовательности
    base - первый шаг
    """
    """
    step_direction - направление шага, на случай base > N
    N_mod - прыгаем вокруг range чтобы предельное значение попало в вывод
    output - выводной список
    """

    step_direction = 1 if (base < N) else -1
    # определяемся с пределом и направлением шага списка
    if base < N:
        step_direction = 1
        N_mod = N + 1
    else:
        step_direction = -1
        N_mod = N - 1
    #! определяемся с пределом и направлением шага списка
    output = []
    for i in range(base, N_mod, step_direction):
        output.append(factorial_recursion(i))
    return output


def lineup_floats(N: int, base: int = 1) -> List[float]:
    """выводит сумму списка вещественных чисел образованных по формуле 
    o = (i + 1/i) ** i

    N - верхний предел ряда

    base - нижний предел ряда
    """
    """
    step_direction - направление шага, на случай base > N
    N_mod - прыгаем вокруг range чтобы предельное значение попало в вывод
    output - выводной список
    calc_output_item- выносим расчётную часть
    """

    def calc_output_item(seed: int) -> float:
        """считаем вывод в соответсвии с ТЗ.

        seed - int из внешнего счетчика 

        round_to - знаков до отсечки"""
        return (1 + 1/seed) ** seed

    step_direction = 1 if (base < N) else -1
    # определяемся с пределом и направлением шага списка
    if base < N:
        step_direction = 1
        N_mod = N + 1
    else:
        step_direction = -1
        N_mod = N - 1
    #! определяемся с пределом и направлением шага списка
    # идею с map подсмотрел на разборе.но это же вся суть- узнать новое.
    output = round(ndigits=2,
                   number=sum(list(map(
                       calc_output_item, range(base, N_mod, step_direction)))))
    return output


def lineup_multiplied(N: int, frequency: int = 5) -> int:
    """Выводит произведение элементов по индексам списка от -N до N.
    Индексы из внешнего файла. Файл создаётся и удаляется подфункциями.

    Вызовет BlockingIOError в случае угрозы перезаписи.

    N - предел списка

    frequency - количество индексов для файла
    """
    """
    limits - обращаемся к отрицательным вводам
    list_numbers - будем суммировать элементы отсюда
    output - вывод
    filename - имя файла который мы создадим
    frequency - количество индексов которые Мы запишем в файл
    content - содержимое файла
    fill_txt - подфункция, отвечает за заполнение файла
    clean_up_txt - подфункция, считывает индексы и удаляет файл
    """

    def fill_txt(filename: str, content: str) -> None:
        """создаём и заполняем файл. BlockingIOError- тут.

        filename - только имя файла, по директориям гулять _не надо_
        content - содержимое файла
        """

        if Path(filename).exists():
            raise BlockingIOError("ВАУ. Перезаписывать не будем.")
        with open(filename,'w') as file_:
            file_.write(content)
        return None

    def clean_up_txt(filename: str) -> List[int]:
        """считываем и __удаляем__ файл

        filename - адрес.
        """
        """extracted - содержимое файла"""
        output = []
        with open(filename,'r') as file_:
            extracted = file_.readlines()
        for line in extracted:
            try:
                output.append(int(line))
            except:
                print(f'not int-able line: __{line}__')
        os.unlink(filename)
        return output

    limits = (-N, N+1)
    list_numbers = [i for i in range(min(limits), max(limits), 1)]
    content = ""
    for i in range(frequency):
        content += (f"{random.choice(range(len(list_numbers)))}\n")
    filename = f"AM_{datetime.datetime.now():%Y-%m-%d_%H_%M_%f}.txt"
    fill_txt(filename=filename, content=content)
    indexes = clean_up_txt(filename=filename)
    output = 1
    print(f'список: {str(list_numbers)}')
    print(f'индексы: {str(indexes)}')
    for ind in indexes:
        print (f'{str(output)} * {str(list_numbers[ind])} = ',end='')
        output *= list_numbers[ind]
        print(f'{output}')
    return output


def shake_lineup(list_i: List[int]) -> list:
    output = []
    return output


def test_arrays_equality(
        seed_list: List[int], list_shuffled: List[int]
) -> bool:
    return sorted(seed_list) == sorted(list_shuffled)


def main():
    def t1() -> None:
        print(float_summarize_signs.__doc__)
        print(float_summarize_signs(validate_input_float(short_note="float!")))
        Break()

    def t2() -> None:
        print(lineup_factorials.__doc__)
        print(lineup_factorials(validate_input(short_note="Input N?")))
        Break()

    def t3() -> None:
        print(lineup_floats.__doc__)
        print(lineup_floats(
            validate_input(accepts_zero=False,
                           short_note="Input N?")
        ))

    def t4() -> None:
        print(lineup_multiplied.__doc__)
        print(lineup_multiplied(validate_input(short_note='Input N?')))
        Break()

    t4()


if __name__ == "__main__":
    main()
