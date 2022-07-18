from turtle import color
from matplotlib import markers
import numpy as np
import matplotlib.pyplot as plt

N = 64


def graph(data):
    plt.rcParams.update({'font.size': 4})

    x = np.arange(0, len(data[0]))
    fig, ax = plt.subplots()

    for i in range(len(data)):
        y = data[i] * (i+1)
        ax.scatter(x, y, s=0.5)

    ax.scatter(x, np.zeros(len(data[0])), c='w', s=1)

    ax.grid(True)

    plt.yticks(np.arange(1, len(data)+1, 1))
    plt.xticks(np.arange(1, len(data[0])+1, 3600))

    plt.show()


def graphResult(data):
    plt.rcParams.update({'font.size': 4})

    fig, ax = plt.subplots()

    ax.scatter(np.arange(0, len(data)), data, s=2, marker='.')

    ax.scatter(np.arange(0, len(data)), np.zeros(len(data)), c='w', s=5)

    ax.grid(True)

    plt.yticks(np.arange(1, max(data)+1, 1))
    plt.xticks(np.arange(1, len(data), 3600))

    plt.show()

def compareGraph(data, res):
    plt.rcParams.update({'font.size': 4})

    fig, axs = plt.subplots(2)
    axs[0].grid(True)
    axs[1].grid(True)

    x1 = np.arange(0, len(data[0]))

    for i in range(len(data)):
        y = data[i] * (i+1)
        axs[0].scatter(x1, y, s=0.1, marker='.')

    axs[0].scatter(x1, np.zeros(len(data[0])), c='w', s=0.1)
    
    axs[1].scatter(x1, res, s=0.5, marker='.')
    axs[1].scatter(x1, np.zeros(len(res)), c='w', s=0.1)
    
    # plt.yticks(np.arange(1, len(data)+1, 1))
    # plt.xticks(np.arange(1, len(data[0])+1, 3600))

    axs[0].grid(True)
    axs[1].grid(True)

    plt.show()

def hist(data):
    plt.rcParams.update({'font.size': 5})
    plt.hist(data, bins=np.arange(1, N, 1))
    plt.grid(True)
    # plt.xticks(np.arange(0, N+1, 10))
    plt.show()
