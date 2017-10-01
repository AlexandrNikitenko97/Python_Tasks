"""
 Расстояние Хэмминга между двумя двоичными числами - это число позиций, в которых биты различаются
 Для примера:

    117 = 0 1 1 1 0 1 0 1
     17 = 0 0 0 1 0 0 0 1
      H = 0+1+1+0+0+1+0+0 = 3

Даны два положительных целых числа (N, M) в десятичном виде.
Вам необходимо подсчитать расстояние Хэмминга между этими двумя числами в двоичном виде.

Входные данные: Два аргумента, как целые числа (int).

Выходные данные: Расстояние Хэмминга, как целое число (int).

Примеры:

hamming(117, 17) == 3

hamming(1, 2) == 2

hamming(16, 15) == 5

"""


def hamming(n, m):
    n = bin(n).lstrip('0b')
    m = bin(m).lstrip('0b')
    n_ar = [x for x in n]
    m_ar = [x for x in m]
    different = 0
    while True:
        if len(n_ar) == len(m_ar):
            for i in range(len(n_ar)):
                if n_ar[i] != m_ar[i]:
                    different += 1
            break
        elif len(n) - len(m) > 0:
            while len(n_ar) != len(m_ar):
                m_ar.insert(0, '0')
        else:
            while len(n_ar) != len(m_ar):
                n_ar.insert(0, '0')
    return different
