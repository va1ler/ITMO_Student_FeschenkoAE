package moves;

import ru.ifmo.se.pokemon.*;

public final class Facade extends PhysicalMove {
    public Facade() {
        super(Type.NORMAL, 70, 1);
    }

    @Override
    protected double calcBaseDamage(Pokemon att, Pokemon def) {
        double damage = super.calcBaseDamage(att, def);
        Status s = att.getCondition();
        if (s == Status.BURN || s == Status.POISON || s == Status.PARALYZE) {
            damage = damage * 2;
        }
        return damage;
    }

    @Override
    protected String describe() {
        return "бьёт Facade";
    }
}