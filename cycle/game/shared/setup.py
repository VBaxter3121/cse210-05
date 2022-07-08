# import random
# import constants
# from game.casting.actor import Actor
# from game.shared.point import Point


# class Food(Actor):
#     """
#     A tasty item that snakes like to eat.
    
#     The responsibility of Food is to select a random position and points that it's worth.

#     Attributes:
#         _points (int): The number of points the food is worth.
#     """
#     def __init__(self):
#         "Constructs a new Food."
#         super().__init__()
#         self._points = 0
#         self.set_text("@")
#         self.set_color(constants.RED)
#         self.reset()
        
#     def reset(self):
#         """Selects a random position and points that the food is worth."""
#         self._points = random.randint(1, 8)
#         x = random.randint(1, constants.COLUMNS - 1)
#         y = random.randint(1, constants.ROWS - 1)
#         position = Point(x, y)
#         position = position.scale(constants.CELL_SIZE)
#         self.set_position(position)
        
#     def get_points(self):
#         """Gets the points the food is worth.
        
#         Returns:
#             points (int): The points the food is worth.
#         """
#         return self._points

from game.casting.cycle import Cycle
from game.casting.score import Score

class Setup():
    """
    """

    def __init__(self):
        """
        """
        self._first_time = True
        
    def replay(self, cast):
        """
        """
        cast.clear_cast()
        cycle1 = Cycle("player1")
        cycle2 = Cycle("player2")
        cast.add_actor("cycles", cycle1)
        cast.add_actor("cycles", cycle2)
        score1 = Score("player1")
        score2 = Score("player2")
        cast.add_actor("scores", score1)
        cast.add_actor("scores", score2)