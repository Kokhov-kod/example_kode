
import math

p= 206265
eks1= 0.0066943662
c= 6399592
PI=math.pi
B1=(50.1278*PI)/180
L1=(24.7538*PI)/180
A1=(6.5*PI)/180
S=281260.18
bk=6356751.5
class Ellipsoid:
    
    def Run_Kut_In():
     p= 206265
     eks1= 0.0066943662
     c= 6399592
     PI=math.pi
     B1=(50.1278*PI)/180
     L1=(24.7538*PI)/180
     A1=(6.5*PI)/180
     S=281260.18
     S0=(S/c)*p
     betta=1.25*eks1
     math.cos2B1=math.cos(B1)*math.cos(B1)
     gam1=betta*math.cos2B1
     V1=(1+0.6*gam1)/(1+0.2*gam1)
     V13=V1*V1*V1
     DelB1=S0*V13*math.cos(A1)
     DelB1rad=(DelB1/3600)*PI/180
     DelL1=(S0*V1*(math.sin(A1)/math.cos(B1)))/2
     DelL1rad=(DelL1/3600)*PI/180
     DelA1=(DelL1*math.sin(B1))
     DelA1rad=(DelA1/3600)*PI/180
     B2=(B1+(0.5)*DelB1rad)
     A2=(A1+(0.5)*DelA1rad)
     math.cos2B2=math.cos(B2)*math.cos(B2)
     gam2=betta*math.cos2B2
     V2=(1+0.6*gam2)/(1+0.2*gam2)
     V23=V2*V2*V2
     DelB2=(S0*V23*math.cos(A2))
     DelB2rad=(DelB2/3600)*PI/180
     DelL2=(S0*V2*(math.sin(A2)/math.cos(B2)))/2
     DelL2rad=(DelL2/3600)*PI/180
     DelA2=(DelL2*math.sin(B2))
     DelA2rad=(DelA2/3600)*PI/180
     B3=(B1+(0.25)*(DelB1rad+DelB2rad))
     A3=(A1+(0.25)*(DelA1rad+DelA2rad))
     math.cos2B3=math.cos(B3)*math.cos(B3)
     gam3=betta*math.cos2B3
     V3=(1+0.6*gam3)/(1+0.2*gam3)
     V33=V3*V3*V3
     DelB3=(S0*V33*math.cos(A3))
     DelB3rad=(DelB3/3600)*PI/180
     DelL3=(S0*V3*(math.sin(A3)/math.cos(B3)))/2
     DelL3rad=(DelL3/3600)*PI/180
     DelA3=(DelL3*math.sin(B3))
     DelA3rad=(DelA3/3600)*PI/180
     B4=(B1-DelB2rad+2*DelB3rad)
     A4=(A1-DelA2rad+2*DelA3rad)
     math.cos2B4=math.cos(B4)*math.cos(B4)
     gam4=betta*math.cos2B4
     V4=(1+0.6*gam4)/(1+0.2*gam4)
     V43=V4*V4*V4
     DelB4=(S0*V43*math.cos(A4))
     DelB4rad=(DelB4/3600)*PI/180
     DelL4=(S0*V4*(math.sin(A4)/math.cos(B4)))/2
     DelL4rad=(DelL4/3600)*PI/180
     DelA4=(DelL4*math.sin(B4))
     DelA4rad=(DelA4/3600)*PI/180
     DelB=0.17*(DelB1rad+4*DelB3rad+DelB4rad)
     DelL=0.17*(DelL1rad+4*DelL3rad+DelL4rad)
     DelA=0.17*(DelA1rad+4*DelA3rad+DelA4rad)
     QB2=(B1*180/PI)+(DelB*180/PI)
     QL2=(L1*180/PI)+(DelL*180/PI)
     QA2=(A1*180/PI)+(DelA*180/PI)
     print("                          ЗНАЧЕНИЯ ПАРАМЕТРОВ A1-A4:  %.6f, %.6f, %.6f, %.6f" %((A1*180/PI),(A2*180/PI),(A3*180/PI),(A4*180/PI)))
     print("                          ЗНАЧЕНИЯ ПАРАМЕТРОВ B1-B4:  %.6f, %.6f, %.6f, %.6f" %((B1*180/PI),(B2*180/PI),(B3*180/PI),(B4*180/PI)))
     print("                          ЗНАЧЕНИЯ ПАРАМЕТРОВ V1-V4:  %.6f, %.6f, %.6f, %.6f" %(V1,V2,V3,V4))
     print("                      ЗНАЧЕНИЯ ПАРАМЕТРОВ V1^3-V4^3:  %.6f, %.6f, %.6f, %.6f" %(V13,V23,V33,V43))
     print("                    ЗНАЧЕНИЯ ПАРАМЕТРОВ ∆B1''-∆B4'':  %.6f, %.6f, %.6f, %.6f" %(DelB1,DelB2,DelB3,DelB4))
     print("                    ЗНАЧЕНИЯ ПАРАМЕТРОВ ∆L1''-∆L4'':  %.6f, %.6f, %.6f, %.6f" %(DelL1,DelL2,DelL3,DelL4))
     print("                    ЗНАЧЕНИЯ ПАРАМЕТРОВ ∆A1''-∆A4'':  %.6f, %.6f, %.6f, %.6f" %(DelA1,DelA2,DelA3,DelA4))
     print("                              ЗНАЧЕНИЯ ПАРАМЕТРА ∆В:  %.6f" %((DelB*180/PI)))
     print("                              ЗНАЧЕНИЯ ПАРАМЕТРА ∆L:  %.6f" %(DelL))
     print("                              ЗНАЧЕНИЯ ПАРАМЕТРА ∆A:  %.6f" %((DelA*180/PI)))
     print("              ШИРОТА ТОЧКИ Q2 В ДЕСЯТИЧНЫХ ГРАДУСАХ:  %.6f " %QB2)
     print("             ДОЛГОТА ТОЧКИ Q2 В ДЕСЯТИЧНЫХ ГРАДУСАХ:  %.6f " %QL2)
     print("ЗНАЧЕНИЕ АЗИМУТА А21 ТОЧКИ Q2 В ДЕСЯТИЧНЫХ ГРАДУСАХ:  %.6f " %QA2)
     #print("%.6f" %math.math.cos(A1))
     #print("%.6f" %math.math.cos(A2))   
    def Bessel():
         
         B1=(50.1278*PI)/180
         L1=(24.7538*PI)/180
         A1=(6.5*PI)/180
         S=281260.18
         tanU1=math.sqrt(1-eks1)*math.tan(B1)
         tan2U1=tanU1*tanU1
         sinU1=(tanU1/math.sqrt(1+tan2U1))
         cosU1=(1/math.sqrt(1+tan2U1))
         sinA0=cosU1*math.sin(A1)
         A0=(math.asin(sinA0))
         A0rad=A0*PI/180
         cos2A0=math.cos(A0rad)*math.cos(A0rad)
         cos4A0=cos2A0*cos2A0
         ctgsig1=math.cos(A1)/tanU1
         ctg2sig1=ctgsig1*ctgsig1
         sin2sig1=(2*ctgsig1)/(ctg2sig1+1)
         cos2sig1=(ctg2sig1-1)/(ctg2sig1+1)
         k2=eks1*cos2A0
         k4=k2*k2
         k6=k2*k2*k2
         eks12=eks1*eks1
         eks13=eks1*eks1*eks1
         A=bk*(1+(k2/4)-((3*k4)/64)+((5*k6)/256))
         B=bk*(k2/8-(k4/32)+((15*k6)/1024))

         
         C=bk*(k4/128-((3*k6)/512))
         alfa=(((eks1/2)+(eks12/8)+(eks13/16))-((eks12+eks13)/16)*cos2A0+3*eks13*cos4A0/128)*p
         alfarad=(alfa/3600)*PI/180
         betta=(((eks12/32)+eks13/32)*cos2A0-eks13*cos4A0/64)*p
         bettarad=(betta/3600)*PI/180
         sig0=(((S-(B+C*cos2sig1)*sin2sig1))/A)
         sig0rad=sig0*PI/180
         sin2sig1sig0=sin2sig1*math.cos(2*sig0rad)+cos2sig1*math.sin(2*sig0rad)
         cos2sig1sig0=cos2sig1*math.cos(2*sig0rad)-sin2sig1*math.sin(2*sig0rad)
         sig=sig0rad+(B+5*C*cos2sig1sig0)*(sin2sig1sig0/A)
         sigrad=sig*PI/180
         Delta=((alfarad*sigrad)+bettarad*(sin2sig1sig0-sin2sig1))*sinA0
         sinU2=sinU1*math.cos(sigrad)+cosU1*math.cos(A1)*math.sin(sigrad)
         U2=math.asin(sinU2)


         eks2=eks1
         tanlyamb=(math.sin(A1)*math.sin(sigrad))/(cosU1*math.cos(sigrad)-sinU1*math.sin(sigrad)*math.cos(A1))
         lyamb=math.atan(tanlyamb)
         tanA2=(cosU1*math.sin(A1))/(cosU1*math.cos(sigrad)*math.cos(A1)-sinU1*math.sin(sigrad))
         A2=math.atan(tanA2)
         tanB2=(1/math.sqrt(1-eks2))*math.tan(U2)
         B2=math.atan(tanB2)
         L2=L1+lyamb-Delta
         A21=A2+180
         print("        ЗНАЧЕНИЕ ПАРАМЕТРА ТАНГЕНС U1:  %.6f" %tanU1)
         print("      ЗНАЧЕНИЕ ПАРАМЕТРА ТАНГЕНС^2 U1:  %.6f" %tan2U1)
         print("            ЗНАЧЕНИЕ ПАРАМЕТРА sin U1:  %.6f" %sinU1)
         print("            ЗНАЧЕНИЕ ПАРАМЕТРА cos U1:  %.6f" %cosU1)
         print("            ЗНАЧЕНИЕ ПАРАМЕТРА sin a0:  %.6f" %sinA0)
         print("                ЗНАЧЕНИЕ ПАРАМЕТРА a0:  %.6f" %A0)
         print("             ЗНАЧЕНИЕ ПАРАМЕТРА a0rad:  %.6f" %A0rad)
         print("      ЗНАЧЕНИЕ ПАРАМЕТРА math.cos^2a0:  %.6f" %cos2A0)
         print("      ЗНАЧЕНИЕ ПАРАМЕТРА math.cos^4a0:  %.6f" %cos4A0)
         print("      ЗНАЧЕНИЕ ПАРАМЕТРА math.ctgsig1:  %.6f" %ctgsig1)
         print("     ЗНАЧЕНИЕ ПАРАМЕТРА math.ctg2sig1:  %.6f" %ctg2sig1)
         print("     ЗНАЧЕНИЕ ПАРАМЕТРА math.sin2sig1:  %.6f" %sin2sig1)
         print("     ЗНАЧЕНИЕ ПАРАМЕТРА math.cos2sig1:  %.6f" %cos2sig1)
         print("                ЗНАЧЕНИЕ ПАРАМЕТРА k2:  %.6f" %k2)
         print("                ЗНАЧЕНИЕ ПАРАМЕТРА k4:  %.6f" %k4)
         print("                ЗНАЧЕНИЕ ПАРАМЕТРА k6:  %.6f" %k6)
         print("                 ЗНАЧЕНИЕ ПАРАМЕТРА A:  %.6f" %A)
         print("                 ЗНАЧЕНИЕ ПАРАМЕТРА B:  %.6f" %B)
         print("                 ЗНАЧЕНИЕ ПАРАМЕТРА C:  %.6f" %C)
         print("              ЗНАЧЕНИЕ ПАРАМЕТРА alfa:  %.6f" %alfa)
         print("           ЗНАЧЕНИЕ ПАРАМЕТРА alfarad:  %.6f" %alfarad)
         print("             ЗНАЧЕНИЕ ПАРАМЕТРА betta:  %.6f" %betta)
         print("          ЗНАЧЕНИЕ ПАРАМЕТРА bettarad:  %.6f" %bettarad)
         print("              ЗНАЧЕНИЕ ПАРАМЕТРА sig0:  %.6f" %sig0)
         print("           ЗНАЧЕНИЕ ПАРАМЕТРА sig0rad:  %.6f" %sig0rad)
         print(" ЗНАЧЕНИЕ ПАРАМЕТРА math.sin2sig1sig0:  %.6f" %sin2sig1sig0)
         print(" ЗНАЧЕНИЕ ПАРАМЕТРА math.cos2sig1sig0:  %.6f" %cos2sig1sig0)
         print("               ЗНАЧЕНИЕ ПАРАМЕТРА sig:  %.6f" %sig)
         print("            ЗНАЧЕНИЕ ПАРАМЕТРА sigrad:  %.6f" %sigrad)
         print("             ЗНАЧЕНИЕ ПАРАМЕТРА Delta:  %.6f" %Delta)
         print("        ЗНАЧЕНИЕ ПАРАМЕТРА math.sinU2:  %.6f" %sinU2)
         print("                ЗНАЧЕНИЕ ПАРАМЕТРА U2:  %.6f" %U2)
         print("                ЗНАЧЕНИЕ ПАРАМЕТРА B2:  %.6f" %B2)
         print("          ЗНАЧЕНИЕ ПАРАМЕТРА tanlyamb:  %.6f" %tanlyamb)
         print("  ЗНАЧЕНИЕ ПАРАМЕТРА lyamb в секундых:  %.6f" %(lyamb*180/PI*120000))
         print("                ЗНАЧЕНИЕ ПАРАМЕТРА L2:  %.6f" %L2)
         print("             ЗНАЧЕНИЕ ПАРАМЕТРА tanA2:  %.6f" %tanA2)
         print("                ЗНАЧЕНИЕ ПАРАМЕТРА A2:  %.6f" %(A2*180/PI))
         print("               ЗНАЧЕНИЕ ПАРАМЕТРА A21:  %.6f" %A21)        
    def Srednie():
         B1=(50.1278*PI)/180
         L1=(24.7538*PI)/180
         A1=(6.5*PI)/180
         B2=(52.639614*PI)/180
         L2=(24.990330*PI)/180
         A2=(6.5*PI)/180
         S=281260.18
         DeltaB=B2-B1
         DeltaB2=DeltaB*DeltaB
         l=L2-L1
         l2=l*l
         Bm=(B2+B1)/2
         sin2Bm=math.sin(Bm)*math.sin(Bm)
         cos2Bm=math.cos(Bm)*math.cos(Bm)
         Vm=math.sqrt(1+eks1*cos2Bm)
         Vm3=Vm*Vm*Vm
         Nm=c/Vm
         Mm=c/Vm3
         kont=Nm/Mm
         Vm2=Vm*Vm
         Q=DeltaB*Mm*(1-(l2*(2*sin2Bm))/24)
         P=l*Nm*math.cos(Bm)*(1+(DeltaB2-(l*math.sin(Bm)*(l*math.sin(Bm))))/24)
         DeltaA=l*math.sin(Bm)*(1+((3*DeltaB2)+2*l2-2*(l*math.sin(Bm)*(l*math.sin(Bm))))/24)*206265
         tanAm=P/Q
         Am=math.atan(tanAm)
         A12=(Am+(DeltaA/7200)*180/PI)
         A21=((Am+DeltaA/7200)*180/PI)+180
         Sq=math.sqrt(Q*Q+P*P)
         print("ЗНАЧЕНИЕ ПАРАМЕТРА B2rad = %.6f" %B2)
         print("ЗНАЧЕНИЕ ПАРАМЕТРА B1rad = %.6f" %B1)
         print("ЗНАЧЕНИЕ ПАРАМЕТРА DeltaBrad = %.6f" %DeltaB)
         print("ЗНАЧЕНИЕ ПАРАМЕТРА lrad = %.6f" %l)
         print("ЗНАЧЕНИЕ ПАРАМЕТРА Bmrad = %.6f" %Bm)
         print("ЗНАЧЕНИЕ ПАРАМЕТРА sinBm = %.6f" %math.sin(Bm))
         print("ЗНАЧЕНИЕ ПАРАМЕТРА cosBm = %.6f" %math.cos(Bm))
         print("ЗНАЧЕНИЕ ПАРАМЕТРА eks1cos2bm = %.6f" %(eks1*cos2Bm))
         print("ЗНАЧЕНИЕ ПАРАМЕТРА Vm = %.6f" %Vm)
         print("ЗНАЧЕНИЕ ПАРАМЕТРА Nm = %.6f" %Nm)
         print("ЗНАЧЕНИЕ ПАРАМЕТРА Mm = %.6f" %Mm)
         print("ЗНАЧЕНИЕ ПАРАМЕТРА Q = %.6f" %Q)
         print("ЗНАЧЕНИЕ ПАРАМЕТРА P = %.6f" %P)
         print("ЗНАЧЕНИЕ ПАРАМЕТРА tgAm = %.6f" %tanAm)
         print("ЗНАЧЕНИЕ ПАРАМЕТРА Am = %.6f" %(math.atan(tanAm)*180/PI))
         print("ЗНАЧЕНИЕ ПАРАМЕТРА lsinBm = %.6f" %(l*math.sin(Bm)))
         print("ЗНАЧЕНИЕ ПАРАМЕТРА DeltaA = %.6f" %DeltaA)
         print("ЗНАЧЕНИЕ ПАРАМЕТРА A12 = %.6f" %A12)
         print("ЗНАЧЕНИЕ ПАРАМЕТРА A21 = %.6f" %A21)
         print("ЗНАЧЕНИЕ ПАРАМЕТРА Sq = %.6f" %Sq)

print("РАБОТА №5")
print()
print("Решение прямой геодезической задачи способом Рунге – Кутта - Ингланда на эллипсоиде Красовскогоprint()")
print()
print("----------------------------------------------------------------------------------------------------------------")
print()
Ellipsoid.Run_Kut_In()
print("----------------------------------------------------------------------------------------------------------------")
print()
print("Решение прямой геодезической задачи способом Бесселя (1-й алгоритм)")
print()
print("----------------------------------------------------------------------------------------------------------------")
print()
Ellipsoid.Bessel()
print("----------------------------------------------------------------------------------------------------------------")
print()
print("Решение обратной геодезической задачи по формулам со средними аргументами")
print()
print("----------------------------------------------------------------------------------------------------------------")
print()
Ellipsoid.Srednie()