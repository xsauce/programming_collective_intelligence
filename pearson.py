def pearson(v1, v2):
    '''
    判断两组数据与某一个直线拟合程度的量度，在数据不是很规范时，有用。
    '''
    si = {}
    for i in v1:
        if i in v2:
            si[i] = 1
    n = len(si)
    if n == 0:
        return 1
    sum1 = sum([v1[i] for i in v1])
    sum2 = sum([v2[i] for i in v2])
    sum1Sq = sum([pow(v1[i], 2) for i in v1])
    sum2Sq = sum([pow(v2[i], 2) for i in v2])
    pSum = sum(v1[i] * v2[i] for i in v1])
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    return num / den
