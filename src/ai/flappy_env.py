import numpy as np

class FlappyBirdEnv:
    def __init__(self, game):
        """
        game: an instance of the Flappy game logic (should provide access to player, pipes, etc.)
        """
        self.game = game
        self.state_dim = 5
        self.action_space = [0, 1]  # 0: do nothing, 1: flap

    def reset(self):
        """Resets the game and returns the initial state."""
        self.game.reset()
        return self._get_state()

    def step(self, action):
        """
        Takes an action (0 or 1), advances the game, and returns (next_state, reward, done, info)
        """
        if action == 1:
            self.game.player.flap()
        self.game.tick()  # Advance the game by one frame
        next_state = self._get_state()
        reward = self._get_reward()
        done = self.game.is_over()
        info = {}
        return next_state, reward, done, info

    def _get_state(self):
        """
        Returns the current state as a 5-dimensional normalized numpy array:
        [player_y, player_vel, pipe_dx, pipe_top_y, pipe_bottom_y]
        """
        player = self.game.player
        pipes = self.game.pipes
        floor = self.game.floor
        window = self.game.config.window

        # Find the next pipe
        next_pipe = None
        for pipe in pipes.upper:
            if pipe.x + pipe.w > player.x:
                next_pipe = pipe
                break
        if next_pipe is None:
            next_pipe = pipes.upper[0]

        # Normalization factors
        max_y = floor.y
        max_vel = 10.0  # Assume max abs velocity
        max_dx = window.width
        max_pipe_y = floor.y

        player_y = player.y / max_y
        player_vel = (player.vel_y + max_vel) / (2 * max_vel)  # Map [-max_vel, max_vel] to [0, 1]
        pipe_dx = (next_pipe.x - player.x) / max_dx
        pipe_top_y = next_pipe.y / max_pipe_y
        pipe_bottom_y = (next_pipe.y + pipes.pipe_gap) / max_pipe_y

        state = np.array([
            player_y,
            player_vel,
            pipe_dx,
            pipe_top_y,
            pipe_bottom_y
        ], dtype=np.float32)
        return state

    def _get_reward(self):
        """
        Returns the reward for the current state.
        +1 for passing a pipe, -1 for dying, 0 otherwise.
        """
        if self.game.is_over():
            return -1.0
        if self.game.player_just_passed_pipe():
            return 1.0
        return 0.0 