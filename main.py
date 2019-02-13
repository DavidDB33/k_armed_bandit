import os
import sys
import random
random.seed(1)

from penv import KArmedBandit
from rl_dir import RL
from pers import Persistance

num_arms = 10
max_step = 1000
epsilon = 0.1
initial_state = 0

filename_data = 'data.dat'
filename_log = 'action_taked.log'

if os.path.isfile(filename_data):
    with open(filename_data, 'r') as f:
        data = list(map(float, f.readlines()))
else:
    data = None
if len(sys.argv) > 1:
    filename_log = sys.argv[1]

env = KArmedBandit(num_arms, prob_arms = data, action_taked_filename = filename_log)
if not os.path.isfile(filename_data):
    env.store_data(filename_data)
q_table = Persistance()
q_table.flush()
rl = RL(s_dim = 1, a_dim = num_arms, Q = q_table)

rl.DEBUG = True
q_table.DEBUG = True
env.DEBUG = True

step = 0
while step < max_step:
    exploration = random.random()
    if exploration < epsilon:
        action = env.sample()
    else:
        action = rl.get_best_action(initial_state)
    next_state, reward, is_done = env.step(action)
    rl.update(initial_state, action, reward)
    step += 1

best = max(enumerate(env.info()), key = lambda x: x[1].mean)
print(best)
