# 座標圧縮

def zaatu(a_li):
    a_se=sorted(set(a_li))
    a_dic={v: i for i,v in enumerate(a_se)}
    ans_a=list(map(lambda v: a_dic[v],a_li))
    return ans_a