import os
if os.environ.get("FLAPPY_HEADLESS", "0") == "1":
    os.environ["SDL_VIDEODRIVER"] = "dummy"
import pygame
from src.flappy import Flappy
from src.entities.player import Player, PlayerMode
from src.entities.pipe import Pipes
from src.entities.background import Background
from src.entities.floor import Floor
from src.entities.score import Score

class FlappyHeadless(Flappy):
    def __init__(self):
        super().__init__()
        self._just_passed_pipe = False
        self._game_over = False
        self._last_score = 0
        self._setup_headless()
        self._init_game_state()

    def _setup_headless(self):
        # Disable rendering and sound for headless mode
        try:
            pygame.display.iconify()  # Minimize window
        except Exception:
            pass
        for snd in [self.config.sounds.wing, self.config.sounds.hit, self.config.sounds.die]:
            try:
                snd.set_volume(0)
            except Exception:
                pass

    def _init_game_state(self):
        self.background = Background(self.config)
        self.floor = Floor(self.config)
        self.player = Player(self.config)
        self.pipes = Pipes(self.config)
        self.score = Score(self.config)
        self.player.set_mode(PlayerMode.NORMAL)
        self._just_passed_pipe = False
        self._game_over = False
        self._last_score = 0

    def reset(self):
        self._init_game_state()

    def tick(self):
        # Advance the game by one frame (no rendering)
        if self.player.collided(self.pipes, self.floor):
            self._game_over = True
            return
        # Check if player passed a pipe
        self._just_passed_pipe = False
        for pipe in self.pipes.upper:
            if self.player.crossed(pipe):
                self.score.add()
                self._just_passed_pipe = True
        self.background.tick()
        self.floor.tick()
        self.pipes.tick()
        self.score.tick()
        self.player.tick()
        # No pygame.display.update() or sleep

    def is_over(self):
        return self._game_over

    def player_just_passed_pipe(self):
        return self._just_passed_pipe 