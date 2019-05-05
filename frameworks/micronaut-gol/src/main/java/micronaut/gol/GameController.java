package micronaut.gol;

import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Post;

@Controller("/games")
public class GameController {

    @Post
    public Game create() {
        return new Game(10, 10);
    }
}
