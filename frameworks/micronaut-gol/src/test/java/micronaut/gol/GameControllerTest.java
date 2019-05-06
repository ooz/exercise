package micronaut.gol;

import io.micronaut.http.HttpRequest;
import io.micronaut.http.HttpResponse;
import io.micronaut.http.client.HttpClient;
import io.micronaut.http.client.annotation.Client;
import io.micronaut.runtime.server.EmbeddedServer;
import io.micronaut.test.annotation.MicronautTest;
import org.junit.jupiter.api.Test;

import javax.inject.Inject;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;

@MicronautTest
public class GameControllerTest {

    @Inject
    EmbeddedServer server;

    @Inject
    @Client("/")
    HttpClient client;

    Game game;
    String gameId;

    @Test
    public void should_create_initial_game_board() {
        whenGameIsCreated();

        thenGameBoardHasInitialSize();
    }

    @Test
    public void should_get_game_board() {
        // given
        should_create_initial_game_board();

        whenGameIsFetched();

        thenGameBoardHasInitialSize();
    }

    @Test
    public void should_tick_game_board() {
        // given
        should_create_initial_game_board();

        whenGameIsTicked();

        thenGameBoardHasTicked();
    }

    private void whenGameIsCreated() {
        HttpResponse<Game> response = client.toBlocking().exchange(
                HttpRequest.POST("/games", ""),
                Game.class);

        game = response.getBody().get();
    }

    private void whenGameIsFetched() {
        HttpResponse<Game> response = client.toBlocking().exchange(
            HttpRequest.GET("/games/" + gameId),
        Game.class);

        game = response.getBody().get();
    }

    private void whenGameIsTicked() {
        HttpResponse<Game> response = client.toBlocking().exchange(
                HttpRequest.POST("/games/" + gameId, ""),
                Game.class);

        game = response.getBody().get();
    }

    private void thenGameBoardHasInitialSize() {
        gameId = game.getId().toString();
        assertFalse(gameId.isEmpty());

        int columns = 10;
        int rows = 10;
        int newlines = rows - 1;
        int expectedBoardCharacterCount= columns * rows + newlines;
        assertEquals(expectedBoardCharacterCount, game.getBoard().length());

        assertEquals(0, game.getAgeInTicks());
    }

    private void thenGameBoardHasTicked() {
        gameId = game.getId().toString();
        assertFalse(gameId.isEmpty());

        int columns = 10;
        int rows = 10;
        int newlines = rows - 1;
        int expectedBoardCharacterCount= columns * rows + newlines;
        assertEquals(expectedBoardCharacterCount, game.getBoard().length());

        assertEquals(1, game.getAgeInTicks());
    }
}
