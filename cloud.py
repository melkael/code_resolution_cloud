from itertools import tee
from functools import reduce

mu = 5
lambd = 50
seuils = [10, 20, 30]   # le dernier seuil est la capacité du buffer

S_i = [0] * len(seuils) # len(seuils donne le nombre de serveurs)
mu *= 12/len(seuils) 

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def ro(i):
    return lambd/(i*mu)

def set_termes():
    termes = [ro(1) ** (seuils[0] - 1)]
    for i in range(2, len(seuils)):
        termes.append(ro(i) ** (seuils[i - 1] - seuils[i - 2] + 1)) 
    return termes

# termes = liste des premiers termes du produit des ro_i ** (Fk - Fk-1 -1) (le dernier terme etant celui à la puissance i - Fk-1 + 1)
termes = set_termes()
for i in range(0, seuils[0]):
    S_i[0] += ro(1) ** i
index = 1
for Fk_prec, Fk in pairwise(seuils):
    for i in range(Fk_prec, Fk):
        S_i[index] +=  reduce((lambda x, y: x * y), termes[:index]) *\
                       ro(index + 1) ** (i - seuils[index - 1] + 1)
    index += 1

pi_zero = 1 / (1 + sum(S_i))
print(pi_zero)