"""
GB Программист, "Знакомство с языком Python( семинары)", #2

lineup_factorials - выводит последовательность факториалов

lineup_floats - выводит отредактированную последовательность

lineup_multiplied - выводит произведение элементов последовательности

shake_lineup - перемешивает список


factorial_recursion - считаем факториал

"""


from __future__ import annotations

__all__ = ['factorial_recursion']
__version__ = "#2"
__author__ = "anton6733@gmail.com"


# standart imports
import random
from typing import List

# local imports
from homework_sem1 import Break, validate_input


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
    """создаёт список  факториалов от  base до N

    N- предел последовательности
    base - первый шаг
    """

    """
    step_direction - направление шага, на случай base > N
    N_mod - прыгаем вокруг range чтобы предельное значение попало в вывод
    output - выводной список
    
    """
    step_direction = 1 if (base < N) else -1
    if base < N:
        step_direction = 1
        N_mod = N + 1
    else:
        step_direction = -1
        N_mod = N - 1 
    output = []
    if base == N:
        return [factorial_recursion(N)]
    for i in range(base, N_mod, step_direction):
        output.append(factorial_recursion(i))
    return output


def lineup_floats(N: int) -> None:
    return None


def lineup_multiplied(N: int) -> int:
    output = 0
    return output


def shake_lineup(list_i: List[int]) -> list:
    output = []
    return output


def test_arrays_equality(
        seed_list: List[int], list_shuffled: List[int]
) -> bool:
    return sorted(seed_list) == sorted(list_shuffled)


def main():
    print(lineup_factorials.__doc__)
    print(lineup_factorials(validate_input(short_note="Input N?")))
    # Break()


if __name__ == "__main__":
    main()
