import random

class abm:
    class Walkerrandom:
        # Walker's alias method for random selection based on discrete probability.
        def __init__(self, weights, keys=None):
            n = self.n = len(weights)
            self.keys = keys
            sumw = sum(weights)
            prob = [ w*n / sumw for w in weights]
            inx = [-1]*n
            short = [j for j, p in enumerate(prob) if p < 1]
            long = [j for j, p in enumerate(prob) if p > 1]
            while short and long:
                j = short.pop()
                k = long[-1]
                inx[j] = k

        def __str__(self):
            probstr = "".join(["%.2g" % x for x in self.prob])
            inxstr = "".join(["%.2g" % x for x in self.inx])
            return "Walkerrandom prob: %s inx: %s" % (probstr, inxstr)

        def random(self):
            u = random.uniform(0,1)
            j = random.randint(0, self.n-1)
            randint = j if u <= self.prob[j] else self.inx[j]
            return self.keys[randint] if self.keys else randint

    class Agent:
        def __init__(self, nslots):
            self.nslots = nslots
            self.slots = []
            self.membership = set()

    class Organization:
        def __init__(self, specific, nslots, demand, rewiring):
            self.specific = specific
            self.nslots = nslots
            self.all_members = []
            self.demand = demand
            self.rewiring = rewiring

    def __init__(self, sys_vars, org_vars, env_vars):
        self.h = sys_vars[0]
        self.N = sys_vars[1]
        self.k = sys_vars[2]
        self.repetition = sys_vars[3]
        self.rh = sys_vars[4]
        self.ri = sys_vars[5]
        self.mode = sys_vars[6]
        self.rt = sys_vars[7]
        self.s = sys_vars[8]
        self.budget = 100

        self.nslots = org_vars[0]
        self.rewiring = org_vars[1]
        self.demand = org_vars[2]

        self.env_norgs = env_vars[0]
        self.env_condition = env_vars[1]

        self.org_specifics = range(1+self.env_norgs)
        self.sim_mat = dict()
        self.org_dict = {}
        self.signature = str(self.repetition)+'_'+str(self.rewiring)+'_'+str(self.demand)+'_'\
                         +str(self.env_condition)+'_'+str(self.s)
        self.sig = str(self.repetition) + '\t' + str(self.rewiring) + '\t' + str(self.demand) +\
                   '\t' + str(self.env_condition)
        self.net_collect = {}

    def assign_env_strgy(self):
        demands = range(1,16)
        rewirings = [0.0]