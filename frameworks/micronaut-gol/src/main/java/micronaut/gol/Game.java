package micronaut.gol;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.*;

import static java.util.stream.Collectors.toList;
import static lombok.AccessLevel.PACKAGE;

@Getter
@NoArgsConstructor
@Setter(PACKAGE) // for jackson and the GameRepository
public class Game {

    public static final char ALIVE = '1';
    public static final char DEAD = '0';
    private static final String GOL_STATES = new String(new char[] {DEAD, ALIVE});
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

    public Game tick() {
        char[][] board = stringToBoard(this.board);

        Game newGame = new Game();
        newGame.setId(id);
        newGame.setBoard(boardToString(tick(board)));
        newGame.setAgeInTicks(ageInTicks + 1);

        return newGame;
    }

    private static char[][] tick(char[][] board) {
        char[][] newBoard = new char[board.length][];

        for (int y = 0; y < board.length; y++) {
            newBoard[y] = new char[board[y].length];
            for (int x = 0; x < board[y].length; x++) {
                int aliveNeighbors = countAliveNeighbors(board, x, y, board[y].length, board.length);

                if (board[y][x] == DEAD && aliveNeighbors == 3) {
                    newBoard[y][x] = ALIVE; // birth
                } else if (board[y][x] == ALIVE && (aliveNeighbors == 2 || aliveNeighbors == 3)) {
                    newBoard[y][x] = ALIVE; // survival
                } else if (board[y][x] == ALIVE && aliveNeighbors < 2) {
                    newBoard[y][x] = DEAD; // loneliness
                } else if (board[y][x] == ALIVE && aliveNeighbors > 3) {
                    newBoard[y][x] = DEAD; // overcrowd
                } else {
                    newBoard[y][x] = board[y][x];
                }
            }
        }

        return newBoard;
    }

    private static int countAliveNeighbors(char[][] board, int x, int y, int width, int height) {
        int alive = 0;

        int[][] possiblePositions = new int[][] {{x-1, y-1}, {x, y-1}, {x+1, y-1},
                                                 {x-1, y},             {x+1, y},
                                                 {x-1, y+1}, {x, y+1}, {x+1, y+1}};

        for (int pos = 0; pos < possiblePositions.length; pos++) {
            int possibleX = possiblePositions[pos][0];
            int possibleY = possiblePositions[pos][1];

            if (possibleX >= 0 && possibleX < width && possibleY >= 0 && possibleY < height) {
                if (board[possibleY][possibleX] == ALIVE) {
                    alive++;
                }
            }
        }

        return alive;
    }

    private String boardToString(char[][] board) {
        List<String> lines = new ArrayList<>();

        for (int row = 0; row < board.length; row++) {
            lines.add(new String(board[row]));
        }

        return String.join("\n", lines);
    }

    private char[][] stringToBoard(String rendered) {
        String[] lines = rendered.split("\\n");
        char[][] board = new char[lines.length][];
        for (int line = 0; line < lines.length; line++) {
            board[line] = lines[line].toCharArray();
        }

        return board;
    }

}
