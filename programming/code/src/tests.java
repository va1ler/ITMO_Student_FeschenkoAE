public class tests {
    public static void main(String[] args) {
        Monster a = new Charmeleon("Огонёк");
        Monster b = new Bulbasaur("Листик");
        Arena arena = new Arena(a, b);
        arena.go();
    }
}

class Monster {
    private String name;
    private int hp;
    private int defense = 0;
    private Move[] moves = new Move[4];
    private int moveCount = 0;

    Monster(String name, int hp) {
        this.name = name;
        this.hp = hp;
    }

    protected void addMove(Move m) {
        moves[moveCount] = m;
        moveCount++;
    }

    String getName() {
        return name;
    }

    boolean isAlive() {
        return hp > 0;
    }

    Move getMove(int turn) {
        return moves[turn % moveCount];
    }

    void takeDamage(int power) {
        int d = power - defense;
        if (d < 0) {
            d = 0;
        }
        hp = hp - d;
        if (hp < 0) {
            hp = 0;
        }
        System.out.println("  " + name + " теряет " + d + " HP, осталось " + hp);
    }

    void changeDefense(int delta) {
        defense = defense + delta;
        System.out.println("  защита " + name + ": " + defense);
    }
}

abstract class Move {
    private int power;

    Move(int power) {
        this.power = power;
    }

    final void attack(Monster att, Monster def) {
        System.out.println(att.getName() + " " + describe());
        if (power > 0) {
            def.takeDamage(power);
        }
        applyOppEffects(def);
        applySelfEffects(att);
    }

    protected abstract String describe();

    protected void applyOppEffects(Monster p) {
    }

    protected void applySelfEffects(Monster p) {
    }
}

final class Scratch extends Move {
    Scratch() {
        super(10);
    }

    @Override
    protected String describe() {
        return "царапает";
    }
}

final class Ember extends Move {
    Ember() {
        super(15);
    }

    @Override
    protected String describe() {
        return "пускает угольки";
    }
}

final class Harden extends Move {
    Harden() {
        super(0);
    }

    @Override
    protected String describe() {
        return "твердеет";
    }

    @Override
    protected void applySelfEffects(Monster p) {
        p.changeDefense(5);
    }
}

class Charmander extends Monster {
    Charmander(String name, int hp) {
        super(name, hp);
        addMove(new Scratch());
    }
}

final class Charmeleon extends Charmander {
Charmeleon(String name) {
        super(name, 40);
        addMove(new Ember());
}
}

final class Bulbasaur extends Monster {
    Bulbasaur(String name) {
        super(name, 30);
        addMove(new Harden());
        addMove(new Scratch());
    }
}

class Arena {
    private Monster first;
    private Monster second;

    Arena(Monster first, Monster second) {
        this.first = first;
        this.second = second;
    }

    void go() {
        int turn = 0;
        while (first.isAlive() && second.isAlive()) {
            first.getMove(turn).attack(first, second);
            if (second.isAlive()) {
                second.getMove(turn).attack(second, first);
            }
            turn++;
        }
        Monster winner = first.isAlive() ? first : second;
        System.out.println("Победил " + winner.getName());
    }
}