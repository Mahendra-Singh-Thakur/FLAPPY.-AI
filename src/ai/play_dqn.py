import torch
import pygame
import time
from src.flappy import Flappy
from src.ai.dqn_agent import DQNAgent
from src.ai.flappy_env import FlappyBirdEnv
import glob
import os

# Automatically find the latest checkpoint
CKPT_DIR = "model"
def get_latest_checkpoint():
    ckpt_files = glob.glob(os.path.join(CKPT_DIR, "flappy_dqn_v2.pt"))
    if not ckpt_files:
        # Try to find any .pt file in the model directory
        ckpt_files = glob.glob(os.path.join(CKPT_DIR, "*.pt"))
    if not ckpt_files:
        raise FileNotFoundError(f"No checkpoint found in '{CKPT_DIR}/' directory.")
    return max(ckpt_files, key=os.path.getctime)


def main():
    # Set up game and environment
    game = Flappy()
    env = FlappyBirdEnv(game)
    agent = DQNAgent(state_dim=env.state_dim, action_dim=len(env.action_space))
    
    # Load latest checkpoint
    ckpt_path = get_latest_checkpoint()
    checkpoint = torch.load(ckpt_path, map_location=agent.device)
    agent.model.load_state_dict(checkpoint['model_state_dict'])
    agent.epsilon = 0.0  # Always exploit
    print(f"Loaded checkpoint: {ckpt_path}")

    state = env.reset()
    done = False
    total_reward = 0

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        action = agent.select_action(state)
        next_state, reward, done, _ = env.step(action)
        state = next_state
        total_reward += reward
        # print(f"Reward: {reward}")
        # Render the game
        # time.sleep(1 / 30)  # 30 FPS

    print(f"Game over! Total reward: {total_reward}")

if __name__ == "__main__":
    main() 