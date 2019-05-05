package micronaut.gol;

import org.junit.jupiter.api.Test;

import static micronaut.gol.Game.ALIVE;
import static micronaut.gol.Game.DEAD;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class GameTest {

    private Game game;

    @Test
    public void should_birth() {
        givenThreeCellDeadCenterGame();

        whenTicking();

        assertEquals("000\n010\n000", game.getBoard());
        assertEquals(ALIVE, charInCenter(game));
        assertEquals(1, game.getAgeInTicks());
    }

    @Test
    public void should_survive_with_2_neighbors() {
        givenThreeCellAliveCenterGame();

        whenTicking();

        assertEquals(ALIVE, charInCenter(game));
        assertEquals(1, game.getAgeInTicks());
    }

    @Test
    public void should_survive_with_3_neighbors() {
        givenFourCellAliveCenterGame();

        whenTicking();

        assertEquals(ALIVE, charInCenter(game));
        assertEquals(1, game.getAgeInTicks());
    }

    @Test
    public void should_kill_lonely_cell() {
        givenLonelyCellCenterGame();

        whenTicking();

        assertEquals(DEAD, charInCenter(game));
        assertEquals(1, game.getAgeInTicks());
    }

    @Test
    public void should_kill_overcrowded_cell() {
        givenOvercrowdedAliveCenterGame();

        whenTicking();

        assertEquals(DEAD, charInCenter(game));
        assertEquals(1, game.getAgeInTicks());
    }

    private void givenThreeCellDeadCenterGame() {
        game = new Game();
        game.setBoard("100\n001\n010");
        game.setAgeInTicks(0);
    }

    private void givenThreeCellAliveCenterGame() {
        game = new Game();
        game.setBoard("000\n011\n100");
        game.setAgeInTicks(0);
    }
    private void givenFourCellAliveCenterGame() {
        game = new Game();
        game.setBoard("010\n110\n001");
        game.setAgeInTicks(0);
    }

    private void givenLonelyCellCenterGame() {
        game = new Game();
        game.setBoard("000\n010\n000");
        game.setAgeInTicks(0);
    }

    private void givenOvercrowdedAliveCenterGame() {
        game = new Game();
        game.setBoard("011\n110\n101");
        game.setAgeInTicks(0);
    }

    private void whenTicking() {
        game = game.tick();
    }

    private char charInCenter(Game game) {
        return game.getBoard().split("\\n")[1].charAt(1);
    }
}
