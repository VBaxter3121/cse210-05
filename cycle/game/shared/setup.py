from game.casting.cycle import Cycle
from game.casting.score import Score

class Setup():
    """
    A series of setup commands.

    The responsability of Setup is to assist with the first time set up,
    as well as to handle resetting the game between multiple games in the
    same session.

    Attributes:
        _first_time (bool): Whether this is the first game since the program
        launched.
    """

    def __init__(self):
        """Constructs a new instance of Setup"""
        self._first_time = True
        
    def replay(self, cast):
        """Clears all cast members, then creates new ones ready for a new game.
        
        Args:
            cast (Cast): The cast of actors in the game."""
        cast.clear_cast()
        cycle1 = Cycle("player1")
        cycle2 = Cycle("player2")
        cast.add_actor("cycles", cycle1)
        cast.add_actor("cycles", cycle2)
        score1 = Score("player1")
        score2 = Score("player2")
        cast.add_actor("scores", score1)
        cast.add_actor("scores", score2)