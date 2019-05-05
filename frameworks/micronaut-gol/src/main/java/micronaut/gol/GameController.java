package micronaut.gol;

import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.Post;

import javax.inject.Inject;
import java.util.UUID;

@Controller("/games")
public class GameController {

    @Inject
    private GameRepository gameRepository;

    @Post
    public Game create() {
        return gameRepository.save(new Game(10, 10));
    }

    @Get("/{id}")
    public Game get(UUID id) {
        return gameRepository
                .findById(id)
                .orElse(null);
    }
}
