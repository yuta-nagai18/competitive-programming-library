#時計周りに90度回転 (転置してから反転)
import numpy as np
def rotate(t):
    t=np.array(t).T.tolist()
    for i in range(len(t)):
        t[i]=list(t[i])
        t[i].reverse()
    return t

#転置だけ
import numpy as np
def transpose(t):
    t=np.array(t).T.tolist()
    return t

#(a,b)を反時計回りにd度回転 d<0のとき時計回り
from math import sin,cos,radians
def rotate_degree(a,b,d):
    d=radians(d)
    return (a*cos(d)-b*sin(d),a*sin(d)+b*cos(d))

