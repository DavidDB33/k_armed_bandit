from scipy import stats
from scipy.stats import norm
from collections import namedtuple

MEAN = 0
STD = 3

Info = namedtuple('Info', ['mean'])

class Penv():
    def __init__(self, num_bandits = 1, prob_bandits = None):
        self.num_bandits = num_bandits
        self.prob_bandits = self._init_calc_probs(num_bandits, prob_bandits)

    def _init_calc_probs(self, num_bandits, prob_bandits):
        """Execute only at init
        Initialize bandits means"""
        if prob_bandits is None:
            prob_bandits = norm.rvs(loc=MEAN, scale=STD, size=num_bandits)
        else:
            prob_bandits = [1.0]*num_bandits
        return prob_bandits

    def info(self):
        """ Get info about env """
        return [Info(mean=x) for x in self.prob_bandits]
        
        
    def step(self, action):
        """ Get next step of the environment """
        return norm.rvs(loc=self.prob_bandits[action], scale=0.2, size=1)[0]

