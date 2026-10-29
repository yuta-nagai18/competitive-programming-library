#多次元リストを複数キーでソートする

data=[["きゅうり",1,4],["いちご",2,6],["にんじん",2,1],["とうふ",1,0]]

sorted_data=sorted(data,key=lambda x:(x[1],x[2]),reverse=True)

print(sorted_data)