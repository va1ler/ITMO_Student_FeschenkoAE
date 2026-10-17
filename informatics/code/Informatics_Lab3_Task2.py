# Author = Фещенко Александр Эдуардович
# Group = P3117
# Date = 13.10.2026
import re

VOWELS = 'аеёиоуыэюя'
CONS = rf'[^\W{VOWELS}]'
WORD = rf'\b{CONS}*([{VOWELS}])(?:{CONS}|\1)*\b'


def solve(text):
    words = [m.group() for m in re.finditer(WORD, text, re.I)]
    return sorted(words, key=lambda w: (len(w), w.lower()))


tests = [
    ('Классное слово – обороноспособность, которое должно идти после слов: трава и молоко.',
     ['и', 'идти', 'слов', 'слово', 'трава', 'должно', 'молоко', 'обороноспособность']),
    ('Мама мыла раму, а папа читал газету.',
     ['а', 'Мама', 'папа']),
    ('Ёжик нёс мёд через ёлку в лес.',
     ['лес', 'мёд', 'нёс', 'через']),
    ('ВНИМАНИЕ: Сдать ДЗ в срок! День тишины.',
     ['День', 'срок', 'Сдать']),
    ('Утро ясное, погода плохая.',
     []),
]

for text, expected in tests:
    got = solve(text)
    print('OK  ' if got == expected else 'FAIL', got)