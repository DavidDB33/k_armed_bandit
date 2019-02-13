import random
import scipy
from scipy.stats import norm
from collections import namedtuple

INIT_MEAN = 0
INIT_STD = 3

Info = namedtuple('Info', ['mean'])

class MetaEnvironment():
    def __init__(self, num_states, num_actions):
        self.num_states = num_states
        self.num_actions = num_actions

    def load(self, nfile):
        pass

    def save(self, nfile):
        pass

    def step(self, action):
        """ Get next step of the environment
        Input: 
            action: the action taked
        Return: 
            next state: the state, in this case always 0
            reward: the reward of the action taked in this state
            is_done: when the environment arrive to a final state this value returns true. In this case, is always false
        """
        next_state = None
        reward = None
        is_done = True
        return next_state, reward, is_done

    def render(self):
        """ Comunication with the screen.
        Print in a box the state to be human readable
        Input: no input
        Return: no return
        """
        pass

    def sample(self):
        return random.randint(0,self.num_actions-1)

    def __del__(self):
        pass

    def reset(self):
        pass

class KArmedBandit(MetaEnvironment):
    std = 0.2
    def __init__(self, num_arms = 1, prob_arms = None, action_taked_filename = None):
        self.num_arms = num_arms
        self.prob_arms = self._init_calc_probs(num_arms, prob_arms)
        if action_taked_filename is not None:
            self.action_taked_logger = open(action_taked_filename, 'w')
            optimal = self._get_optimal_arm()
            self.action_taked_logger.write(','.join('1' if x == optimal else '0' for x in range(num_arms))+'\n')
        else:
            self.action_taked_logger = None

    def _init_calc_probs(self, num_arms, prob_arms):
        """Execute only at init
        Initialize arms means"""
        if prob_arms is None:
            prob_arms = norm.rvs(loc=INIT_MEAN, scale=INIT_STD, size=num_arms)
        return prob_arms

    def _get_optimal_arm(self):
        return max(enumerate(self.prob_arms),key = lambda x:x[1])[0]

    def info(self):
        """ Get info about env """
        return [Info(mean=x) for x in self.prob_arms]
        
    def step(self, action):
        """ Get next step of the environment
        Input: 
            action: the action taked
        Return: 
            next state: the state, in this case always 0
            reward: the reward of the action taked in this state
            is_done: when the environment arrive to a final state this value returns true. In this case, is always false
        """
        reward = norm.rvs(loc=self.prob_arms[action], scale=self.std, size=1)[0]
        if reward == 0:
            reward = 1e-18 # enough to no modify the reward but different of 0 to note that this action is taked in the logger
        next_state = 0
        is_done = False
        if self.action_taked_logger is not None:
            self.action_taked_logger.write(','.join(str(reward) if action == x else '0' for x in range(self.num_arms))+'\n')
        return next_state, reward, is_done

    def reset(self, num_arms = 1, prob_arms = None):
        self.action_taked_logger.close()
        self.__init__(num_arms = num_arms, prob_arms = prob_arms)

    def sample(self):
        return random.randint(0,self.num_arms-1)

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write('\n'.join(map(str,self.prob_arms)))

    def __del__(self):
        if self.action_taked_logger is not None:
            self.action_taked_logger.close()
