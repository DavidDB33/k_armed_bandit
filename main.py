import random

from penv import Penv
from rl_dir import RL
from pers import Persistance

num_arms = 10
env = Penv(num_arms)
q = Persistance()
q.flush()

rl = RL(s_dim = 1, a_dim = num_arms, Q = q)
rl.DEBUG = True
q.DEBUG = True
env.DEBUG = True
s = 0
alpha = 0.01
actions = list(range(num_arms))

step = 0
while step < 10000:
    exploration = random.random()
    if exploration < alpha:
        a = random.choice(actions)
    else:
        a = rl.get_best_action(s)
    r = env.step(a)
    rl.update(s, a, r)
    step += 1

best = max(enumerate(env.info()), key = lambda x: x[1].mean)
print(best)
