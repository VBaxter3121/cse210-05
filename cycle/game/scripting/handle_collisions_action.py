import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self, keyboard_service, setup):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._player1_win = False
        self._player2_win = False
        self._keyboard_service = keyboard_service
        self._setup = setup

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
        else:
            if self._keyboard_service.is_key_down('r'):
                self._setup.replay(cast)
                self._is_game_over = False
                self._player1_win = False
                self._player2_win = False

    # def _handle_food_collision(self, cast):
    #     """Updates the score nd moves the food if the snake collides with the food.
        
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     score = cast.get_first_actor("scores")
    #     food = cast.get_first_actor("foods")
    #     snake = cast.get_first_actor("snakes")
    #     head = snake.get_head()

    #     if head.get_position().equals(food.get_position()):
    #         points = food.get_points()
    #         snake.grow_tail(points)
    #         score.add_points(points)
    #         food.reset()

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycles = cast.get_actors("cycles")
        head1 = cycles[0].get_segments()[0]
        head2 = cycles[1].get_segments()[0]
        segments = cycles[0].get_segments()[1:]
        segments2 = cycles[1].get_segments()[1:]
        segments = segments + segments2
        
        for segment in segments:
            if head1.get_position().equals(segment.get_position()):
                self._player2_win = True
                self._is_game_over = True

            if head2.get_position().equals(segment.get_position()):
                self._player1_win = True
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycles = cast.get_actors("cycles")
            segments = cycles[0].get_segments()
            segments2 = cycles[1].get_segments()
            segments = segments + segments2
            # food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            scores = cast.get_actors("scores")
            if self._player1_win == True:
                message.set_text("Player 1 Wins! Press 'R' to play again")
                constants.PLAYER1_SCORE += 1
            elif self._player2_win == True:
                message.set_text("Player 2 Wins! Press 'R' to play again")
                constants.PLAYER2_SCORE += 1
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)

    def is_game_over(self):
        """
        """
        return self._is_game_over