import java.util.Optional;

public class StreamNull {
    public static void main(String[] args) {
        var value = Optional.ofNullable("something")
            .map(v -> null)
            .stream()
            .map(v -> { throw new RuntimeException("this won't happen!"); })
            .findFirst()
            .orElse(null);

        assert value == null;
    }
}
