"""
 Даны длины сторон треугольника и необходимо найти углы треугольника.
  Если невозможно сформировать треугольник из данных сторон (или для вырожденного треугольника),
  тогда результатом должны быть все нули. Результат должен быть представлен, как список (list) целых чисел
  в возрастающем порядке. Углы должны быть записаны в градусах и округляются до целого числа (стандартное округление).


Входные данные: Длины сторон треугольник, как целые числа (int).

Выходные данные: Углы данного треугольника в градусах, как сортированный список (list) целых чисел (int).

Примеры:

angles(4, 4, 4) == [60, 60, 60]

angles(3, 4, 5) == [37, 53, 90]

angles(2, 2, 5) == [0, 0, 0]

"""

import math


def get_angles(first, second, third):
    top = pow(first, 2) + pow(second, 2) - pow(third, 2)
    bottom = 2 * first * second
    angle = math.acos(top/bottom)
    return int(round(angle * 180 / math.pi))


def angles(a, b, c):
    if (a+b) > c and (b+c) > a and (a+c) > b:
        angle_a = get_angles(a, b, c)
        angle_b = get_angles(c, a, b)
        angle_c = 180 - angle_a - angle_b
        return sorted([angle_a, angle_b, angle_c])
    else:
        return [0, 0, 0]
