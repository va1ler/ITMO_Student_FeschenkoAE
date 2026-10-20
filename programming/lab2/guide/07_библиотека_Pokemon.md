# 07. Библиотека Pokemon.jar (пакет ru.ifmo.se.pokemon)

Пересказ документации пакета. Описания классов взяты со страницы документации (скрин), состав методов взят из самого Pokemon.jar командой `javap -protected`.

## Как всё устроено в двух словах

`Battle` берёт две команды покемонов и заставляет их драться. Каждый ход покемон выбирает одну из своих атак (`Move`) и применяет её к противнику. Атаки бывают трёх видов: физические и специальные (наносят урон) и статусные (не наносят урон, а меняют характеристики или состояние). Ты в лабе пишешь только наследников `Pokemon` и наследников трёх видов атак, всё остальное делает библиотека.

## Классы

### Pokemon — предок всех покемонов
Обычный (не abstract) публичный класс. Твои покемоны наследуются от него.
- `Pokemon(String name, int level)` — конструктор, его вызывает твой `super(name, level)`.
- **protected** (вызываешь только внутри своего класса-наследника):
  - `setType(Type...)` — задать типы покемона (например `Type.FAIRY`);
  - `setMove(Move...)` / `addMove(Move)` — задать атаки (максимум 4);
  - `addType(Type)`, `getPreparedMove()`.
- **public final** (переопределить нельзя): `setStats(hp, att, def, spAtt, spDef, speed)` — базовые характеристики; `setLevel`, `getLevel`, `getHP`, `getStat(Stat)`, `isAlive`, `getCondition`, `setCondition`, `addEffect`, `setMod(Stat, int)`, `confuse`, `restore`, `attack`, `turn`, `toString` и др.
- Почему почти всё `final`: автор библиотеки запретил менять механику боя, ты можешь только настроить покемона.

### Move — абстрактный предок всех атак
- Поля `protected`: `type`, `power`, `accuracy`, `priority`, `hits`.
- Конструкторы: `Move()`, `Move(Type, power, accuracy)`, `Move(Type, power, accuracy, priority, hits)`.
- `protected abstract void attack(Pokemon att, Pokemon def)` — абстрактный, поэтому `Move` нельзя создать через `new`.
- Методы, которые можно переопределить (protected, не final):
  - `checkAccuracy(att, def)` — попала ли атака (ты переопределил в Confide и DisarmingVoice → всегда `true`);
  - `describe()` — текст «использует …», его ты переопределяешь во всех атаках;
  - `applyOppEffects(Pokemon)` — эффект на противника;
  - `applySelfEffects(Pokemon)` — эффект на себя.
- Статические «служебные» атаки: `getNoMove()`, `getStruggleMove()`, `getConfusionMove()`.

### DamageMove extends Move — абстрактный класс атак, которые наносят урон
- Реализует `attack(...)` как `public final`: проверка точности → расчёт урона → применение урона и эффектов.
- Формула урона разбита на методы (все protected, можно переопределить):
  `calcBaseDamage` (ты переопределил в Facade: ×2 при BURN/POISON/PARALYZE), `calcTypeEffect`, `calcCriticalHit`, `calcSameTypeAttackBonus`, `calcRandomDamage`, `applyOppDamage`, `applySelfDamage`.
- `protected abstract double calcAttDefFactor(att, def)` — остаётся абстрактным: какие характеристики сравнивать, решают наследники.

### PhysicalMove extends DamageMove — физические атаки
Реализует `calcAttDefFactor` (final) через ATTACK атакующего и DEFENSE защищающегося. Твои: LowSweep, Facade, VineWhip.

### SpecialMove extends DamageMove — специальные атаки
Реализует `calcAttDefFactor` (final) через SPECIAL_ATTACK и SPECIAL_DEFENSE. Твои: ShadowBall, FlashCannon, DazzlingGleam, DisarmingVoice, FocusBlast, ChargeBeam, Thunder.

### StatusMove extends Move — статусные атаки (без урона)
Реализует `attack(...)` как `public final`: проверяет `checkAccuracy`, и если попала, вызывает `applyOppEffects` (на противника) и `applySelfEffects` (на себя). Твои: RockPolish, Confide.

### Battle — проведение боя (`public final class`)
`new Battle()`, `addAlly(Pokemon)`, `addFoe(Pokemon)`, `go()`. Есть свой `main` — поэтому в манифесте Pokemon.jar стоит `Main-Class: ru.ifmo.se.pokemon.Battle`.

### Effect — эффект на покемона (`final`)
- Строится цепочкой: `new Effect().chance(0.3).turns(2).condition(Status.SLEEP).stat(Stat.SPEED, 2)`.
- Готовые статические эффекты: `Effect.burn(p)`, `paralyze(p)` (у тебя в Thunder с шансом 30%), `freeze`, `poison`, `sleep`, `flinch`, `confuse`.

### Перечисления (enum)
- `Type` — типы покемонов и атак: NORMAL, FIRE, WATER, ELECTRIC, GRASS, ICE, FIGHTING, POISON, GROUND, FLYING, PSYCHIC, BUG, ROCK, GHOST, DRAGON, DARK, STEEL, FAIRY, NONE.
- `Stat` — характеристики: HP, ATTACK, DEFENSE, SPEED, SPECIAL_ATTACK, SPECIAL_DEFENSE, ACCURACY, EVASION.
- `Status` — состояния: NORMAL, BURN, FREEZE, POISON, SLEEP, PARALYZE.

### Messages, Messages_en, Messages_ru_RU
Тексты сообщений боя на разных языках (наследники `ListResourceBundle`). Тебе их трогать не надо.

## Что из этого спросят на защите
- Почему `Move` и `DamageMove` абстрактные → у них есть абстрактные методы (`attack`, `calcAttDefFactor`), объект такого класса создать нельзя.
- Почему ты наследуешь атаки от `PhysicalMove`/`SpecialMove`/`StatusMove`, а не от `Move` → в них уже реализован `attack`, тебе остаётся переопределить эффекты и `describe`.
- Почему методы `protected` → они видны наследникам (твоим классам в других пакетах), но не всем подряд.
- Почему многие методы `final` → чтобы наследник не мог сломать механику боя.
