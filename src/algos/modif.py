# Алгоритм принятия решения с учетом всего интервала планирования

# Преимущества данного алгоритма заключаются в том, 
# что обеспечивается выравнивание времени наблюдения каждого КА и 
# при этом достигается максимально возможное общее время наблюдения.

import numpy as np
from copy import copy


N = 4
PRIORNUM = 3

def findVisibles(data, j):
    visible = []

    for i in range(len(data)):
        if data[i][j] == 1:
            visible.append(i+1)

    return visible

def noCollisions(data):
    res = np.zeros(len(data[0]), dtype=np.int64)

    for j in range(len(data[0])):
        v = findVisibles(data, j)
        if len(v) == 1:
            res[j] = v[0]

    return res

def tMeanEachPrior(tPot, prior):
    s = 0
    k = 0
    for i in range(len(tPot)):
        if tPot[i][2] == prior:
            s += tPot[i][0]
            k += 1
    if k == 0:
        return 0

    return s / k

def tMean(tPot):
    tM = []
    for i in range(PRIORNUM):
        tM.append(tMeanEachPrior(tPot, i+1))

    return tM
    
def AddInterv(data, i, res):
    for j in range(len(res)):
        if data[i][j] == 1:
            res[j] = i+1
            for k in range(len(data)):
                data[k][j] = 0
            data[i][j] = 1

    return res, data


def potentialTime(data):
    tPot = np.sum(data, axis=1)
    res = np.array([tPot, np.arange(1, len(tPot)+1), np.random.randint(low=1, high=4, size=len((tPot)))])

    res = np.transpose(res)
    sort(res)

    return res

def sort(data):
    for i in range(1, len(data)):
        key = copy(data[i])
        j = i-1
        while j >= 0 and key[0] < data[j][0]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key

def modifInterv(data):
    # 1) Добавление в план наблюдения интервалов времени в которых отсутствует коллизия
    res = noCollisions(data)
    newData = copy(data)

    # 3) Спутники сортируются по возрастанию потенциальной длительности наблюдения
    tPot = potentialTime(newData)
    print(tPot)
    # 2) Расчёт среднего времени наблюдения спутника
    tM = tMean(tPot)
    print(tM)

    # 4) Производится сравнение потенциального времени наблюдения каждого КА 
    #       со средним временем наблюдения. Если потенциальное время наблюдения спутника 
    #       меньше или равно среднему, то все интервалы видимости соответствующего спутника 
    #       добавляются в план наблюдения и алгоритм переходит к шагу 6. 
    #       Если потенциальное время наблюдения спутника больше среднего времени наблюдения спутника, 
    #       то алгоритм переходит к шагу 5;
    for p in range(PRIORNUM, 0, -1):
        for i in range(N):
            if tPot[i][0] <= tM[p-1] and tPot[i][2] == p:
                res, newData = AddInterv(newData, int(tPot[i][1]-1), res)
                # print(newData)
                tPot = potentialTime(newData)
                # print(i, tPot)
            else:
                # 5) Перерасчет среднего (при необходимости)
                # print(i, tPot[i][0], tM)
                tPot = potentialTime(newData)
                tM = tMean(newData)
                res, newData = AddInterv(newData, int(tPot[i][1]-1), res)
                # print(tPot)

    
    # 6) Переход к следующему спутнику, шаг 3 алгоритма.

    return res
