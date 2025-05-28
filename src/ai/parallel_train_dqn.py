import numpy as np
import os
import json
import torch
import glob
from multiprocessing import Process, Queue
from src.ai.flappy_env import FlappyBirdEnv
from src.ai.dqn_agent import DQNAgent
from src.ai.flappy_headless import FlappyHeadless

LOG_PATH = os.path.join("logs", "parallel_train_log.jsonl")
CKPT_DIR = "checkpoints"
CKPT_FREQ = 10
NUM_ENVS = 6


def worker(env_cls, queue, max_steps=1000):
    env = FlappyBirdEnv(env_cls())
    for episode in range(1, max_steps + 1):
        state = env.reset()
        done = False
        while not done:
            action = np.random.choice([0, 1])
            next_state, reward, done, _ = env.step(action)
            # Get the score from the underlying game
            score = int(getattr(env.game.score, 'score', 0))
            queue.put((episode, state, action, reward, next_state, done, score))
            state = next_state


def save_checkpoint(agent, episode):
    os.makedirs(CKPT_DIR, exist_ok=True)
    ckpt = {
        'model_state_dict': agent.model.state_dict(),
        'optimizer_state_dict': agent.optimizer.state_dict(),
        'epsilon': agent.epsilon,
        'episode': episode
    }
    torch.save(ckpt, os.path.join(CKPT_DIR, f"dqn_parallel_ep{episode}.pt"))


def parallel_train(num_episodes=10000):
    agent = DQNAgent(state_dim=5, action_dim=2)
    queue = Queue()
    def make_env():
        return FlappyHeadless()
    processes = [Process(target=worker, args=(FlappyHeadless, queue, num_episodes // NUM_ENVS)) for _ in range(NUM_ENVS)]
    for p in processes:
        p.start()

    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as log_file:
        step = 0
        episode = 0
        total_reward = 0
        current_episode = 1
        while episode < num_episodes:
            if not queue.empty():
                ep, state, action, reward, next_state, done, score = queue.get()
                agent.store(state, action, reward, next_state, done)
                agent.train()
                # Log step
                log_entry = {
                    "episode": ep,
                    "step": step,
                    "state": state.tolist(),
                    "action": int(action),
                    "reward": float(reward),
                    "next_state": next_state.tolist(),
                    "done": bool(done),
                    "score": int(score)
                }
                log_file.write(json.dumps(log_entry) + "\n")
                total_reward += reward
                step += 1
                if done:
                    episode += 1
                    print(f"Episode {ep}: Total Reward = {total_reward}")
                    total_reward = 0
                    if episode % CKPT_FREQ == 0:
                        save_checkpoint(agent, episode)
        for p in processes:
            p.terminate()

if __name__ == "__main__":
    parallel_train(10000) 