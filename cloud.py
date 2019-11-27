from itertools import tee
from functools import reduce
import sys



mu = 20
lambd = 50
# toujours laisser 1 en premier seuil (F0 = 1 car on active le premier serveur quand un client entre)
seuils = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]   # le dernier seuil est la capacité du buffer
# K = len(seuils) - 1 = nombre de VM

S_i = [0] * len(seuils) # len(seuils donne le nombre de serveurs)
#mu *= 12/len(seuils) 

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def ro(i):
    return lambd/(i*mu)


def set_Rho():
    Rho = [1, ro(1) ** (seuils[1] - 1)]
    for i in range(2, len(seuils) - 1):
        Rho.append(Rho[-1] * (ro(i) ** (seuils[i] - seuils[i-1])))
    exposant = seuils[-1] - seuils[-2] + 1
    S = ro(len(seuils) - 1) ** exposant
    S *= Rho[-1]
    Rho.append(S)
    return Rho


Rho = set_Rho()

print(Rho)
# termes = liste des premiers termes du produit des ro_i ** (Fk - Fk-1 -1) (le dernier terme etant celui à la puissance i - Fk-1 + 1)
#termes = set_termes()
#print("Termes multiplicatifs:", termes)

def set_Sommes():
    Sommes = []
    for s_prec in range(len(Rho) - 1):
        S = 0
        for i in range(1, seuils[s_prec + 1] - seuils[s_prec] + 1):
            S += Rho[s_prec] * (ro(s_prec+1) ** i)
        Sommes.append(S)
    Sommes[-1] += Rho[-1]
    return Sommes 

Sommes = set_Sommes()
pi_zero = 1 / (1 + sum(Sommes))
print(pi_zero)

P = [pi_zero]
if(len(seuils) == 4):
    for i in range(seuils[1] - 1):
        P.append(P[-1] * ro(1))
    for i in range(seuils[2] - seuils[1]):
        P.append(P[-1] * ro(2))
    for i in range(seuils[3] - seuils[2] + 1):
        P.append(P[-1] * ro(3))

if(len(seuils) == 7):
    for i in range(seuils[1] - 1):
        P.append(P[-1] * ro(1))
    for i in range(seuils[2] - seuils[1]):
        P.append(P[-1] * ro(2))
    for i in range(seuils[3] - seuils[2]):
        P.append(P[-1] * ro(3))
    for i in range(seuils[4] - seuils[3]):
        P.append(P[-1] * ro(4))
    for i in range(seuils[5] - seuils[4]):
        P.append(P[-1] * ro(5))
    for i in range(seuils[6] - seuils[5] + 1):
        P.append(P[-1] * ro(6))

if(len(seuils) == 13):
    for i in range(seuils[1] - 1):
        P.append(P[-1] * ro(1))
    for i in range(seuils[2] - seuils[1]):
        P.append(P[-1] * ro(2))
    for i in range(seuils[3] - seuils[2]):
        P.append(P[-1] * ro(3))
    for i in range(seuils[4] - seuils[3]):
        P.append(P[-1] * ro(4))
    for i in range(seuils[5] - seuils[4]):
        P.append(P[-1] * ro(5))
    for i in range(seuils[6] - seuils[5]):
        P.append(P[-1] * ro(6))
    for i in range(seuils[7] - seuils[6]):
        P.append(P[-1] * ro(7))
    for i in range(seuils[8] - seuils[7]):
        P.append(P[-1] * ro(8))
    for i in range(seuils[9] - seuils[8]):
        P.append(P[-1] * ro(9))
    for i in range(seuils[10] - seuils[9]):
        P.append(P[-1] * ro(10))
    for i in range(seuils[11] - seuils[10]):
        P.append(P[-1] * ro(11))
    for i in range(seuils[12] - seuils[11] + 1):
        P.append(P[-1] * ro(12))

print(sum(P))