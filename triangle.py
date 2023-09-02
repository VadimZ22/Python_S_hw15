import argparse
from triangle_log import log_info, log_error


class Triangle:

    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <=0:
            log_error('Длина стороны треугльника должна быть больше 0!')
            raise ValueError()
        self.a = a
        self.b = b
        self.c = c
        log_info(f'Создан треугольник со сторонами: {self.a}, {self.b},{self.c}')

    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b},{self.c}'

    def __eq__(self, other):
        if isinstance(other, Triangle):
            first = sorted((self.a, self.b, self.c))
            second = sorted((other.a, other.b, other.c))
            return first == second
        log_error(f'Объект {other} не является экземпляром класса Triangle')
        raise ValueError()


def create_triangle(a, b, c):
    return Triangle(a, b, c)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Creating triangle')
    parser.add_argument('-a', metavar='a', type=float,
                        help='enter side a', default=1)
    parser.add_argument('-b', metavar='b', type=float,
                        help='enter side b', default=0)
    parser.add_argument('-c', metavar='c', type=float,
                        help='enter side c', default=0)
    args = parser.parse_args()
    create_triangle(args.a, args.b, args.c)

# Вызов
# python .\triangle.py -a 10 -b 15 -c 13
