from dateutil import utils
from networkx.algorithms import approximation
import networkx as nx
import matplotlib.pyplot as plt
import random


# max_clique
# https://www.sciencedirect.com/science/article/pii/S0022000003001107
# A = approximation ratio is v/log(v)^2 -maximum clique/independent set in the worst case


def create_GNP(n,p):
    G = nx.gnp_random_graph(n,p)
    return G


def activate_max_clique(G):
    return approximation.max_clique(G)


# def plot(n,aproximation_ratio):
#     fig, axes = plt.subplots(2, 3, sharex=True, sharey=True)
#     axes[0,0].plot(n, aproximation_ratio)
#     axes[0,1].plot(n, aproximation_ratio)
#     axes[0, 2].plot(n, aproximation_ratio)
#     axes[1, 0].plot(n, aproximation_ratio)
#     axes[1, 1].plot(n, aproximation_ratio)
#     axes[1, 2].plot(n, aproximation_ratio)
#     plt.show()


def calculate_ratio():
    """
    this function calculate the aproximation ratio of max_clique approximation algorithm
    doing so by compression between the approximate algo and accurate algo
    & plotting the results
    :return: aproximation ratio of max_clique: int
    """
    fig, axes = plt.subplots(2, 3, sharex=True, sharey=True)
    k=0
    for j in range (0,6):
        p = random.random()
        n_list = []
        aprox_ratio_list = []
        for i in range(0,10):

            n=random.randint(1,30)
            g=create_GNP(n,p)
            aprox_len= len(activate_max_clique(g))
            cliques = nx.find_cliques(g)
            accurate_len=len(max(cliques, key=len))
            num=aprox_len-accurate_len
            aproximation_ratio=abs(num)
            aprox_ratio_list.append(aproximation_ratio)
            n_list.append(n)
            print(aproximation_ratio)
        if j<3:
            axes[0, k].plot(n_list, aprox_ratio_list)
            k+=1

        elif j==3 :
            k=0
            axes[1, k].plot(n_list, aprox_ratio_list)
            k += 1
        else:
            axes[1, k].plot(n_list, aprox_ratio_list)
            k += 1
        plt.show()


if __name__ == '__main__':
    calculate_ratio()


