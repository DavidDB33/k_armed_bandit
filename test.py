from pprint import pprint

import penv
from penv import Penv
from rl_dir import RL
from pers import Persistance

num_arms = 10
env = Penv(num_arms)

for step in range(num_arms):
    info = env.info()
    print("--> #{} bandit. Mean: {}".format(step, info[step].mean))
    pprint([env.step(step) for _ in range(10)])
    print()

Q = Persistance()
rl = RL(1, num_arms, Q)
state = 0
action = 0
value = 0.5
new_action = 4
new_value = 4.0
rl.set(state, action, value)

s_a_value = rl.get_action_value(state, action)

s_best_value = rl.get_best_action(state)
rl.update(state, new_action, new_value)

print("action: {}".format(s_a_value))
print("best_action: {}".format(s_best_value))
print("an action: {}".format(rl.get_action_value(state, new_action)))
pprint(list(rl.get_actions_values(state)))
