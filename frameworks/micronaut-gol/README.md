# Micronaut Game of Life

Minimal test project for micronaut using the Game of Life (GoL) kata.

Exposes a JSON REST API that allows you to create, get and update GoL boards.
The application is stateless, all created boards just live in-memory.

## Development

```
./gradlew idea
```

* This project uses lombok, please install the lombok plugin in IntelliJ Idea

## Run

```
./gradlew run
```

Possible operations:

* `POST /games` - create a new GoL
* `GET /games/{id}` - fetch details of a specific GoL
* `POST /games/{id}` - perform one tick for this GoL
