# def arithmetic(x, y, z):
#     if z == "+":
#         return x + y
#     elif z == "-":
#         return x - y
#     elif z == "*":
#         return x * y
#     elif z == "/":
#         return x / y
#     else:
#         return "Неизвестная ошибка"


# def is_year_leap(year):
#     if year % 4 == 0:
#         print('True високосный')
#     else:
#         print('False не високосный')


# def square(a):
#     p = 4 * a
#     s = a * a
#     d = (a ** 2) / 2
#
#     k = (p, s, d)
#
#     return k


# def season(month):
#     if month == 12 or month < 3:
#         return 'Winter'
#     elif month == 3 or month < 6:
#         return 'Sping'
#     elif month == 6 or month < 9:
#         return 'Summer'
#     elif month == 9 or month < 11:
#         return 'Autumn'
#     else:
#         return 'Error'


# def bank(a, years):
#     deposit = a
#     koef = 2
#     year = 1
#     while year <= years:
#         deposit = koef * deposit
#         year += 1
#         return deposit


def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    limit = n ** (1 / 2)

    i = 2

    while i <= limit:

        if n % i == 0:
            return False

    i += 1

    return True


if __name__ == '__main__':
    # print(arithmetic(2, 3, '+'))
    # print(arithmetic(2, 2, '*'))
    # print(arithmetic(4, 2, '-'))
    # print(arithmetic(4, 2, '/'))
    # print(arithmetic(4, 2, 0))

    # print(is_year_leap(2011, ))
    # print(is_year_leap(2020, ))

    # print(square(16))

    # print(season(12))  # Winter
    # print(season(9))  # Autumn

    # print(bank(20, 2))  # 40.0

    print(is_prime(2))  # true
    print(is_prime(6))  # false
