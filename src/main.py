from yaml import safe_dump
from utils.io import loadData, exportData
from algos.LIHP import LIHP
from algos.FIHP import FIHP
from algos.RW import RW
from algos.interv import interv
from algos.modif import modifInterv
from utils.gaph import *

from copy import copy
import numpy as np
import time

N = 11
compare = {"RW":0, "LIHP":0, "FIHP":0, "interv":0, "modif":0}

for i in range(1, N):
    data = loadData("./data/massbig"+str(i)+".mat")

    start_time = time.time()
    res = RW(data)
    end_time = time.time()

    exportData(res, './res/RW/massbig'+str(i)+".txt")

    compare["RW"] += end_time - start_time

    start_time = time.time()
    res = LIHP(data)
    end_time = time.time()

    exportData(res, './res/LIHP/massbig'+str(i)+".txt")

    compare["LIHP"] += end_time - start_time

    start_time = time.time()
    res = FIHP(data)
    end_time = time.time()

    exportData(res, './res/FIHP/massbig'+str(i)+".txt")

    compare["FIHP"] += end_time - start_time

    start_time = time.time()
    res = interv(data)
    end_time = time.time()

    exportData(res, './res/interv/massbig'+str(i)+".txt")

    compare["interv"] += end_time - start_time

    start_time = time.time()
    res = modifInterv(data)
    end_time = time.time()

    exportData(res, './res/modif/massbig'+str(i)+".txt")

    compare["modif"] += end_time - start_time

    print("file №"+str(i)+" done")

for k in compare.keys():
    compare[k] /= N-1

print(compare)

# example = np.array([[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
#                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
#                      [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
#                      [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# data = loadData("./data/massbig1.mat")
# newdata = copy(data)
# res = RW(data)
# print(res)

# exportData(res, "./res/interv/massbig1.txt")

# hist(res)
# compareGraph(newdata, res)
