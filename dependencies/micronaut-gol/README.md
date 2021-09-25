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

## Lessons learned

* Micronaut having problems injecting/resolving beans despite everything looking fine? Phantom error! Clean and rebuild!
* Not having exercised GoL in a while, I wasted unnecessary time getting a basic implementation. Errors due to Java primitives and primitive obsession
* It was fun to do this with micronaut. I like the expressive, low bloat approach

