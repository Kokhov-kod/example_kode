import math
B1=201600
B=B1/3600
Br=B*math.pi/180
A1=6378245#красовский
A2=6378137#wgs84
A3=6378136#пз90
A4=6378511.67#вариант
E1=0.0066934216#красовский
E2=0.0066945419#wgs84
E3=0.0066943662#пз90
E4=0.0063529984#вариант
M11=6384683.5949
M21=6384576.5611
M31=6384575.3915
M41=6374127.2023
M12=6386540.9678
M22=6386434.2154
M32=6386432.9965
M42=6376201.0493
N11=6394689.8800
N21=6394584.3644
N31=6394582.9286
N41=6390611.7883
N12=6395309.9145
N22=6395204.4930
N32=6395203.0407
N42=6391304.7833
b1=6356863.0188
b2=6356751.7963
b3=6356751.3617
b4=6358218.05
e1=0.0066934216
e2=0.0066945419
e3=0.0066943662
e4=0.0063529984
print("Дано: Масштаб трапеции 1: 50 000, значение широты точки А рамки а1 трапеции условно принять равным В1 = 50° +10'n, где n - номер студента по журналу. Широта точки В2 рамки а2 определяется в соответствии с номенклатурой трапеции.")
print("")
print("1) ВЫЧИСЛИТЬ ЗНАЧЕНИЕ РАМОК a1, a2, c И ДИАГОНАЛИ d ТЕХ ЖЕ ЭЛЛИПСОИДОВ")
print("")
print("1.1) ВЫЧИСЛИТЬ ЗНАЧЕНИЕ РАМОК a1, a2")
print("")
L=0/3600+0.25
Lr=L*math.pi/180

B1=201600
B=B1/3600
Br=B*math.pi/180
dely1=N11*math.cos(Br)*Lr
B1=202200
B=B1/3600
Br=B*math.pi/180
dely2=N12*math.cos(Br)*Lr
print ("Красовского")
print ("a1 = %f" %(dely1/500))
print ("a2 = %f" %(dely2/500))
L=0/3600+0.25
Lr=L*math.pi/180

B1=201600
B=B1/3600
Br=B*math.pi/180
dely1=N21*math.cos(Br)*Lr

B1=202200
B=B1/3600
Br=B*math.pi/180
dely2=N22*math.cos(Br)*Lr
print ("WGS 84")
print ("a1 = %f" %(dely1/500))
print ("a2 = %f" %(dely2/500))
L=0/3600+0.25
Lr=L*math.pi/180

B1=201600
B=B1/3600
Br=B*math.pi/180
dely1=N31*math.cos(Br)*Lr

B1=202200
B=B1/3600
Br=B*math.pi/180
dely2=N32*math.cos(Br)*Lr
print ("ПЗ-90")
print ("a1 = %f" %(dely1/500))
print ("a2 = %f" %(dely2/500))
L=0/3600+0.25
Lr=L*math.pi/180

B1=201600
B=B1/3600
Br=B*math.pi/180
dely1=N41*math.cos(Br)*Lr

B1=202200
B=B1/3600
Br=B*math.pi/180
dely2=N42*math.cos(Br)*Lr
print ("Вариант 12")
print ("a1 = %f" %(dely1/500))
print ("a2 = %f" %(dely2/500))
print ("")
print("1.2) ВЫЧИСЛИТЬ ЗНАЧЕНИЕ ДЛИНЫ РАМКИ c")
print("")
B1=0
B=B1/3600+0.17
Br=B*math.pi/180
delx=Br/6*(M11+4*((M11+M12)/2)+M12)
print ("Красовского")
print ("c = %.2f" %(delx/500))
delx=Br/6*(M21+4*((M21+M22)/2)+M22)
print ("WGS 84")
print ("c = %.2f" %(delx/500))
delx=Br/6*(M31+4*((M31+M32)/2)+M32)
print ("ПЗ-90")
print ("c = %.2f" %(delx/500))
delx=Br/6*(M41+4*((M41+M42)/2)+M42)
print ("Вариант 12")
print ("c = %.2f" %(delx/500))
print("")
print("1.3) ВЫЧИСЛИТЬ ЗНАЧЕНИЕ ДИАГОНАЛИ d ")
print("")
d=math.sqrt(dely1/500*dely2/500+delx/500*delx/500)
print ("Красовского")
print ("d = %.2f" %d)
d=math.sqrt(dely1/500*dely2/500+delx/500*delx/500)
print ("WGS 84")
print ("d = %.2f" %d)
d=math.sqrt(dely1/500*dely2/500+delx/500*delx/500)
print ("ПЗ-90")
print ("d = %.2f" %d)
d=math.sqrt(dely1/500*dely2/500+delx/500*delx/500)
print ("Вариант 12")
print ("d = %.2f" %d)
print("")
print("2) ПЛОЩАДЬ СЪЕМОЧНОЙ ТРАПЕЦИИ С ПОГРЕШНОСТЬЮ ДО 0,01 КМ")
print("")
L=0/3600+0.25
Lr=L*math.pi/180
B1=201600
B=B1/3600
Br1=B*math.pi/180

B1=202200
B=B1/3600
Br2=B*math.pi/180

I=2/3*e1*(math.sin(Br2)**3-math.sin(Br1)**3)
#print ("I = %.12f" %I)
II=3/5*e1*e1*(math.sin(Br2)**5-math.sin(Br1)**5)
#print ("II = %.12f" %II)
III=4/7*e1*e1*e1*(math.sin(Br2)**7-math.sin(Br1)**7)
#print ("III = %.12f" %III)
P=b1**2*Lr*(math.sin(Br2)-math.sin(Br1)+I+II+III)

print ("Красовского")
print ("P, км^2 = %.2f" %P)
I=2/3*e2*(math.sin(Br2)**3-math.sin(Br1)**3)
#print ("I = %.12f" %I)
II=3/5*e2*e2*(math.sin(Br2)**5-math.sin(Br1)**5)
#print ("II = %.12f" %II)
III=4/7*e2*e2*e2*(math.sin(Br2)**7-math.sin(Br1)**7)
#print ("III = %.12f" %III)
P=b2**2*Lr*(math.sin(Br2)-math.sin(Br1)+I+II+III)
print ("WGS 84")
print ("P, км^2 = %.2f" %P)
I=2/3*e3*(math.sin(Br2)**3-math.sin(Br1)**3)
#print ("I = %.12f" %I)
II=3/5*e3*e3*(math.sin(Br2)**5-math.sin(Br1)**5)
#print ("II = %.12f" %II)
III=4/7*e3*e3*e3*(math.sin(Br2)**7-math.sin(Br1)**7)
#print ("III = %.12f" %III)
P=b3**2*Lr*(math.sin(Br2)-math.sin(Br1)+I+II+III)
print ("ПЗ-90")
print ("P, км^2 = %.2f" %P)
I=2/3*e4*(math.sin(Br2)**3-math.sin(Br1)**3)
#print ("I = %.12f" %I)
II=3/5*e4*e4*(math.sin(Br2)**5-math.sin(Br1)**5)
#print ("II = %.12f" %II)
III=4/7*e4*e4*e4*(math.sin(Br2)**7-math.sin(Br1)**7)
#print ("III = %.12f" %III)
P=b4**2*Lr*(math.sin(Br2)-math.sin(Br1)+I+II+III)
print ("Вариант 12")
print ("P, км^2 = %.2f" %P)