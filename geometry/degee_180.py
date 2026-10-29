# A=(ax,ay), B=(bx,by), C=(cx,cy)について角ABC(この順で反時計回り)
# (180度未満)  C     A  (180度以上)       B
#                 B                   C     A

def ex_product(ax,ay,bx,by,cx,cy):
    BAx,BAy=ax-bx,ay-by
    BCx,BCy=cx-bx,cy-by
    if BAx*BCy-BAy*BCx>=0:
        # 180度未満
        return True
    else:
        # 180度以上
        return False   

# 外積の定義：
# 3 次元空間内の2つのベクトル a,b の外積 a×bとは、
# a,b の両方に垂直で、右ねじの向き(図参照)を持ち、
# a,b のなす平行四辺形の面積に等しい大きさを持つベクトルである。