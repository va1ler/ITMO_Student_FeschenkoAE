# Author = Фещенко Александр Эдуардович
# Group = P3117
# Date = 13.10.2026
import re

MINUTE = r'[0-5]?\d'
HOUR = r'(?:[01]?\d|2[0-3])'
DAY = r'(?:0?[1-9]|[12]\d|3[01])'
MONTH = r'(?:0?[1-9]|1[0-2])'
WEEKDAY = r'0?[0-6]'
STEP = r'[1-9]\d*'


def field(num):
    item = rf'(?:(?:\*|{num}-{num})(?:/{STEP})?|{num})'
    return rf'{item}(?:,{item})*'


CRON = rf'{field(MINUTE)}\s+{field(HOUR)}\s+{field(DAY)}\s+{field(MONTH)}\s+{field(WEEKDAY)}'


def solve(expr):
    return 'Верно' if re.fullmatch(CRON, expr) else 'Ошибка'


tests = [
    ('30 14 * * *', 'Верно'),
    ('*/5 * * * *', 'Верно'),
    ('0 0 1 1 *', 'Верно'),
    ('0,15,30,45 9-18/3 1-15 */2 1-5', 'Верно'),
    ('59  23  31  12  06', 'Верно'),
    ('60 * * * *', 'Ошибка'),
    ('* 24 * * *', 'Ошибка'),
    ('* * 0 * *', 'Ошибка'),
    ('* * * 13 *', 'Ошибка'),
    ('* * * * 7', 'Ошибка'),
    ('*/0 * * * *', 'Ошибка'),
    ('5/10 * * * *', 'Ошибка'),
    ('* * * *', 'Ошибка'),
    ('1--5 * * * *', 'Ошибка'),
]

for expr, expected in tests:
    got = solve(expr)
    print('OK  ' if got == expected else 'FAIL', expr, '->', got)
