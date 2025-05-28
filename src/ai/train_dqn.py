import numpy as np
import os
import json
import torch
import time
import glob
from src.ai.flappy_env import FlappyBirdEnv
from src.ai.dqn_agent import DQNAgent
from src.ai.flappy_headless import FlappyHeadless

LOG_PATH = os.path.join("logs", "train_log.jsonl")
CKPT_DIR = "checkpoints"
CKPT_FREQ = 3000  # Save every 1000 episodes

def save_checkpoint(agent, episode):
    os.makedirs(CKPT_DIR, exist_ok=True)
    ckpt = {
        'model_state_dict': agent.model.state_dict(),
        'optimizer_state_dict': agent.optimizer.state_dict(),
        'epsilon': agent.epsilon,
        'episode': episode
    }
    torch.save(ckpt, os.path.join(CKPT_DIR, f"dqn_ep{episode}.pt"))

def load_latest_checkpoint(agent):
    ckpt_files = glob.glob(os.path.join(CKPT_DIR, "dqn_ep*.pt"))
    if not ckpt_files:
        return 0  # No checkpoint found, start from episode 1
    latest_ckpt = max(ckpt_files, key=os.path.getctime)
    ckpt = torch.load(latest_ckpt)
    agent.model.load_state_dict(ckpt['model_state_dict'])
    agent.optimizer.load_state_dict(ckpt['optimizer_state_dict'])
    agent.epsilon = ckpt.get('epsilon', agent.epsilon)
    print(f"Loaded checkpoint: {latest_ckpt}")
    return ckpt.get('episode', 0)

def train(num_episodes=100000):
    game = FlappyHeadless()
    env = FlappyBirdEnv(game)
    agent = DQNAgent(state_dim=env.state_dim, action_dim=len(env.action_space))

    os.makedirs(CKPT_DIR, exist_ok=True)
    start_episode = load_latest_checkpoint(agent) + 1

    for episode in range(start_episode, num_episodes + 1):
        state = env.reset()
        total_reward = 0
        done = False
        step = 0
        while not done:
            action = agent.select_action(state)
            next_state, reward, done, _ = env.step(action)
            agent.store(state, action, reward, next_state, done)
            agent.train()
            state = next_state
            total_reward += reward
            step += 1
        print(f"Episode {episode}: Total Reward = {total_reward}")
        # Save checkpoint
        if episode % CKPT_FREQ == 0:
            save_checkpoint(agent, episode)

if __name__ == "__main__":
    train(100000)  # Run 10000 episodes for training 