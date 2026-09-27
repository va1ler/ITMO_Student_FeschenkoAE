# 04. Сборка jar средствами JDK и запуск на helios

⚠️ По конспекту первые 3 лабы надо делать **средствами JDK**. Поэтому собираем командами в терминале, а не кнопками IntelliJ. Это легко, и на защите могут попросить показать.

## Как устроен путь от кода до запуска
```
Main.java  --javac-->  Main.class (байт-код)  --jar-->  lab1.jar  --java -jar-->  JVM выполняет
```
- **javac** — компилятор. Переводит исходник в **байт-код**: это не машинный код процессора, а инструкции для виртуальной машины.
- **JVM** (`java`) исполняет байт-код на любой ОС. Поэтому один и тот же jar работает и на маке, и на helios. Это главная особенность Java: «write once, run anywhere».
- **JDK** = JRE + инструменты разработчика (`javac`, `jar`, `javadoc`, `javap`...). **JRE** = JVM + стандартная библиотека, то есть минимум, чтобы только **запускать**.
- **jar** — zip-архив с `.class`-файлами и файлом-«паспортом» `META-INF/MANIFEST.MF`. В манифесте строка `Main-Class: Main` говорит JVM, с какого класса начинать. Без неё jar не будет исполняемым.

## Сборка (терминал в папке `ITMO_CODING_JAVA`)
```bash
cd ~/Documents/ITMO_Student_FeschenkoAE/ITMO_CODING_JAVA

javac --release 21 -d build src/Main.java     # 1. компиляция в папку build/
jar cfe lab1.jar Main -C build .              # 2. упаковка в jar
java -jar lab1.jar                            # 3. проверка
```
Разбор флагов:
- `--release 21`: компилировать под Java 21, чтобы точно запустилось на helios.
- `-d build`: складывать `.class` в папку `build`.
- `jar c f e`: **c**reate (создать), **f**ile (имя архива `lab1.jar`), **e**ntry point (главный класс `Main`, он попадёт в манифест).
- `-C build .`: зайти в папку `build` и взять оттуда всё (`.`).

Посмотреть, что внутри jar: `jar tf lab1.jar`.

Альтернатива с явным манифестом (её тоже полезно знать):
```bash
echo "Main-Class: Main" > manifest.txt
jar cfm lab1.jar manifest.txt -C build .
```

## Отправка на helios и запуск
Логин вида `sXXXXXX` (обычно `s` + номер ИСУ, у тебя, скорее всего, `s561306`). Порт **2222**.
```bash
scp -P 2222 lab1.jar s561306@helios.cs.ifmo.ru:~/     # скопировать jar в домашнюю папку на helios
ssh -p 2222 s561306@helios.cs.ifmo.ru                 # зайти на helios
java -version                                         # убедиться, что там 21
java -jar lab1.jar                                    # запуск
exit                                                  # выйти
```
- У `scp` порт задаётся большой `-P`, у `ssh` маленькой `-p`. Частая путаница.
- Если на helios JVM ругается на память (`Could not reserve enough space...`), запусти с ограничением: `java -Xmx256m -jar lab1.jar`.
- Если `java` на helios не находится или версия не та, пиши мне, посмотрим `which java`.

## Что добавить в `.gitignore`
Папку `build/` и `*.jar` в git не кладём: это результат сборки, его всегда можно пересобрать. Правило `*.class` уже есть. Добавим `build/`, а jar можно и закоммитить, если захочешь показать его прямо с GitHub.
