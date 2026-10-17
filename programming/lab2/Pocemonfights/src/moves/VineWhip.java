package moves;

import ru.ifmo.se.pokemon.*;

public final class VineWhip extends PhysicalMove {
    public VineWhip() {
        super(Type.GRASS, 45, 1);
    }

    @Override
    protected String describe() {
        return "хлещет лозой Vine Whip";
    }
}