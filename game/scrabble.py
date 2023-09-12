from models.configuration import Board, BagTiles, Player, tiles


class ScrabbleGame:

    def __init__(self, players_count):

        self.board = Board()
        self.bag_tiles = BagTiles(tiles)
        self.players = []

        for _ in range(players_count):
            self.players.append(Player())