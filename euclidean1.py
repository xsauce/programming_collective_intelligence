def euclidean(v1, v2):
    '''
    欧几里德距离：坐标的平方差
    '''
    sum_squares = sum([pow(v1[i] - v2[i], 2) for i in v1 if i in v2])
    return 1 / (1 + sqrt(sum_squares))
