package pokemons;

import moves.*;
import ru.ifmo.se.pokemon.*;

public final class Thundurus extends Pokemon{
    public Thundurus(String name, int level) {
        super(name, level);
        setType(Type.ELECTRIC, Type.FLYING);
        setStats(79, 115, 70, 125, 80, 111);
        setMove(new FocusBlast(), new ChargeBeam(), new Thunder(), new Confide());
    }
}