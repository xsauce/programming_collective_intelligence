# -*- coding:utf-8 -*-
def tanimoto(v1, v2):
    '''
    求交集和并集的比率, Tanimoto coefficient
    '''
    c1, c2, shr = 0, 0, 0
    for i in range(len(v1)):
        if v1[i] != 0:
            c1 += 1 ＃ 出现在v1中
        if v2[i] != 0:
            c2 += 1 ＃ 出现在v2中
        if v1[i] != 0 and v2[i] != 0:
            shr += 1 ＃ 在v1和v2中都出现
    return 1.0 - (float(shr)) / (c1 + c2 - shr)
