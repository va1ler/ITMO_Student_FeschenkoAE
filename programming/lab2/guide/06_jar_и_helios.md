# 06. Сборка jar средствами JDK на helios

Как в ЛР1 (`lab1/guide/04_jar_и_helios.md`): на защите закидываешь файлы на helios, там компилируешь, собираешь jar командой `jar cfe` и запускаешь. Все команды проверены на твоём проекте.

## Чем отличается от ЛР1
В ЛР1 был один класс без библиотек. Теперь:
- классы лежат в **пакетах** (`lab2`, `pokemons`, `moves`), поэтому главный класс называется `lab2.Main`, а не `Main`;
- код использует **чужую библиотеку** `Pokemon.jar`. Компилятору её показываем через `-cp`, а в итоговый jar **кладём её классы внутрь**. Тогда `lab2.jar` самодостаточный: запускается один, без `Pokemon.jar` рядом.

```
src/**/*.java --javac (+Pokemon.jar)--> out/ (наши .class)
Pokemon.jar   --jar xf-->               out/ru/... (классы библиотеки)
out/          --jar cfe-->              lab2.jar  --java -jar-->  бой
```

## Какие файлы нужны на helios
| Файл | Зачем |
|---|---|
| `src/` | исходники: `lab2/Main.java`, 6 покемонов, 12 атак |
| `Pokemon.jar` | библиотека (в `~/proglab2` уже лежит) |

## 1. Закинуть файлы (терминал Mac)
```bash
cd ~/Documents/ITMO_Student_FeschenkoAE/programming/lab2/Pocemonfights
scp -P 2222 -r src Pokemon.jar s561306@helios.cs.ifmo.ru:~/proglab2/
```
- `-r` — копировать папку целиком (recursive).
- У `scp` порт большой `-P`, у `ssh` маленькой `-p`.

## 2. Собрать и запустить (на helios), по одной команде
```bash
ssh -p 2222 s561306@helios.cs.ifmo.ru
cd ~/proglab2
javac -encoding UTF-8 -cp Pokemon.jar -sourcepath src -d out src/lab2/Main.java
cd out
jar xf ../Pokemon.jar
cd ..
jar cfe lab2.jar lab2.Main -C out .
java -jar lab2.jar
```

Разбор `javac`:
- `-encoding UTF-8` — исходники в UTF-8 (русский текст в `describe()`).
- `-cp Pokemon.jar` — classpath: где искать готовые классы (`Pokemon`, `Battle`, `SpecialMove`...).
- `-sourcepath src` — где искать **исходники** остальных классов. Указываем только `Main.java`, а `javac` сам находит по `import` покемонов, а через них атаки, и компилирует их тоже.
- `-d out` — куда класть `.class`. Папки повторяют пакеты: `out/lab2/Main.class`, `out/pokemons/Golett.class`, `out/moves/ShadowBall.class`.

Разбор `jar xf ../Pokemon.jar` (выполняется внутри `out`):
- `x` — extract (распаковать), `f` — из файла `../Pokemon.jar` (`..` — папка уровнем выше).
- В `out` появляется папка `ru/ifmo/se/pokemon/` с классами библиотеки, рядом с нашими.

Разбор `jar cfe lab2.jar lab2.Main -C out .` (как в ЛР1):
- `c` — create, `f` — имя архива (`lab2.jar`), `e` — entry point, главный класс `lab2.Main` (полное имя с пакетом). `jar` сам создаёт манифест со строкой `Main-Class: lab2.Main`.
- `-C out .` — зайти в `out` и взять всё оттуда: и наши классы, и классы библиотеки.

Проверка:
```bash
jar tf lab2.jar    # внутри: META-INF/MANIFEST.MF, lab2/, pokemons/, moves/, ru/ifmo/se/pokemon/...
```

Скриншот вывода боя — для отчёта.

## Если что-то не так
| Что видишь | Причина и что делать |
|---|---|
| `scp: ... No such file or directory` | нет папки на helios: `ssh -p 2222 s561306@helios.cs.ifmo.ru mkdir -p proglab2` |
| `package ru.ifmo.se.pokemon does not exist` | забыл `-cp Pokemon.jar` или его нет в папке |
| `no main manifest attribute, in lab2.jar` | забыл `e` и имя класса: `jar cf` вместо `jar cfe ... lab2.Main` |
| `Could not find or load main class Main` | в `cfe` написал `Main` вместо `lab2.Main` |
| `NoClassDefFoundError: ru/ifmo/se/pokemon/...` | забыл распаковать библиотеку в `out` (`jar xf ../Pokemon.jar` внутри `out`) |
| `Could not reserve enough space...` | `java -Xmx256m -jar lab2.jar` |
| вместо русского `????` | `java -Dfile.encoding=UTF-8 -jar lab2.jar` |
| бой «завис» | это нормально: библиотека делает паузы между ходами, бой идёт ~15 с |

## Вопросы на защите про сборку
- **Что такое classpath?** Список мест (папок и jar), где JVM и `javac` ищут классы. Разделитель на Unix `:`, на Windows `;`.
- **Зачем `-cp` при компиляции?** Компилятор должен знать, что `Pokemon` и `SpecialMove` существуют и какие у них методы.
- **Зачем распаковывать `Pokemon.jar` в `out`?** Чтобы классы библиотеки попали внутрь `lab2.jar`. При `java -jar` флаг `-cp` игнорируется, и JVM ищет классы только внутри jar (и в `Class-Path` манифеста, которого у нас нет).
- **Почему `lab2.Main`, а не `Main`?** Класс лежит в пакете `lab2`, полное имя включает пакет.
- **Где манифест, если мы его не писали?** Его создаёт `jar`: флаг `e` записывает в `META-INF/MANIFEST.MF` строку `Main-Class: lab2.Main`.
- **Как запустить без jar?** `java -cp Pokemon.jar:out lab2.Main`.
- **Как ещё можно было?** Не распаковывать библиотеку, а написать свой манифест со строкой `Class-Path: Pokemon.jar` и собрать `jar cfm`. Тогда `Pokemon.jar` должен лежать рядом с `lab2.jar`.
