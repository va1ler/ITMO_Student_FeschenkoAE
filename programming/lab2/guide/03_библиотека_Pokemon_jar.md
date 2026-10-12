# ЛР2 — как устроена библиотека Pokemon.jar

[← теория](./02_теория_ООП.md) · [дальше: план лабы →](./04_план_лабы.md)

Документация: https://se.ifmo.ru/~tony/doc/ · пакет `ru.ifmo.se.pokemon` · файл: `lab2/task/Pokemon.jar` (2018 г., работает на Java 17 и 21, проверено).

## 1. Карта классов

```
Object
├── Pokemon                     ← твои покемоны наследуются отсюда
├── Move  (abstract)            ← атака: type, power, accuracy, priority, hits
│   ├── DamageMove (abstract)   ← атаки с уроном: считает урон
│   │   ├── PhysicalMove        ← урон от Attack / Defense
│   │   └── SpecialMove         ← урон от Sp.Attack / Sp.Defense
│   └── StatusMove              ← без урона, только эффекты
├── Effect                      ← эффект: статус или изменение характеристик на N ходов
├── Battle (final)              ← симулятор боя
└── enum'ы: Type (18 типов + NONE), Stat (HP, ATTACK, DEFENSE, SPEED,
            SPECIAL_ATTACK, SPECIAL_DEFENSE, ACCURACY, EVASION),
            Status (NORMAL, BURN, FREEZE, POISON, SLEEP, PARALYZE)
```

## 2. `Pokemon` — что тебе пригодится

| Метод | Доступ | Зачем |
|---|---|---|
| `Pokemon(String name, int level)` | public | вызываешь через `super(name, level)` |
| `setType(Type... types)` | **protected** | 1 или 2 типа: `setType(Type.GROUND, Type.GHOST)` |
| `setStats(hp, att, def, spAtt, spDef, speed)` | public final | 6 базовых характеристик (порядок важен!) |
| `setMove(Move... moves)` | **protected** | задать атаки, **заменив** прежние |
| `addMove(Move move)` | **protected** | **добавить** атаку (максимум 4, иначе забудет самую старую) |
| `setMod(Stat stat, int value)` | public final | изменить характеристику на ±N ступеней (−6…+6), сам печатает сообщение |
| `getCondition()` | public final | текущий статус (`Status.PARALYZE` и т. п.) |
| `confuse()` | public final | смутить покемона |

Почти все методы `final` → переопределять в своих покемонах **нечего**. Покемон в лабе = **только конструктор**.

`setType` / `setMove` / `addMove` — `protected`, поэтому вызываются **из конструктора** твоего класса, а не из `Main`.

## 3. `Move` и наследники — что можно переопределить

Конструкторы (у всех трёх одинаковые):
```java
super(Type type, double power, double accuracy)                       // priority = 0, hits = 1
super(Type type, double power, double accuracy, int priority, int hits)
```
Точность — **доля**: 100% → `1`, 90% → `0.9`.

Что происходит при атаке (`attack` уже `final`, его не трогаешь):

**DamageMove** (Physical/Special):
1. `checkAccuracy(att, def)` — попал или нет;
2. расчёт урона: `calcBaseDamage` × `calcAttDefFactor` × крит × бонус своего типа × эффективность типов × случайность;
3. `applyOppDamage(def, damage)` — урон цели;
4. `applySelfDamage(att, damage)` — урон себе (по умолчанию ничего);
5. `applyOppEffects(def)` — доп. эффекты на цель (по умолчанию ничего);
6. `applySelfEffects(att)` — доп. эффекты на себя (по умолчанию ничего).

**StatusMove**: `checkAccuracy` → проверка иммунитета по типу → `applySelfEffects` и `applyOppEffects`. Урона нет.

Методы-«крючки» (все `protected`, можно `@Override`):

| Метод | Когда переопределять | Пример из варианта |
|---|---|---|
| `describe()` | **всегда** — текст в бою после имени покемона | все 12 атак |
| `applyOppEffects(Pokemon p)` | эффект на цель | Thunder, Confide, Low Sweep, Shadow Ball… |
| `applySelfEffects(Pokemon p)` | эффект на себя | Charge Beam, Rock Polish |
| `checkAccuracy(Pokemon att, Pokemon def)` | атака никогда не промахивается → `return true;` | Confide, Disarming Voice |
| `calcBaseDamage(Pokemon att, Pokemon def)` | нестандартная сила | Facade |
| `applySelfDamage(Pokemon att, double damage)` | отдача себе | — (в варианте нет) |

## 4. Как делать эффекты

**Изменить характеристику на N ступеней** — проще всего:
```java
p.setMod(Stat.SPEED, -1);          // скорость −1
p.setMod(Stat.SPECIAL_ATTACK, 2);  // спец. атака +2
```

**Наложить статус** — статические методы `Effect`:
```java
Effect.paralyze(p);   // паралич
Effect.burn(p); Effect.poison(p); Effect.freeze(p); Effect.sleep(p);
Effect.confuse(p); Effect.flinch(p);
```

**С вероятностью** — обычный `Math.random()`, он возвращает число в [0, 1):
```java
if (Math.random() < 0.3) { ... }   // 30%
```

**Продвинутый вариант** — объект `Effect` с «текучим» интерфейсом (каждый сеттер возвращает тот же `Effect`):
```java
Effect e = new Effect().chance(0.3).turns(2).stat(Stat.ATTACK, -1);
p.addEffect(e);
```
Для нашего варианта хватает `setMod` и статических методов.

## 5. `Battle`

```java
Battle b = new Battle();
b.addAlly(покемон);   // в свою команду
b.addFoe(покемон);    // в команду соперника
b.go();               // бой до победы одной из команд
```
Каждый ход покемон **случайно** выбирает одну из своих атак. Порядок ходов зависит от приоритета атаки и скорости.

## 6. Сборка и запуск (средствами JDK)

Структура папки, которую предлагаю (рядом с `task/`):
```
programming/lab2/
├── task/            (задание, Pokemon.jar)
└── src/
    ├── lab2/Main.java
    ├── pokemons/Thundurus.java, Golett.java, ...
    └── moves/Thunder.java, Confide.java, ...
```
Команды (из папки `programming/lab2`):
```
javac --release 17 -encoding UTF-8 -cp task/Pokemon.jar -d out src/lab2/Main.java src/pokemons/*.java src/moves/*.java
java -cp task/Pokemon.jar:out lab2.Main
```
- `--release 17` — потому что на helios Java 17 (урок ЛР1).
- `-encoding UTF-8` — русские строки в исходниках; на helios кодировка по умолчанию может быть другой.
- Если в терминале helios вместо русского вопросики — проверь `locale`; при необходимости запусти с `-Dfile.encoding=UTF-8`.
- Сообщения боя печатаются на языке системы. Принудительно по-русски: `java -Duser.language=ru -Duser.country=RU ...`.
