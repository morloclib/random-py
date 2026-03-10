import random as _random

def morloc_setSeed(seed):
    _random.seed(seed)
    return None

def morloc_random_real():
    return _random.random()

def morloc_random_int():
    return _random.randint(0, 2147483647)

def morloc_random_bool():
    return _random.random() < 0.5

def morloc_randomRange_real(lo, hi):
    return _random.uniform(lo, hi)

def morloc_randomRange_int(lo, hi):
    return _random.randint(lo, hi)

def morloc_bernoulli(p):
    return _random.random() < p

def morloc_choice(xs):
    return _random.choice(xs)

def morloc_weightedChoice(pairs):
    weights = [w for (w, _) in pairs]
    values = [v for (_, v) in pairs]
    return _random.choices(values, weights=weights, k=1)[0]

def morloc_sample(n, xs):
    return _random.sample(xs, n)

def morloc_sampleWith(n, xs):
    return _random.choices(xs, k=n)

def morloc_permute(xs):
    result = list(xs)
    _random.shuffle(result)
    return result
