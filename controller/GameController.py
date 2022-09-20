from ..view.GameView import GameView

class Game:

    def __init__(self):
        self.view = GameView()
        self.game_objects = None

    def game_loop(self):
        self.view.update(self.game_objects)

