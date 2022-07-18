import numpy as np 
import pandas as pd
from scipy.io import loadmat, savemat


def loadData(filename):
    mat = loadmat(filename)
    data = mat['ForecastTime']

    return data

def exportData(data, filename):
    # savemat(filename, data)
    np.savetxt(filename, data, fmt='%d')
