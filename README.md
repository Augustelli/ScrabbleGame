# Scrabble CLI

The Scrabble Game project is a Python-based implementation of the classic word game, Scrabble. It allows users to enjoy this popular word game on their computers. Players can take turns forming words on a virtual game board, earning points based on the letters used and their placement on the board. The game provides features like scoring, tile exchange, supports multiple players and save current game.

With this project, users can relish the fun and challenge of Scrabble without the need for physical game boards and tiles. It's a great way to sharpen vocabulary and strategic thinking while competing with friends or AI opponents.

The project is an excellent way to learn Python programming, as it covers various aspects of game development, including user input, data structures, and logical algorithms.

Have fun playing Scrabble on your computer with this project!
## Screenshots or Examples

![Example 1](screenshot1.png)
![Example 2](screenshot2.png)

## How to Play Scrabble

Scrabble is a word game where players use lettered tiles to create words on a game board. The objective is to score more points than your opponents by forming valid words.

**Setup:**

    The game is typically played by 2 to 4 players.
    Each player takes seven lettered tiles from the tile bag and places them on their tile rack.
    Decide who goes first. This player will place the first word on the board.
    The game board consists of a grid with premium score spaces. Place the board in the center of the playing area.

**Gameplay:**

Players take turns clockwise.
On your turn, you can:
1. Form a word on the board using your tiles.
2. Add tiles to a word already on the board.
3. Exchange some or all of your tiles by playing 'CHANGE'
4. Pass your turn by playing 'PASS' or press ENTER

To create words, tiles must be placed horizontally or vertically on the board. The first word must cover the center (star) square.
Words must be connected to other words already on the board. To play a word you must specify the position of the first letter with the following format: COLUMN ROW ORIENTATION. It is to play the first word or continuation of it. The complete word to be played must always be specified. If only one letter is specified, it will be considered the word to be played.
Tiles can be placed either across or down, and they can be used to form multiple words in a single turn.
Words must be found in a standard dictionary (Spanish).
Score points based on the letters' values and any premium squares on which the letters are placed.
End your turn by drawing new tiles to replenish your rack. The tile bag provides replacements.

**Scoring:**

Each tile has a point value.
Premium squares include Double Letter Score (DL), Triple Letter Score (TL), Double Word Score (DW), and Triple Word Score (TW).
Score is calculated based on the word formed and any premium square multipliers.

**End of the Game:**
The game ends when one of these conditions is met:

- All players consecutively pass twice.
- A player uses all their tiles, and no tiles remain in the bag.

**Winning:**

The player with the highest score at the end of the game wins.

Remember, Scrabble is a game of strategy, vocabulary, and skill. Players can challenge a word's validity, so it's essential to agree on a dictionary or word source before starting. Have fun forming words and competing against your friends or family in this classic word game!

For more detailed rules and scoring, consider referring to the official Scrabble rulebook or the specific rules of the version you're playing. Enjoy your Scrabble game!

To learn how to play Scrabble, refer to the [official Scrabble rules](https://en.wikipedia.org/wiki/Scrabble)

## Requierements
- Python 3.x.x
- pip
- Docker 24.0.5
- Docker Compose
- Code Climate Analyser
## How to Get Started, Clone, and Run the Application

1. Clone proyect
```bash
# Clone the proyect
git clone https://github.com/yourusername/yourproject.git
```


2. Install dependencies
```bash
# Create virtual environment
python3 -m venv venv
# Activate virtualenv
source venv/bin/activate
# Install dependencies
pip install -r requirements.txt
```
3. Run aplication
```bash
# Note to run the aplicaction you must be on proyect root folder
python3 -m game.main
```

4. Run tests
```bash
# Note to run the tests you must be on proyect root folder
python3 -m unittest

# To run converage
coverage run -m unittest

# To see converage report
coverage report -m
```

## Docker and Docker Compose
Running the Project with Docker:

To run the project using Docker, follow these steps:

1. Building the Docker Image:

Navigate to the project's root directory.
Execute the following command to build the Docker image:

```bash
docker build -t scrabble .
```

2. Running Docker Compose:

With the Docker image ready, the next step is to deploy the application and the Redis service together.
Execute the following Docker Compose command:

```bash
docker compose up -d

# Check ID to enter the container
docker ps -a
# Enter container with id ex: ced2c597190e
docker exec -it ced2c597190e sh
```
Note: Ensure that Docker and Docker Compose are installed on your system before proceeding.

3. Ussing the application inside the container

Inside the container, while being in the root folder of the project, run the following command to start the application we can
- Run unittest
- Run coverage and its report
- Play the game

```bash
# To run the tests
python3 -m unittest

# To run coverage and its report
coverage run -m unittest && coverage report -m

# To play the game
python3 -m game.main
```

# Author
- **Mancuso Augusto Tomás**
- Email: **a.mancuso@alumno.um.edu.ar**

## Estado del Repositorio

### Rama Principal (Main)
[![CircleCI - Main](https://circleci.com/gh/um-computacion-tm/scrabble-2023-Augustelli/tree/main.svg?style=svg)](https://circleci.com/gh/um-computacion-tm/scrabble-2023-Augustelli/tree/main)

## Calidad del Código

### Mantenibilidad
[![Maintainability](https://api.codeclimate.com/v1/badges/8b7b07672b40b37ff06a/maintainability)](https://codeclimate.com/github/um-computacion-tm/scrabble-2023-Augustelli/maintainability)

