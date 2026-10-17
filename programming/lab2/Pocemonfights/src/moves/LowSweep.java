package moves;

import ru.ifmo.se.pokemon.*;

public final class LowSweep extends PhysicalMove {
    public LowSweep() {
        super(Type.FIGHTING, 65, 1);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        p.setMod(Stat.SPEED, -1);
    }

    @Override
    protected String describe() {
        return "делает подсечку Low Sweep";
    }
}