# 2点を決めたときの残りの正方形の2点の座標

# A=(ax,ay), B=(bx,by), C=(cx,cy), D=(dx,dy) の正方形ABCD
#       A                  A        B
#              B   or     
#    D                     
#           C              D        C
# 右の図は下でのay=byのとき
# 点Aと点Bが決まっているとき点Cと点Dの座標を知りたい


def squares_pos(ax,ay,bx,by):
    if not (ax<bx and ay>=by):
        return [False,False,False,False]
    else:
        x=bx-ax
        y=ay-by
        cx=bx-y
        cy=by-x
        dx=ax-y
        dy=ay-x
        return [cx,cy,dx,dy]

# ABC275-C

