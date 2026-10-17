package lab2;

import pokemons.*;
import ru.ifmo.se.pokemon.*;

public class Main {
    public static void main(String[] args) {
        Battle b = new Battle();
        Pokemon p1 = new Golett("Mini Rock", 1);
        Pokemon p2 = new Golurk("Big Boss", 43);
        Pokemon p3 = new Floette("Flower Knight", 19);
        Pokemon p4 = new Flabebe("Flower", 1);
        Pokemon p5 = new Florges("Flower Queen", 19);
        Pokemon p6 = new Thundurus("Pokemon God", 1);
        b.addAlly(p1);
        b.addAlly(p2);
        b.addFoe(p3);
        b.addFoe(p4);
        b.addFoe(p5);
        b.addFoe(p6);
        b.go();
    }
}
