from utils.io import loadData, exportData
from algos.LIHP import LIHP
from algos.FIHP import FIHP
from algos.RW import RW
from algos.interv import interv
from algos.modif import modifInterv
from utils.gaph import *

from copy import copy
import numpy as np

# for i in range(5, 151):
#     data = loadData("./data/massbig"+str(i)+".mat")
#     res = RW(data)
#     exportData(res, './res/RW/massbig'+str(i)+".txt")
#     res = LIHP(data)
#     exportData(res, './res/LIHP/massbig'+str(i)+".txt")
#     res = FIHP(data)
#     exportData(res, './res/FIHP/massbig'+str(i)+".txt")

#     print("file №"+str(i)+" done")

example = np.array([[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                     [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
                     [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

data = loadData("./data/massbig1.mat")
newdata = copy(data)
res = modifInterv(example)
print(res)

# exportData(res, "./res/interv/massbig1.txt")

hist(res)
# compareGraph(newdata, res)
