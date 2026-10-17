package pokemons;

import moves.*;
import ru.ifmo.se.pokemon.*;

public final class Golurk extends Golett {
    public Golurk(String name, int level) {
        super(name, level);
        setStats(89, 124, 80, 55, 80, 55);
        addMove(new FlashCannon());
    }
}