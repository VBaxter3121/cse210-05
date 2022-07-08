import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, player):
        super().__init__()
        self._points = 0
        self._player = player
        self.show_points()
        if self._player == "player2":
            self.set_position(Point(0, constants.MAX_Y - 15))

    def show_points(self):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        if self._player == "player1":
            self.set_text(f"Score: {constants.PLAYER1_SCORE}")
        if self._player == "player2":
            self.set_text(f"Score: {constants.PLAYER2_SCORE}")