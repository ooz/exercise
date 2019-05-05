package micronaut.gol;

import io.micronaut.http.HttpRequest;
import io.micronaut.http.HttpResponse;
import io.micronaut.http.client.HttpClient;
import io.micronaut.http.client.annotation.Client;
import io.micronaut.runtime.server.EmbeddedServer;
import io.micronaut.test.annotation.MicronautTest;
import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.Test;

import javax.inject.Inject;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;

@MicronautTest
@Slf4j
public class GameControllerTest {

    @Inject
    EmbeddedServer server;

    @Inject
    @Client("/")
    HttpClient client;

    Game game;

    @Test
    public void should_create_initial_game_board() {
        whenGameIsCreated();

        thenGameBoardHasInitialSize();
    }

    private void whenGameIsCreated() {
        HttpResponse<Game> response = client.toBlocking().exchange(
                HttpRequest.POST("/games", ""),
                Game.class);

        game = response.getBody().get();

        log.info(game.toString());
    }

    private void thenGameBoardHasInitialSize() {
        assertFalse(game.getId().toString().isEmpty());

        int columns = 10;
        int rows = 10;
        int newlines = rows - 1;
        int expectedBoardCharacterCount= columns * rows + newlines;
        assertEquals(expectedBoardCharacterCount, game.getBoard().length());

        assertEquals(game.getAgeInTicks(), 0);
    }
}
