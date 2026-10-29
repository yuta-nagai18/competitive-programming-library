class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.weight_x = [0] * (n+1) # 根への距離（x方向）
        self.weight_y = [0] * (n+1) # 根への距離 (y方向)

    # xを含む根付き木の根番号を返す
    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.root(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight_x[x] += self.weight_x[self.par[x]]
            self.weight_y[x] += self.weight_y[self.par[x]]
            self.par[x] = y
            return y
    
    # xの、根からの重みを返す
    def get_weight(self, x):
        self.root(x)
        return -self.weight_x[x],-self.weight_y[x]

    # Py_x=Px_x+wx, Py_y=Px_y+wyとなるようにxとyを併合
    def unite(self, x, y, wx, wy):
        rx = self.root(x)
        ry = self.root(y)
        # xの木の高さ < yの木の高さ
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight_x[rx] = wx - self.weight_x[x] + self.weight_x[y]
            self.weight_y[rx] = wy - self.weight_y[x] + self.weight_y[y]
        # xの木の高さ ≧ yの木の高さ
        else:
            self.par[ry] = rx
            self.weight_x[ry] = -wx - self.weight_x[y] + self.weight_x[x]
            self.weight_y[ry] = -wy - self.weight_y[y] + self.weight_y[x]
            # 木の高さが同じだった場合の処理
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    # xとyが同じグループに属すか判定
    def isSame(self, x, y):
        return self.root(x) == self.root(y)

    # Py_x-Px_x, py_y-Px_y (xからyへのx方向のコスト,y方向のコスト) を返す
    def diff(self, x, y):
        return self.weight_x[x] - self.weight_x[y],self.weight_y[x] - self.weight_y[y]
