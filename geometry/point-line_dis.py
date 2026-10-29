#点と直線の距離
#点(x0,y0)と、直線(点(x1,y1)、点(x2,y2)を通る)の距離
x0,y0,x1,y1,x2,y2=map(int,input().split())
a=y2-y1
b=x1-x2
c=(x2-x1)*y1+(y1-y2)*x1
distance=abs(a*x0+b*y0+c)/(a**2+b**2)**(1/2)

