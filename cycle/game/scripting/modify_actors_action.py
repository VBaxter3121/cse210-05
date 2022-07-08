from game.scripting.action import Action

class ModifyActorsAction(Action):
    """
    """

    def __init__(self):
        """
        """
        self._counter = 0
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the modify actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        update_actions = script.get_actions("update")
        handle_collisions_action = update_actions[1]
        self._is_game_over = handle_collisions_action.is_game_over()
        if not self._is_game_over:
            self._counter += 1

            if self._counter >= 20:
                self._counter = 0

                cycles = cast.get_actors("cycles")
                for cycle in cycles:
                    cycle.grow_trail(1)