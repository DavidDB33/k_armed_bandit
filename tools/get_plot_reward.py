import sys
import statistics
import matplotlib as mpl
import matplotlib.pyplot as plt

value_lists = []
min_ylim = 0
max_ylim = 0

for filename in sys.argv[1:]:
    reward_mean_list = [0]
    reward_total = 0
    step = 1
    with open(filename, 'r') as f:
        line = f.readline()
        values = list(map(int, line.split(',')))
        for line in f:
            values = list(map(float, line.split(',')))
            _, reward = [(i,x) for i, x in enumerate(values) if x != 0][0]
            reward_total += reward
            reward_mean_list.append(reward_total/step)
            step += 1
    min_ylim = min(min_ylim, min(reward_mean_list))
    max_ylim = max(max_ylim, max(reward_mean_list))
    value_lists.append(reward_mean_list)


def plt_init():
    global plt
    fig = plt.figure()
    fig.set_size_inches(fig.get_size_inches()*4)


# Set global config
mpl.rcParams['axes.linewidth'] = 3
mpl.rc('font', size=26)

plt_init()
plt.ylabel('average reward')
plt.xlabel('steps')
plt.ylim(min_ylim, max_ylim+0.5)
for filename, values in zip(sys.argv[1:], value_lists):
    plt.plot(values, label=filename.split('.')[0])
plt.legend()
plt.show()
