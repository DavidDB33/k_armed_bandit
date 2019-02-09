import scipy
from scipy.stats import norm
from collections import namedtuple

MEAN = 0
STD = 3

Info = namedtuple('Info', ['mean'])

class Penv():
    def __init__(self, num_arms = 1, prob_arms = None):
        self.num_arms = num_arms
        self.prob_arms = self._init_calc_probs(num_arms, prob_arms)

    def _init_calc_probs(self, num_arms, prob_arms):
        """Execute only at init
        Initialize arms means"""
        if prob_arms is None:
            prob_arms = norm.rvs(loc=MEAN, scale=STD, size=num_arms)
        else:
            prob_arms = [1.0]*num_arms
        return prob_arms

    def info(self):
        """ Get info about env """
        return [Info(mean=x) for x in self.prob_arms]
        
    def step(self, action):
        """ Get next step of the environment """
        return norm.rvs(loc=self.prob_arms[action], scale=0.2, size=1)[0]

    def reset(self, num_arms = 1, prob_arms = None):
        self.__init__(num_arms = num_arms, prob_arms = prob_arms)

    def render(self):
        return None
