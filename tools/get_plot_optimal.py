import sys
import statistics
import matplotlib.pyplot as plt

optimal = 0
optimal_taked_times = 0
optimal_percentage_step = []
step = 1
with open(sys.argv[1], 'r') as f:
    line = f.readline()
    values = list(map(int, line.split(',')))
    optimal = max(enumerate(values), key = lambda x:x[1])[0]
    for line in f:
        values = list(map(float, line.split(',')))
        action, _ = [(i,x) for i, x in enumerate(values) if x != 0][0]
        optimal_taked_times += int(action==optimal)
        optimal_percentage_step.append(optimal_taked_times/step)
        step += 1

def plt_init():
    global plt
    plt.figure().dpi *= 4

plt_init()
plt.ylabel('optimal action percetage')
plt.ylim(0,1)
plt.xlabel('steps')
plt.plot(optimal_percentage_step)
plt.show()
