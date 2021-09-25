package micronaut.gol;

import javax.inject.Singleton;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import java.util.UUID;

@Singleton
public class InMemoryGameRepository implements GameRepository {

    private Map<UUID, Game> games = new HashMap<>();

    @Override
    public Optional<Game> findById(UUID id) {
        return Optional.ofNullable(games.get(id));
    }

    @Override
    public Game save(Game game) {
        UUID id = game.getId();

        if (id == null) {
            do {
                id = UUID.randomUUID();
            } while (games.containsKey(id));
            game.setId(id);
        }

        games.put(id, game);
        return games.get(id);
    }

}
