<img src="[images/flappybird.png](https://github.com/Mahendra-Singh-Thakur/FLAPPY_BIRD/blob/main/Screenshot%202025-05-28%20083438.png)" alt="Flappy Bird" width="200"/>


# FlapPyBird with DQN AI

This project is a clone of the classic Flappy Bird game built with Python and Pygame, extended with a Deep Q-Learning (DQN) based AI agent that learns to play the game.

## Project Structure

```
.gitignore
.pre-commit-config.yaml
.replit
LICENSE
Makefile
README.md
flappy.ico
main.py
pyproject.toml
screenshot1.png

assets/
├── audio/      # Game sound effects
└── sprites/    # Game visual assets

src/
├── ai/         # AI implementation (DQN, Environment, Training/Evaluation Scripts)
│   ├── __init__.py
│   ├── dqn_agent.py      # DQN Agent class
│   ├── flappy_env.py     # OpenAI Gym-like environment wrapper
│   ├── flappy_headless.py  # Headless game logic for faster training
│   ├── flappy_visual.py  # Visual game logic for evaluation/visual training
│   ├── parallel_train_dqn.py # Script for parallel training
│   └── train_dqn.py      # Script for single-environment training
├── entities/   # Game entities (Player, Pipes, Score, etc.)
│   ├── __init__.py
│   ├── background.py
│   ├── entity.py
│   ├── floor.py
│   ├── game_over.py
│   ├── pipe.py
│   ├── player.py
│   ├── score.py
│   └── welcome_message.py
├── utils/      # Utility modules (GameConfig, Images, Sounds, etc.)
│   ├── __init__.py
│   ├── constants.py
│   ├── game_config.py
│   ├── images.py
│   ├── sounds.py
│   ├── utils.py
│   └── window.py
└── flappy.py       # Main game logic (original human-playable version)
```

## Setup

1.  **Install Python 3.9+**
    Make sure you have a compatible version of Python installed.

2.  **Install Dependencies**
    Navigate to the project root in your terminal and run:
    ```bash
    pip install -r requirements.txt
    ```
    This will install `pygame`, `numpy`, and `torch`.

## Playing the Original Game

To play the classic Flappy Bird game manually:

Navigate to the project root in your terminal and run:

```bash
python main.py
```

**Controls:**

- **Up Arrow** or **Space**: Make the bird flap.
- **Esc**: Quit the game.

## AI Implementation (Deep Q-Learning)

The AI agent is implemented using Deep Q-Learning. It learns to play the game by interacting with the environment, receiving states, taking actions, and getting rewards.

### Components:

- **`dqn_agent.py`**: Defines the DQN neural network model and the agent's learning logic (epsilon-greedy action selection, experience replay, training step).
- **`flappy_env.py`**: An OpenAI Gym-like environment wrapper around the game logic, providing the state representation, handling actions, and calculating rewards.
  - **State Input**: A 5-dimensional normalized NumPy array representing the game state.
  - **Action Output**: An integer: `0` (do nothing) or `1` (flap).
  - **Reward**: +1 for passing a pipe, -1 for crashing, 0 otherwise.
- **`flappy_headless.py`**: A version of the game logic optimized for fast, headless training (no rendering or sound). Enabled when `FLAPPY_HEADLESS=1` environment variable is set.
- **`flappy_visual.py`**: A version of the game logic that includes rendering for visual training or evaluation.

## Training the AI

### Single-Environment Training:

Use `src/ai/train_dqn.py` for basic training.

To run **headless training** (recommended for speed):

```bash
# On Windows
set FLAPPY_HEADLESS=1
python -m src.ai.train_dqn

# On Linux/macOS
export FLAPPY_HEADLESS=1
python -m src.ai.train_dqn
```

To run **visual training** (for monitoring early stages):

```bash
python -m src.ai.train_dqn
```

- Training logs will be saved in `logs/train_log.jsonl` (if enabled). **Note:** Logging to file is currently disabled in `train_dqn.py` for speed.
- Model checkpoints will be saved periodically in the `checkpoints/` directory.
- Training will automatically resume from the latest checkpoint found.

### Parallel Training:

Use `src/ai/parallel_train_dqn.py` to train with multiple environments in parallel for faster data collection.

To run parallel training (headless):

```bash
# On Windows
set FLAPPY_HEADLESS=1
python -m src.ai.parallel_train_dqn

# On Linux/macOS
export FLAPPY_HEADLESS=1
python -m src.ai.parallel_train_dqn
```

- Parallel training logs are saved in `logs/parallel_train_log.jsonl`.
- Model checkpoints are saved in `checkpoints/` with a different naming convention (`dqn_parallel_ep*.pt`).

## Evaluating the Trained AI

To watch your trained AI agent play the original game visually:

Use `src/ai/play_dqn.py`.

```bash
python -m src.ai.play_dqn
```

- This script loads the latest checkpoint from `checkpoints/` (specifically looking for `dqn_ep1370.pt` based on current code, adjust `get_latest_checkpoint` if needed).
- The game window will open, and you will see the AI controlling the bird.

## Customization

- **Model Architecture**: Modify the `DQN` class in `dqn_agent.py`.
- **Hyperparameters**: Adjust agent hyperparameters (`gamma`, `lr`, `epsilon` schedule, etc.) in the `DQNAgent` class or training scripts.
- **Environment State/Reward**: Customize the state representation or reward function in `flappy_env.py`.
- **Checkpoint Frequency**: Change `CKPT_FREQ` in the training scripts.
- **Number of Parallel Environments**: Change `NUM_ENVS` in `parallel_train_dqn.py`.

---

Enjoy training and watching your AI play Flappy Bird!
