class RL():
    DEBUG = True

    def __init__(self, s_dim, a_dim, Q):
        """ Set dimensions of states and actions, coded in numbers. It's needed a persistant policy tool too """
        self.s_dim = s_dim
        self.a_dim = a_dim
        self.Q = Q

    def get_best_action(self, s):
        best_a = 0
        best_a_value = None
        if self.DEBUG:
            self._debug_list = []
        for i, a_value in enumerate(range(self.a_dim)):
            a_value = self.get_action_value(s,i)
            if self.DEBUG:
                self._debug_list.append(a_value)
            if best_a_value is None or best_a_value < a_value:
                best_a = i
                best_a_value = a_value
        if self.DEBUG:
            print('############################')
            print('# State: {state}'.format(state=s))
            for i, a_value in enumerate(self._debug_list):
                if i == best_a:
                    print('#   {move}: {value} <'.format(move=i, value=a_value))
                else:
                    print('#   {move}: {value}'.format(move=i, value=a_value))
            print('# Best: {move}'.format(move=best_a))
            print('############################')
        return best_a

    def get_action_value(self, s, a):
        return self.Q.get(s, a)

    def get_actions(self, s):
        return list(range(self.a_dim))

    def get_actions_values(self, s):
        return sorted(self.Q.get_items(s))

    def get_max_value(self, s):
        return max([self.get_action_value(s,i) for i in range(self.a_dim)])
        
    def set(self, s, a, v):
        self.Q.set(s, a, v)

    def update(self, s, a, r):
        v_0, n_0 = self.Q.get(s,a)
        n = n_0 + 1
        v = v_0 + (r - v_0)/n
        if self.DEBUG:
            print('#RRRRRRRRRRRRRRRRRRRRRRRRRRR')
            print('# Value_0:',v_0)
            print('# N_0:    ',n_0)
            print('# Reward: ',r)
            print('# Value:  ',v)
            print('# N:      ',n)
            print('#RRRRRRRRRRRRRRRRRRRRRRRRRRR')
        return self.Q.set(s,a,v)

