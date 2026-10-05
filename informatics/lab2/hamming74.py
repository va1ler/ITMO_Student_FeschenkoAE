"""Декодер классического кода Хэмминга (7,4).

На вход: 7 символов «0»/«1» подряд, например 0000010.
Порядок битов: r1 r2 i1 r3 i2 i3 i4 (позиции 1..7),
где r — проверочные биты, i — информационные.

Программа считает синдром, находит ошибочный бит (если он есть),
исправляет его и выводит правильные информационные биты.
"""
import sys

NAMES = ["r1", "r2", "i1", "r3", "i2", "i3", "i4"]   # имена битов по позициям 1..7


def read_message(text):
    """Проверяет ввод и превращает строку в список из 7 чисел 0/1."""
    text = text.strip().replace(" ", "")
    if len(text) != 7 or any(ch not in "01" for ch in text):
        raise ValueError("нужно ровно 7 символов «0» или «1», например 0000010")
    return [int(ch) for ch in text]


def syndrome(b):
    """Синдром: каждая проверка — XOR битов, в номере позиции которых есть нужная степень двойки."""
    r1, r2, i1, r3, i2, i3, i4 = b
    s1 = r1 ^ i1 ^ i2 ^ i4      # позиции 1, 3, 5, 7
    s2 = r2 ^ i1 ^ i3 ^ i4      # позиции 2, 3, 6, 7
    s3 = r3 ^ i2 ^ i3 ^ i4      # позиции 4, 5, 6, 7
    return s1, s2, s3


def decode(text):
    b = read_message(text)
    s1, s2, s3 = syndrome(b)
    pos = s1 + 2 * s2 + 4 * s3          # номер ошибочного бита (0 — ошибки нет)

    fixed = b[:]
    if pos:
        fixed[pos - 1] ^= 1               # инвертируем ошибочный бит

    info = "".join(str(fixed[i]) for i in (2, 4, 5, 6))   # i1 i2 i3 i4
    return (s1, s2, s3), pos, "".join(map(str, fixed)), info


def main():
    text = sys.argv[1] if len(sys.argv) > 1 else input("Введите 7 бит (r1 r2 i1 r3 i2 i3 i4): ")
    try:
        (s1, s2, s3), pos, fixed, info = decode(text)
    except ValueError as e:
        print("Ошибка ввода:", e)
        sys.exit(1)

    print(f"Синдром (s1 s2 s3): {s1}{s2}{s3}")
    if pos == 0:
        print("Ошибок нет")
    else:
        print(f"Ошибка в бите {pos} ({NAMES[pos - 1]})")
        print(f"Исправленное сообщение: {fixed}")
    print(f"Информационные биты (i1 i2 i3 i4): {info}")


if __name__ == "__main__":
    main()
