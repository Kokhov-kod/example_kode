import math

print ("Определить плоские прямоугольные координаты этой точки в системе координат смежной с запада зоны с L = 21°.")
print ()
print ("Геодезические координаты заданной точки и значения ℓ выписываются из работы №6: B = 56° 37' 43.9000”. L = 30° 15' 13.1360")
print ()
print ("")
l0=21
B=56.628861
L=30.253648
lp=l0-L
C=ll=L-l0
B=(56.628861*math.pi)/180
L=(30.253648*math.pi)/180
l=(ll*math.pi)/180
a=6378245
b=6356863.0188
e=math.sqrt (0.0066934216)

a0 = 32140.404-(135.3302-(0.7092-0.004*math.cos(B)**2) *math.cos(B)**2)*math.cos(B)**2
a4 = (0.25 + 0.00252 *math.cos(B)**2) *math.cos(B)**2-0.04166
a6 = (0.166 * math.cos(B)**2-0.084 ) *math.cos(B)**2
a3 = (0.3333333 + 0.00123 *math.cos(B)**2) *math.cos(B)**2 - 0.1666667
a5 = 0.0083 - ( 0.1667 - (0.1968 + 0.004* math.cos(B)**2)* math.cos(B)**2) *math.cos(B)**2
N = a / math.sqrt( 1 - e**2*math.sin(B)**2)
x = 6367558.4969 * B -(a0 - (0.5 + (a4+a6*l**2)*l**2)*l**2*N)*math.sin(B)*math.cos(B)
y = ( 1 + (a3  + a5 *l**2) *l**2)*l* N*math.cos(B)

print ("B рад = %.9f" %B)
print ("l рад = %.9f" %l)
print ("Sin B = %.9f" %(math.sin(B)))
print ("Cos B = %.9f" %(math.cos(B)))
print ("Cos^2 B = %.9f" %(math.cos(B)**2))
print ("Sin B*Cos B = %.9f" %(math.sin(B)*math.cos(B)) )
print ("l^2n= %.9f" %l**2)
print ("N = %.3f" %N)
print ("N*l^2 = %.3f" %(N*(l**2)))
print ("a0 = %.4f" %a0)
print ("a4 = %.8f" %a4)
print ("a6 = %.8f" %a6)
print ("a3 = %.8f" %a3)
print ("a5 = %.8f" %a5)
print ("6367558.4969*B = %.9f" %(6367558.4969 * B))
print ("x (м) = %.3f" %x)
print ("1+(a3+a5*l^2)*l^2 = %.9f" %( 1 + (a3  + a5 *l**2) *l**2))
print ("l*N*cos B = %.9f" %(l* N*math.cos(B)))
print ("y (м) = %.3f" %y)

βe = x / 6367558.4969
β=(βe*math.pi)/180
Bx= β+(50221746+(293622 +(2350 + 22*math.cos(β)**2)*math.cos(β)**2)* math.cos(β)**2)*math.sin(β)*math.cos(β)*10**(-10)
     
b2 = (0.5 + 0.003369 *math.cos(Bx)**2 )*math.sin(Bx)* math.cos(Bx)
b3 = 0.333333 - (0.166667 - 0.001123 *math.cos(Bx)**2)* math.cos(Bx)**2
b4 = 0.25 + (0.16161 + 0.00562* math.cos(Bx)**2) *math.cos(Bx)**2
b5 = 0.2 - (0.1667 - 0.0088* math.cos(Bx)**2) * math.cos(Bx)**2
z = y / N*math.cos(Bx)  
В = Bx - (1-(b4 - 0.12*z**2 )*z**2)*z**2*b**2
l  = (1 - (b3 - b5* z**2)* z**2)*z       
       
print ()
print ("--------------------------------------------------------------------------------------------------------------------------------------------------------")
print ()
print ("βрад = %.9f" %β)
print ("sin β = %.9f" %math.sin(β))
print ("sinβ^2 = %.9f" %math.sin(β)**2)
print ("cosβ^2 = %.9f" %math.cos(β))
print ("sin β*cos β = %.9f" %(math.sin(β)*math.cos(β)))
print ("Вх рад = %.9f" %Bx)
print ("е^2 = 0.0066934216" )
print ("Nx = %.9f" %N)
print ("cosBx^2 = %.9f" %(math.cos(Bx)**2))
print ("cosBx = %.9f" %(math.cos(Bx)))
print ("Nx*cosBx = %.9f" %(N*math.cos(Bx)))
print ("z = %.9f" %z)
print ("z^2 = %.9f" %(z**2))
print ("b2 = %.9f" %b2)
print ("b4 = %.9f" %b4)
print ("b3 = %.9f" %b3)
print ("b5 = %.9f" %b5)
print ("z^2*b2 = %.9f" %(z**2*b2))
print ("B рад = %.9f" %B)
print ("B = 56° 37' 43.9000”")
print ("l рад = %.9f" %l)
print ("l'' = %.9f" %(ll*3600))
print ("l = %.9f" %(ll))
print ("L =  30° 15' 13.1360''")
