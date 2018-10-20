import numpy as np
import gym

parameters = np.random.rand(4)*2-1
env = gym.make('CartPole-v0')
def run_episode(env, parameters):
    observation = env.reset()
    total_reward = 0
    for _ in range(1000):
        env.render()
        action = 0 if np.matmul(parameters, observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        total_reward += reward
        if done:
            break
        return total_reward
    
def random_search():
    bestparams = None
    bestreward = 0
    for _ in xrange(10000):
        parameters = np.random.rand(4)*2-1
        reward = run_episode(env, parameters)
        if reward > bestreward:
            bestreward = reward
            bestparams = parameters
            if reward == 200:
                break

def hill_climbing():
    noise_scaling = 0.1
    parameters = np.random.rand(4)*2-1
    bestreward = 0
    for _ in xrange(10000):
        newparams = parameters + (np.random.rand(4)*2-1)*noise_scaling
        reward = 0
        run = run_episode(env, parameters)
        print(run)
        if reward > bestreward:
            bestreward = reward
            parameters = newparams
            if reward == 200:
                break

hill_climbing()
# if '__name__' == '__main__':