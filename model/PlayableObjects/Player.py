from PlayerActions import Playeractions


class Player:

    def __init__(self):
        self.state = Playeractions.IDLE
        self.position = None

        pass

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    def move(self):
        pass


