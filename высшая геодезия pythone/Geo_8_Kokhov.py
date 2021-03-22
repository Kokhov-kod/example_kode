import math
from math import fabs
a=6378137.0
e=0.006739496742 
ААС= (237.58*math.pi)/180
S = (46624.432*math.pi)/180
A = (62.212624*math.pi)/180
B = (50.3389772*math.pi)/180
C = (67.4498161*math.pi)/180
Bm = (55*math.pi)/180
HA = 2650.3 
НВ = 2341.4 
HC = 1600.3 
η1=18
ζ1=-24.7
η2=24.4
ζ2=-13.5
η3=-1
ζ3=-14.4
H1=2650.3
H2=2341.4
H3=1600.3
B2=(56.628861*math.pi)/180
A12=(45.3*math.pi)/180
z11=(90.316*math.pi)/180
A13=(107.55*math.pi)/180
z12=(90.76*math.pi)/180

k1 = ((206265*(e)) / (2*a))

A21=(175*math.pi)/180
z21=(90.35*math.pi)/180
A23=(225.3*math.pi)/180
z22=(89.6*math.pi)/180

A32=(287.55*math.pi)/180
z31=(89.23*math.pi)/180
A31=(355*math.pi)/180
z32=(89.7*math.pi)/180
v11 = (( η1 *math.cos (A12) - ζ1 *math.sin (A12))*1/math.tan(z11))
v12 = ((η1 *math.cos (A13) - ζ1 *math.sin (A13)) *1/math.tan(z12))
v21 = (( η1 *math.cos (A21) - ζ1 *math.sin (A21))*1/math.tan(z21))
v22 = (( η1 *math.cos (A23) - ζ1 *math.sin (A23)) *1/math.tan(z22))
v31 = (( η1 *math.cos (A32) - ζ1 *math.sin (A32)) *1/math.tan(z31))
v32 = (( η1 *math.cos (A31) - ζ1 *math.sin (A31)) *1/math.tan(z32))
print("")
print("РЕДУЦИРОВАНИЕ ТРЕУГОЛЬНИКА С ПОВЕРХНОСТИ ЗЕМЛИ НА ПОВЕРХНОСТЬ ЭЛЛИПСОИДА")
print("")
print("1. Редуцирование измеренных горизонтальных углов")
print("")
print ("Поправка AB v1 = %.3f" %v11,"″")
print ("Поправка AC v1 = %.3f" %v12,"″")
print ("Поправка BC v1 = %.3f" %v21,"″")
print ("Поправка BA v1 = %.3f" %v22,"″")
print ("Поправка CA v1 = %.3f" %v31,"″")
print ("Поправка CB v1 = %.3f" %v32,"″")
#k1=0.0001902
V11 = k1*H2* math.cos(B2)**2 *2*math.sin(A12)*math.cos(A12)
V12 = k1*H3* math.cos(B2)**2 *2*math.sin(A13)*math.cos(A13)

V21 = k1*H3* math.cos(B2)**2 *2*math.sin(A23)*math.cos(A23)
V22 = k1*H1* math.cos(B2)**2 *2*math.sin(A21)*math.cos(A21)

V31 = k1*H1* math.cos(B2)**2 *2*math.sin(A31)*math.cos(A31)
V32 = k1*H2* math.cos(B2)**2 *2*math.sin(A32)*math.cos(A32)

wab=v11+V11
wac=v12+V12
wba=v22+V22
wbc=v21+V21
wcb=v32+V32
wca=v31+V31

da=wac-wab
db=wba-wbc
dc=wcb-wca
print ()
print ("Поправка AB v2 = %.3f" %V11,"″")
print ("Поправка AC v2 = %.3f" %V12,"″")
print ("Поправка BC v2 = %.3f" %V21,"″")
print ("Поправка BA v2 = %.3f" %V22,"″")
print ("Поправка CA v2 = %.3f" %V31,"″")
print ("Поправка CB v2 = %.3f" %V32,"″")
print ()
print ("∆A = %f" %da,"″")
print ("∆B = %f" %db,"″")
print ("∆C = %f" %dc,"″")
print ()
sum1=A+B+C
sum2=A+B+C+((da+db+dc)/3600)
sum3=((da+db+dc)/3600)
print ("Сумма измеренных углов = %f" %(sum1*180/math.pi),"°")
print ("Сумма сферических углов = %f" %(sum2*180/math.pi),"°")
print ("Сумма поправок = %f" %(sum3*180/math.pi),"°")
print()
print("2. Редукция измеренного наклонного расстояния S = АС, элипсоид WGS-84")
print()
print ("1)вычисление хорды d:")
dH = fabs(HC - HA)
print ("∆H = %f" %dH,"м")
Hm = (HC + HA) /2
print ("Hm = %f" %Hm,"м")
Rm = a*(1 - 0.5 *e *(-1)*(math.sin(Bm)**2))
print ("Rm = %f" %Rm,"м")
print()
print("2)Вычисление длины стороны сфероидического треугольника АС:")
d = math.sqrt ((S)**2 --(dH)**2 *(1-Hm/ Rm))
print ("d = %f" %d,"м")

S0 = d+(d)**3/(24*(Rm)**2)
print ("S0 = %f" %S0,"м")
print()
print("3)Поправка ∆S")
dS = S0 - S
print ("∆S = %f" %dS,"м")