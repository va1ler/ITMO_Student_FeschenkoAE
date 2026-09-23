#1
n = 76589
ostatki = []
while n > 0:
    ostatki.append(n % 11)
    n = n // 11
ostatki.reverse()

result1 = ""
for d in ostatki:
    if d < 10:
        result1 += str(d)
    else:
        result1 += "A"

print("1)", "76589(10) =", result1 + "(11)")


#2
s = "77774"
print("2)", "77774(9) =", int(s,9), "(10)")


#3
s = "29181"
n = int(s,11)

ostatki = []
while n > 0:
    ostatki.append(n % 9)
    n = n // 9
ostatki.reverse()

result3 = ""
for d in ostatki:
    result3 += str(d)

print("3)", "29181(11) =", result3 + "(9)")


#4
n = 74
bity = []
while n > 0:
    bity.append(n % 2)
    n = n // 2
bity.reverse()
celaya_chast = ""
for b in bity:
    celaya_chast += str(b)


f = 0.29
drob_bity = []
for i in range(6):
    f = f * 2
    d = int(f)
    drob_bity.append(d)
    f = f - d

if drob_bity[5] >= 1:
    i = 4
    while i >= 0:
        drob_bity[i] += 1
        if drob_bity[i] == 2:
            drob_bity[i] = 0
            i -= 1
        else:
            break

drobnaya_chast = ""
for d in drob_bity[:5]:
    drobnaya_chast += str(d)

print("4)", "74,29(10) =", celaya_chast + "," + drobnaya_chast + "(2)")


#5
tetrady = {
    "0": "0000", "1": "0001", "2": "0010", "3": "0011",
    "4": "0100", "5": "0101", "6": "0110", "7": "0111",
    "8": "1000", "9": "1001", "A": "1010", "B": "1011",
    "C": "1100", "D": "1101", "E": "1110", "F": "1111",
}

celaya_chast = tetrady["A"] + tetrady["0"]          # A0 -> 10100000
drobnaya_chast_polnaya = tetrady["6"] + tetrady["2"]  # 62 -> 01100010
drobnaya_chast = drobnaya_chast_polnaya[:5]           # округление до 5 знаков (6-й знак 0)

print("5)", "A0,62(16) =", celaya_chast + "," + drobnaya_chast + "(2)")


#6
triady = {
    "0": "000", "1": "001", "2": "010", "3": "011",
    "4": "100", "5": "101", "6": "110", "7": "111",
}

celaya_chast = (triady["1"] + triady["5"]).lstrip("0")
drobnaya_chast_polnaya = triady["4"] + triady["1"]
# 6-й знак = 1, значит округляем 5-й знак в большую сторону
drobnaya_chast = "10001"

print("6)", "15,41(8) =", celaya_chast + "," + drobnaya_chast + "(2)")


#7
drob = "101011"
drob = drob + "0" * ((4 - len(drob) % 4) % 4)   # дополнили до 1010 1100

group1 = drob[0:4]   # 1010
group2 = drob[4:8]   # 1100

hex_cifry = {"1010": "A", "1100": "C"}   # словарь только для нужных групп

print("7)", "0,101011(2) = 0," + hex_cifry[group1] + hex_cifry[group2] + "(16)")


#8
drob = "101011"
result8 = 0.0
for i, ch in enumerate(drob, start=1):
    result8 += int(ch) * (2 ** -i)

result8 = round(result8, 5)
print("8)", "0,101011(2) =", result8, "(10)")


#9
cel = "78"
drob = "02"
hex_znach = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
             "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

celaya_chast = hex_znach[cel[0]] * 16 + hex_znach[cel[1]]

drobnaya_chast = 0.0
for i, ch in enumerate(drob, start=1):
    drobnaya_chast += hex_znach[ch] * (16 ** -i)

result9 = round(celaya_chast + drobnaya_chast, 5)

print("9)", "78,02(16) =", result9, "(10)")


#10
fib = [1, 2]
while fib[-1] <= 310:
    fib.append(fib[-1] + fib[-2])
fib = [x for x in fib if x <= 310]
fib.reverse()

ostatok = 310
bity = []
for f in fib:
    if f <= ostatok:
        bity.append("1")
        ostatok -= f
    else:
        bity.append("0")

result10 = "".join(bity)

print("10)", "310(10) =", result10 + "(Фиб)")


#11
cifry = "142110"
cifry_sprava = cifry[::-1]

result11 = 0
faktorial = 1
for i, ch in enumerate(cifry_sprava, start=1):
    faktorial = faktorial * i
    result11 += int(ch) * faktorial

print("11)", "142110(Факт) =", result11, "(10)")


# 12
cifry = "654"
cifry_sprava = cifry[::-1]   # 4,5,6

result12 = 0
for i, ch in enumerate(cifry_sprava):
    result12 += int(ch) * ((-10) ** i)

print("12)", "654(-10) =", result12, "(10)")


# 13
n = 21512
cifry_rezultata = []
while n != 0:
    r = n % 9
    if r > 4:
        d = r - 9
    else:
        d = r
    cifry_rezultata.append(d)
    n = (n - d) // 9

cifry_rezultata.reverse()

result13 = ""
for d in cifry_rezultata:
    if d < 0:
        result13 += "{^" + str(abs(d)) + "}"
    else:
        result13 += str(d)

print("13)", "21512(10) =", result13 + "(9С)")

