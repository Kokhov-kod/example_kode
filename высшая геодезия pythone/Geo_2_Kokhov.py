import math

print("")
print("ВЫЧИСЛЕНИЕ ДЛИНЫ ДУГИ КООРДИНАТНЫХ ЛИНИЙ ЗЕМНОГО ЭЛИПСОИДА")
print("")
print("---------------------------------------------------------------------------------------------------------------------")
print("ДАНО")
print("КООРДИНАТЫ ПЕРВОЙ ТОЧКИ ДУГИ")
print("")
print("   B1 = 55° 10' 00.000''+30*n'")
print("   L1 = 37° 30' 00.000''")
print("")
print("---------------------------------------------------------------------------------------------------------------------")
print("вариант 12");
B1=198600+1800*12
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
print ("ВЫЧИСЛИТЬ ЗНАЧЕНИЕ ДЛИНЫ ДУГИ МЕРИДИАНА ЭЛЛИПСОИДА КРАСОВСКОГО,  WGS-84, ПЗ- 90 И ВАРИАНТ 12 МЕЖДУ ТОЧКАМИ С РАЗНОСТЬЮ ИХ ШИРОТ  ΔВ =2° (В2 = В1 + 2°) ТРЕМЯ СПОСОБАМИ.")
print ("")
print ("1)")

#красовский
m0=A1*(1-E1)
m2=3/2*E1*m0
m4=5/4*E1*m2
m6=7/6*E1*m4
a0=m0+m2/2+3/8*m4
a2=m2/2+m4/2+15/32*m6
a4=m4/8+3/16*m6
a6=m6/32
x1=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
x2=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
delx=x2-x1
print ("Красовский")
print ("")
print ("m0= %.4f" %m0)
print ("m2= %.4f" %m2)
print ("m4= %.4f" %m4)
print ("m6= %.4f" %m6)
print ("a0= %.4f" %a0)
print ("a2= %.4f" %a2)
print ("a4= %.4f" %a4)
print ("a6= %.4f" %a6)
print ("x1= %.4f" %x1)
print ("x2= %.4f" %x2)
print ("delx= %.4f" %delx)
#wgs 84
m0=A2*(1-E2)
m2=3/2*E2*m0
m4=5/4*E2*m2
m6=7/6*E2*m4
a0=m0+m2/2+3/8*m4
a2=m2/2+m4/2+15/32*m6
a4=m4/8+3/16*m6
a6=m6/32
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
x1=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
x2=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
delx=x2-x1
print ("")
print ("wgs 84")
print ("")
print ("m0= %.4f" %m0)
print ("m2= %.4f" %m2)
print ("m4= %.4f" %m4)
print ("m6= %.4f" %m6)
print ("a0= %.4f" %a0)
print ("a2= %.4f" %a2)
print ("a4= %.4f" %a4)
print ("a6= %.4f" %a6)
print ("x1= %.4f" %x1)
print ("x2= %.4f" %x2)
print ("delx= %.4f" %delx)
#пз 90
m0=A3*(1-E3)
m2=3/2*E3*m0
m4=5/4*E3*m2
m6=7/6*E3*m4
a0=m0+m2/2+3/8*m4
a2=m2/2+m4/2+15/32*m6
a4=m4/8+3/16*m6
a6=m6/32
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
x1=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
x2=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
delx=x2-x1
print ("")
print ("пз 90")
print ("")
print ("m0= %.4f" %m0)
print ("m2= %.4f" %m2)
print ("m4= %.4f" %m4)
print ("m6= %.4f" %m6)
print ("a0= %.4f" %a0)
print ("a2= %.4f" %a2)
print ("a4= %.4f" %a4)
print ("a6= %.4f" %a6)
print ("x1= %.4f" %x1)
print ("x2= %.4f" %x2)
print ("delx= %.4f" %delx)
#вариант 12
m0=A4*(1-E3)
m2=3/2*E4*m0
m4=5/4*E4*m2
m6=7/6*E4*m4
a0=m0+m2/2+3/8*m4
a2=m2/2+m4/2+15/32*m6
a4=m4/8+3/16*m6
a6=m6/32
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
x1=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
x2=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
delx=x2-x1
print ("")
print ("вариант 12")
print ("")
print ("m0= %.4f" %m0)
print ("m2= %.4f" %m2)
print ("m4= %.4f" %m4)
print ("m6= %.4f" %m6)
print ("a0= %.4f" %a0)
print ("a2= %.4f" %a2)
print ("a4= %.4f" %a4)
print ("a6= %.4f" %a6)
print ("x1= %.4f" %x1)
print ("x2= %.4f" %x2)
print ("delx= %.4f" %delx)
print ("")

print ("2)")
B1=0
B=B1/3600+2
Br=B*math.pi/180
delx=Br/6*(M11+4*((M11+M12)/2)+M12)
print ("Красовского")
print ("delx= %.2f" %delx)
delx=Br/6*(M21+4*((M21+M22)/2)+M22)
print ("WGS 84")
print ("delx= %.2f" %delx)
delx=Br/6*(M31+4*((M31+M32)/2)+M32)
print ("ПЗ-90")
print ("delx= %.2f" %delx)
delx=Br/6*(M41+4*((M41+M42)/2)+M42)
print ("Вариант 12")
print ("delx= %.2f" %delx)
B1=0
B=B1/3600+2
Br=B*math.pi/180
print ("")
print ("3)")
delx=(M11+M12)/2*Br
print ("Красовского")
print ("delx= %.2f" %delx)
delx=(M21+M22)/2*Br
print ("WGS 84")
print ("delx= %.2f" %delx)
delx=(M31+M32)/2*Br
print ("ПЗ-90")
print ("delx= %.2f" %delx)
delx=(M41+M42)/2*Br
print ("Вариант 12")
print ("delx= %.2f" %delx)
print ("")
print("---------------------------------------------------------------------------------------------------------------------")

print("ВЫЧИСЛИТЬ ЗНАЧЕНИЕ ДЛИНЫ ДУГИ ПАРАЛЛЕЛИ ДЛЯ РАЗНОСТИ ДОЛГОТ ΔL = 2°  НА ШИРОТАХ ПУНКТОВ  С В1  И В2  ТЕХ ЖЕ ЭЛЛИПСОИДОВ")
L=0/3600+2
Lr=L*math.pi/180
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
dely1=N11*math.cos(Br)*Lr
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
dely2=N11*math.cos(Br)*Lr
print ("Красовского")
print ("dely1= %f" %dely1)
print ("dely2= %f" %dely2)
L=0/3600+2
Lr=L*math.pi/180
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
dely1=N21*math.cos(Br)*Lr
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
dely2=N21*math.cos(Br)*Lr
print ("WGS 84")
print ("dely1= %f" %dely1)
print ("dely2= %f" %dely2)
L=0/3600+2
Lr=L*math.pi/180
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
dely1=N31*math.cos(Br)*Lr
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
dely2=N31*math.cos(Br)*Lr
print ("ПЗ-90")
print ("dely1= %f" %dely1)
print ("dely2= %f" %dely2)
L=0/3600+2
Lr=L*math.pi/180
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
dely1=N41*math.cos(Br)*Lr
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
dely2=N41*math.cos(Br)*Lr
print ("Вариант 12")
print ("dely1= %f" %dely1)
print ("dely2= %f" %dely2)
print ("")
print("---------------------------------------------------------------------------------------------------------------------")
print ("СОСТАВИТЬ ТАБЛИЦУ СРАВНЕНИЯ ЗНАЧЕНИЙ ДЛИНЫ ДУГИ МЕРИДИАНА И ПАРАЛЛЕЛИ: РАЗНОСТИ ШИРОТ И ДОЛГОТ  В 1° -   В  КМ,    В 1י  И 1” -   В МЕТРАХ")
print ("градусы")
m0=A1*(1-E1)
m2=3/2*E1*m0
m4=5/4*E1*m2
m6=7/6*E1*m4
a0=m0+m2/2+3/8*m4
a2=m2/2+m4/2+15/32*m6
a4=m4/8+3/16*m6
a6=m6/32
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
x1=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
x2=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
delx=(x2-x1)/2
print ("")
print ("Красовский")
print ("delx= %.4f" %delx)
#wgs 84
m0=A2*(1-E2)
m2=3/2*E2*m0
m4=5/4*E2*m2
m6=7/6*E2*m4
a0=m0+m2/2+3/8*m4
a2=m2/2+m4/2+15/32*m6
a4=m4/8+3/16*m6
a6=m6/32
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
x1=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
x2=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
delx=(x2-x1)/2
print ("WGS-84")
print ("delx= %.4f" %delx)
#пз 90
m0=A3*(1-E3)
m2=3/2*E3*m0
m4=5/4*E3*m2
m6=7/6*E3*m4
a0=m0+m2/2+3/8*m4
a2=m2/2+m4/2+15/32*m6
a4=m4/8+3/16*m6
a6=m6/32
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
x1=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
x2=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
delx=(x2-x1)/2
print ("ПЗ-90")
print ("m0= %.4f" %m0)
print ("delx= %.4f" %delx)
#вариант 12
m0=A4*(1-E3)
m2=3/2*E4*m0
m4=5/4*E4*m2
m6=7/6*E4*m4
a0=m0+m2/2+3/8*m4
a2=m2/2+m4/2+15/32*m6
a4=m4/8+3/16*m6
a6=m6/32
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
x1=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
x2=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
delx=(x2-x1)/2
print ("Вариант 12")
print ("delx= %.4f" %delx)
print ("")
print ("2)")
B1=0
B=B1/3600+2
Br=B*math.pi/180
delx=(Br/6*(M11+4*((M11+M12)/2)+M12))/2
print ("Красовского")
print ("delx= %.2f" %delx)
delx=(Br/6*(M21+4*((M21+M22)/2)+M22))/2
print ("WGS 84")
print ("delx= %.2f" %delx)
delx=(Br/6*(M31+4*((M31+M32)/2)+M32))/2
print ("ПЗ-90")
print ("delx= %.2f" %delx)
delx=(Br/6*(M41+4*((M41+M42)/2)+M42))/2
print ("Вариант 12")
print ("delx= %.2f" %delx)
B1=0
B=B1/3600+2
Br=B*math.pi/180
print ("")
print ("3)")
delx=((M11+M12)/2*Br)/2
print ("Красовского")
print ("delx= %.2f" %delx)
delx=((M21+M22)/2*Br)/2
print ("WGS 84")
print ("delx= %.2f" %delx)
delx=((M31+M32)/2*Br)/2
print ("ПЗ-90")
print ("delx= %.2f" %delx)
delx=((M41+M42)/2*Br)/2
print ("Вариант 12")
print ("delx= %.2f" %delx)
print ("")
L=0/3600+2
Lr=L*math.pi/180
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
dely1=(N11*math.cos(Br)*Lr)/2
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
dely2=(N11*math.cos(Br)*Lr)/2
print ("Красовского")
print ("dely1= %f" %dely1)
print ("dely2= %f" %dely2)
L=0/3600+2
Lr=L*math.pi/180
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
dely1=(N21*math.cos(Br)*Lr)/2
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
dely2=(N21*math.cos(Br)*Lr)/2
print ("WGS 84")
print ("dely1= %f" %dely1)
print ("dely2= %f" %dely2)
L=0/3600+2
Lr=L*math.pi/180
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
dely1=(N31*math.cos(Br)*Lr)/2
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
dely2=(N31*math.cos(Br)*Lr)/2
print ("ПЗ-90")
print ("dely1= %f" %dely1)
print ("dely2= %f" %dely2)
L=0/3600+2
Lr=L*math.pi/180
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
dely1=(N41*math.cos(Br)*Lr)/2
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
dely2=(N41*math.cos(Br)*Lr)/2
print ("Вариант 12")
print ("dely1= %f" %dely1)
print ("dely2= %f" %dely2)
print ("")
print("---------------------------------------------------------------------------------------------------------------------")
print ("минуты")
m0=A1*(1-E1)
m2=3/2*E1*m0
m4=5/4*E1*m2
m6=7/6*E1*m4
a0=m0+m2/2+3/8*m4
a2=m2/2+m4/2+15/32*m6
a4=m4/8+3/16*m6
a6=m6/32
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
x1=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
x2=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
delx=(x2-x1)/120
print ("")
print ("Красовский")
print ("delx= %.4f" %delx)
#wgs 84
m0=A2*(1-E2)
m2=3/2*E2*m0
m4=5/4*E2*m2
m6=7/6*E2*m4
a0=m0+m2/2+3/8*m4
a2=m2/2+m4/2+15/32*m6
a4=m4/8+3/16*m6
a6=m6/32
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
x1=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
x2=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
delx=(x2-x1)/120
print ("WGS-84")
print ("delx= %.4f" %delx)
#пз 90
m0=A3*(1-E3)
m2=3/2*E3*m0
m4=5/4*E3*m2
m6=7/6*E3*m4
a0=m0+m2/2+3/8*m4
a2=m2/2+m4/2+15/32*m6
a4=m4/8+3/16*m6
a6=m6/32
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
x1=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
x2=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
delx=(x2-x1)/120
print ("ПЗ-90")
print ("m0= %.4f" %m0)
print ("delx= %.4f" %delx)
#вариант 12
m0=A4*(1-E3)
m2=3/2*E4*m0
m4=5/4*E4*m2
m6=7/6*E4*m4
a0=m0+m2/2+3/8*m4
a2=m2/2+m4/2+15/32*m6
a4=m4/8+3/16*m6
a6=m6/32
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
x1=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
x2=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
delx=(x2-x1)/120
print ("Вариант 12")
print ("delx= %.4f" %delx)
print ("")
print ("2)")
B1=0
B=B1/3600+2
Br=B*math.pi/180
delx=(Br/6*(M11+4*((M11+M12)/2)+M12))/120
print ("Красовского")
print ("delx= %.2f" %delx)
delx=(Br/6*(M21+4*((M21+M22)/2)+M22))/120
print ("WGS 84")
print ("delx= %.2f" %delx)
delx=(Br/6*(M31+4*((M31+M32)/2)+M32))/120
print ("ПЗ-90")
print ("delx= %.2f" %delx)
delx=(Br/6*(M41+4*((M41+M42)/2)+M42))/120
print ("Вариант 12")
print ("delx= %.2f" %delx)
B1=0
B=B1/3600+2
Br=B*math.pi/180
print ("")
print ("3)")
delx=((M11+M12)/2*Br)/120
print ("Красовского")
print ("delx= %.2f" %delx)
delx=((M21+M22)/2*Br)/120
print ("WGS 84")
print ("delx= %.2f" %delx)
delx=((M31+M32)/2*Br)/120
print ("ПЗ-90")
print ("delx= %.2f" %delx)
delx=((M41+M42)/2*Br)/120
print ("Вариант 12")
print ("delx= %.2f" %delx)
print ("")
L=0/3600+2
Lr=L*math.pi/180
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
dely1=(N11*math.cos(Br)*Lr)/120
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
dely2=(N11*math.cos(Br)*Lr)/120
print ("Красовского")
print ("dely1= %f" %dely1)
print ("dely2= %f" %dely2)
L=0/3600+2
Lr=L*math.pi/180
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
dely1=(N21*math.cos(Br)*Lr)/120
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
dely2=(N21*math.cos(Br)*Lr)/120
print ("WGS 84")
print ("dely1= %f" %dely1)
print ("dely2= %f" %dely2)
L=0/3600+2
Lr=L*math.pi/180
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
dely1=(N31*math.cos(Br)*Lr)/120
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
dely2=(N31*math.cos(Br)*Lr)/120
print ("ПЗ-90")
print ("dely1= %f" %dely1)
print ("dely2= %f" %dely2)
L=0/3600+2
Lr=L*math.pi/180
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
dely1=(N41*math.cos(Br)*Lr)/120
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
dely2=(N41*math.cos(Br)*Lr)/120
print ("Вариант 12")
print ("dely1= %f" %dely1)
print ("dely2= %f" %dely2)
print ("")
print("---------------------------------------------------------------------------------------------------------------------")
print ("секунды")
m2=3/2*E1*m0
m4=5/4*E1*m2
m6=7/6*E1*m4
a0=m0+m2/2+3/8*m4
a2=m2/2+m4/2+15/32*m6
a4=m4/8+3/16*m6
a6=m6/32
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
x1=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
x2=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
delx=(x2-x1)/240
print ("")
print ("Красовский")
print ("delx= %.4f" %delx)
#wgs 84
m0=A2*(1-E2)
m2=3/2*E2*m0
m4=5/4*E2*m2
m6=7/6*E2*m4
a0=m0+m2/2+3/8*m4
a2=m2/2+m4/2+15/32*m6
a4=m4/8+3/16*m6
a6=m6/32
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
x1=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
x2=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
delx=(x2-x1)/240
print ("WGS-84")
print ("delx= %.4f" %delx)
#пз 90
m0=A3*(1-E3)
m2=3/2*E3*m0
m4=5/4*E3*m2
m6=7/6*E3*m4
a0=m0+m2/2+3/8*m4
a2=m2/2+m4/2+15/32*m6
a4=m4/8+3/16*m6
a6=m6/32
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
x1=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
x2=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
delx=(x2-x1)/240
print ("ПЗ-90")
print ("m0= %.4f" %m0)
print ("delx= %.4f" %delx)
#вариант 12
m0=A4*(1-E3)
m2=3/2*E4*m0
m4=5/4*E4*m2
m6=7/6*E4*m4
a0=m0+m2/2+3/8*m4
a2=m2/2+m4/2+15/32*m6
a4=m4/8+3/16*m6
a6=m6/32
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
x1=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
x2=a0*Br-a2/2*math.sin(2*Br)+a4/4*math.sin(4*Br)-a6/6*math.sin(6*Br)
delx=(x2-x1)/240
print ("Вариант 12")
print ("delx= %.4f" %delx)
print ("")
print ("2)")
B1=0
B=B1/3600+2
Br=B*math.pi/180
delx=(Br/6*(M11+4*((M11+M12)/2)+M12))/240
print ("Красовского")
print ("delx= %.2f" %delx)
delx=(Br/6*(M21+4*((M21+M22)/2)+M22))/240
print ("WGS 84")
print ("delx= %.2f" %delx)
delx=(Br/6*(M31+4*((M31+M32)/2)+M32))/240
print ("ПЗ-90")
print ("delx= %.2f" %delx)
delx=(Br/6*(M41+4*((M41+M42)/2)+M42))/240
print ("Вариант 12")
print ("delx= %.2f" %delx)
B1=0
B=B1/3600+2
Br=B*math.pi/180
print ("")
print ("3)")
delx=((M11+M12)/2*Br)/240
print ("Красовского")
print ("delx= %.2f" %delx)
delx=((M21+M22)/2*Br)/240
print ("WGS 84")
print ("delx= %.2f" %delx)
delx=((M31+M32)/2*Br)/240
print ("ПЗ-90")
print ("delx= %.2f" %delx)
delx=((M41+M42)/2*Br)/240
print ("Вариант 12")
print ("delx= %.2f" %delx)
print ("")
L=0/3600+2
Lr=L*math.pi/180
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
dely1=(N11*math.cos(Br)*Lr)/240
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
dely2=(N11*math.cos(Br)*Lr)/240
print ("Красовского")
print ("dely1= %f" %dely1)
print ("dely2= %f" %dely2)
L=0/3600+2
Lr=L*math.pi/180
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
dely1=(N21*math.cos(Br)*Lr)/240
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
dely2=(N21*math.cos(Br)*Lr)/240
print ("WGS 84")
print ("dely1= %f" %dely1)
print ("dely2= %f" %dely2)
L=0/3600+2
Lr=L*math.pi/180
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
dely1=(N31*math.cos(Br)*Lr)/240
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
dely2=(N31*math.cos(Br)*Lr)/240
print ("ПЗ-90")
print ("dely1= %f" %dely1)
print ("dely2= %f" %dely2)
L=0/3600+2
Lr=L*math.pi/180
B1=198600+1800*12
B=B1/3600
Br=B*math.pi/180
dely1=(N41*math.cos(Br)*Lr)/240
B1=198600+1800*12
B=B1/3600+2
Br=B*math.pi/180
dely2=(N41*math.cos(Br)*Lr)/240
print ("Вариант 12")
print ("dely1= %f" %dely1)
print ("dely2= %f" %dely2)
print ("")
print("---------------------------------------------------------------------------------------------------------------------")