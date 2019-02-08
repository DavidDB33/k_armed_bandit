# No std libs imported

from penv import Penv
from rl_dir import RL
from pers import Persistance

num_arms = 10
env = Penv(num_arms)
q = Persistance()
q.flush()

rl = RL(s_dim = 1, a_dim = num_arms, Q = q)

rl.update(s, a, v)

