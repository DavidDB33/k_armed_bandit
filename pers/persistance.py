import redis
from struct import Struct

class Persistance():
    DEBUG = True
    DEFAULT = 0.0
    FORMAT = 'di'

    def __init__(self, db=0):
        self.r = redis.Redis(host='localhost', port=6379, db=db)
        self.f = Struct(self.FORMAT)

    def __getitem__(self, e):
        return self.f.unpack(self.r[e])

    def __setitem__(self, k, v):
        self.r[k] = self.f.pack(*v)

    def set(self, s, a, v):
        v_0, n_0 = self.get(s, a)
        n = n_0 + 1
        self[a] = v, n
        if self.DEBUG:
            print('#P N:({n_0} -> {n}) Update action {action}: {val1} <- {val2}'.format(n_0=n_0, n=n, action=a, val1=v_0, val2=v))
    
    def get(self, s, a, default = None):
        try:
            val, n = self[a]
        except KeyError as e:
            val = default if default is not None else self.DEFAULT
            n = 0
            self[a] = val, n
        return val, n

    def get_items(self, s):
        tok, key_list = None, []
        while tok is None or tok != 0:
            for k in key_list:
                v = self[k]
                yield int(k), v
            if tok is None:
                tok, key_list = self.r.scan()
            else:
                tok, key_list = self.r.scan(tok)

    def flush(self):
        self.r.flushdb()
