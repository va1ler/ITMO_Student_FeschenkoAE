import sys

NAMES = ["r1", "r2", "i1", "r3", "i2", "i3", "i4"] 

def read_message(text):
    text = text.strip().replace(" ", "")
    if len(text) != 7 or any(ch not in "01" for ch in text):
        raise ValueError("нужно ровно 7 символов «0» или «1», например 0000010")
    return [int(ch) for ch in text]


def syndrome(b):
    r1, r2, i1, r3, i2, i3, i4 = b
    s1 = r1 ^ i1 ^ i2 ^ i4      
    s2 = r2 ^ i1 ^ i3 ^ i4      
    s3 = r3 ^ i2 ^ i3 ^ i4      
    return s1, s2, s3


def decode(text):
    b = read_message(text)
    s1, s2, s3 = syndrome(b)
    pos = s1 + 2 * s2 + 4 * s3          

    fixed = b[:]
    if pos:
        fixed[pos - 1] ^= 1               

    info = "".join(str(fixed[i]) for i in (2, 4, 5, 6))   
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
