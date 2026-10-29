class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.weight = [0] * (n+1) # 根への距離

    # xを含む根付き木の根番号を返す
    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.root(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y
        
    # xの、根からの重みを返す
    def get_weight(self, x):
        self.root(x)
        return -self.weight[x]

    # Py=Px+wとなるようにxとyを併合
    def unite(self, x, y, w):
        rx = self.root(x)
        ry = self.root(y)
        # xの木の高さ < yの木の高さ
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        # xの木の高さ ≧ yの木の高さ
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            # 木の高さが同じだった場合の処理
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    # xとyが同じグループに属すか判定
    def isSame(self, x, y):
        return self.root(x) == self.root(y)

    # Py-Px (xからyへのコスト) を返す
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]