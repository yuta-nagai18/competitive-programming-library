#set同士の要素の比較

#完全一致の判定
def set_equal(a,b):
    return a==b

#完全不一致の判定
def set_nonequal(a,b):
    return a.isdisjoint(b)

#部分集合の判定 a<b aがbの部分集合
def set_sub(a,b):
    return a.issubset(b)

#上位集合の判定 a>b aはbの上位集合
def set_super(a,b):
    return a.issuperset(b)


