# RW (random walk, случайные блуждания). 
# 
# В данном алгоритме при возникновении коллизии выбор спутника, за которым будет 
# вестись наблюдение, осуществляется по марковскому правилу принятия решений. 
# В случае возникновения коллизии среди спутников одного приоритета, 
# спутник выбирается случайно с вероятностью , где  – количество спутников участвующих в коллизии. 
# 
# Дополнительно можно вводить веса, учитывающие приоритетность наблюдения КА, в том числе , 
# по интегральным значениям времени наблюдения каждого аппарата.
import numpy as np
from random import choice


def findVisibles(data, j):
    visible = []

    for i in range(len(data)):
        if data[i][j] == 1:
            visible.append(i+1)

    return visible

def RW(data):
    res = np.zeros(len(data[0]), dtype=np.int64)

    for j in range(len(data[0])):
        vis = findVisibles(data, j)
        if len(vis) == 0:
            res[j] = 0
        else:
            res[j] = choice(findVisibles(data, j))

    return res