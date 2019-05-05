package micronaut.gol;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.UUID;

import static java.util.stream.Collectors.toList;
import static lombok.AccessLevel.PACKAGE;
import static lombok.AccessLevel.PRIVATE;

@Getter
@NoArgsConstructor(access = PRIVATE) // for jackson
@Setter(PACKAGE) // for jackson and the GameRepository
public class Game {

    private static final String GOL_STATES = "01";
    private static final Random RNG = new Random();

    @JsonProperty("_id")
    private UUID id;

    private String board;

    private int ageInTicks;

    private static List<String> randomLines(int count, int lineLength) {
        return Collections.nCopies(count, "").stream()
                .map(line -> randomLine(lineLength))
                .collect(toList());
    }

    private static String randomLine(int length) {
        StringBuilder line = new StringBuilder(length);

        for (int i = 0; i < length; i++) {
            line.append(GOL_STATES.charAt(RNG.nextInt(GOL_STATES.length())));
        }

        return line.toString();
    }

    public static Game random(int columns, int rows) {
        Game game = new Game();
        game.setBoard(String.join("\n", randomLines(rows, columns)));
        game.setAgeInTicks(0);
        return game;
    }

}
