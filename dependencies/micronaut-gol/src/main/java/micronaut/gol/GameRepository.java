package micronaut.gol;

import java.util.Optional;
import java.util.UUID;

public interface GameRepository {

    Optional<Game> findById(UUID id);

    Game save(Game game);

}
