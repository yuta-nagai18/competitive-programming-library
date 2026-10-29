import copy
#深いコピー
def deepcopy(A):
    return copy.deepcopy(A)

#浅いコピー
def thincopy(A):
    return copy.copy(A)

def thincopy2(A):
    return A.copy()
