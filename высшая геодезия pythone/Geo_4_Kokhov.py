import math
print ("ЛАБОРАТОРНАЯ РАБОТА НОМЕР 4. РЕШЕНИЕ СФЕРИЧЕСКОГО ТРЕУГОЛЬНИКА  ")
print ("ДАНО СТОРОНА b=44797.282(м)+300м*n, где n - номер варианта")
print ("ЗНАЧЕНИЯ СФЕРИЧЕСКИХ УГЛОВ ПРИНЯТЬ ИЗ ПРИМЕРА ДАННОЙ РАБОТЫ")
print("")
print ("------------------------------РЕШЕНИЕ СФЕРИЧЕСКОГО ТРЕУГОЛЬНИКА СПОСОБОМ АДДИТАМЕНТОВ------------------------------")
print("")
UgolAp=(62.212571*math.pi)/180
UgolBp=(50.339042*math.pi)/180
UgolCp=(67.449916*math.pi)/180
k=0.00000409
f=0.00253
bsfericheskogo=83797.282
bkm=bsfericheskogo/1000
Ab=k*bkm*bkm*bkm
ee=(f*math.sin(UgolAp)*math.sin(UgolCp)*bkm*bkm)/math.sin(UgolBp)
W=((UgolAp+UgolBp+UgolCp)*180/math.pi)-180-ee
delta=(ee/3)/3600
UgolApP=UgolAp-delta
UgolBpP=UgolBp-delta
UgolCpP=UgolCp-delta
bploskogo=bsfericheskogo-Ab
aploskogo=(bsfericheskogo*math.sin(UgolApP))/math.sin(UgolBpP)
akm=aploskogo/1000
cploskogo=(bsfericheskogo*math.sin(UgolCpP))/math.sin(UgolBpP)
ckm=cploskogo/1000
Aa=k*akm*akm*akm
Ac=k*ckm*ckm*ckm
asfericheskogo=aploskogo+Aa
csfericheskogo=cploskogo+Ac
print ("ЗНАЧЕНИЕ СФЕРИЧЕСКИХ УГЛОВ")
print ("Углов А = 62* 12′ 45,257")
print ("Углов B = 50  20  20.552")
print ("Углов C = 67  26  59.701")
print ("ЗНАЧЕНИЕ СИНУСОВ УГЛОВ")
print ("ЗНАЧЕНИЕ СИНУСА УГЛА A = %.8f" %math.sin(UgolAp))
print ("ЗНАЧЕНИЕ СИНУСА УГЛА B = %.8f" %math.sin(UgolBp))
print ("ЗНАЧЕНИЕ СИНУСА УГЛА C = %.8f" %math.sin(UgolCp))
print ("ЗНАЧЕНИЕ ПЛОСКИХ СТОРОН")
print ("ЗНАЧЕНИЕ ПЛОСКОЙ СТОРОНЫ a = %.3f(м)" %aploskogo)
print ("ЗНАЧЕНИЕ ПЛОСКОЙ СТОРОНЫ b = %.3f(м)" %bploskogo)
print ("ЗНАЧЕНИЕ ПЛОСКОЙ СТОРОНЫ c = %.3f(м)" %cploskogo)
print ("ЗНАЧЕНИЕ АДДИТАМЕНТОВ")
print ("ЗНАЧЕНИЕ АДДИТАМЕНТА Aa = %.3f(м)" %Aa)
print ("ЗНАЧЕНИЕ АДДИТАМЕНТА Ab = %.3f(м)" %Ab)
print ("ЗНАЧЕНИЕ АДДИТАМЕНТА Ac = %.3f(м)" %Ac)
print ("ЗНАЧЕНИЕ СФЕРИЧЕСКИХ СТОРОН")
print ("ЗНАЧЕНИЕ СФЕРИЧЕСКОЙ СТОРОНЫ a = %.3f" %asfericheskogo)
print ("ЗНАЧЕНИЕ СФЕРИЧЕСКОЙ СТОРОНЫ b = %.3f" %bsfericheskogo)
print ("ЗНАЧЕНИЕ СФЕРИЧЕСКОЙ СТОРОНЫ c = %.3f" %csfericheskogo)
print ("ЗНАЧЕНИЕ СУММЫ УГЛОВ ТРЕУГОЛЬНИКА = ", ((UgolAp+UgolBp+UgolCp)*180)/math.pi)
print ("ЗНАЧЕНИЕ СФЕРИЧЕСКОГО ИЗБЫТКА = %.3f(сек)" %ee)
print ("ЗНАЧЕНИЕ НЕВЯЗКИ = %.3f" %W)
print ("")

print ("------------------------------РЕШЕНИЕ СФЕРИЧЕСКОГО ТРЕУГОЛЬНИКА ЧЕРЕЗ ТЕОРЕМУ ЛЕЖАНДРА------------------------------")
print("")
  
UgolAp=(62.212571*math.pi)/180
UgolBp=(50.339042*math.pi)/180
UgolCp=(67.449916*math.pi)/180
k=0.00000409
f=0.00253
bsfericheskogo=83797.282
bkm=bsfericheskogo/1000
ee=(f*math.sin(UgolAp)*math.sin(UgolCp)*bkm*bkm)/math.sin(UgolBp)
W=((UgolAp+UgolBp+UgolCp)*180/math.pi)-180-ee
delta=(ee/3)/3600
UgolApP=UgolAp-delta
UgolBpP=UgolBp-delta
UgolCpP=UgolCp-delta
asfericheskogo=(bsfericheskogo*math.sin(UgolApP))/math.sin(UgolBpP)
csfericheskogo=(bsfericheskogo*math.sin(UgolCpP))/math.sin(UgolBpP)
print ("ЗНАЧЕНИЕ СФЕРИЧЕСКОЙ СТОРОНЫ a = %.3f " %asfericheskogo)
print ("ЗНАЧЕНИЕ СФЕРИЧЕСКОЙ СТОРОНЫ b = %.3f " %bsfericheskogo)
print ("ЗНАЧЕНИЕ СФЕРИЧЕСКОЙ СТОРОНЫ c = %.3f" %csfericheskogo)
print ("ЗНАЧЕНИЕ СФЕРИЧЕСКОГО ИЗБЫТКА = %.3f(сек)" %ee)
print ("ЗНАЧЕНИЕ НЕВЯЗКИ = %.3f" %W)
print ("ЗНАЧЕНИЕ СФЕРИЧЕСКОГО УГЛА А = %.6f" %((UgolAp*180)/math.pi))
print ("ЗНАЧЕНИЕ СФЕРИЧЕСКОГО УГЛА B = %.6f" %((UgolBp*180)/math.pi))
print ("ЗНАЧЕНИЕ СФЕРИЧЕСКОГО УГЛА C = %.6f" %((UgolCp*180)/math.pi))
print ("ЗНАЧЕНИЕ ПЛОСКОГО УГЛА А = %.6f" %((UgolApP*180)/math.pi))
print ("ЗНАЧЕНИЕ ПЛОСКОГО УГЛА B = %.6f" %((UgolBpP*180)/math.pi))
print ("ЗНАЧЕНИЕ ПЛОСКОГО УГЛА C = %.6f" %((UgolCpP*180)/math.pi))
print ("ЗНАЧЕНИЕ ПОПРАВОК - ЭПСИЛОН/3 = %.3f" %delta)
print ("ЗНАЧЕНИЕ СУММЫ УГЛОВ ПЛОСКОГО ТРЕУГОЛЬНИКА = ", ((UgolAp+UgolBp+UgolCp)*180)/math.pi)
print ("ЗНАЧЕНИЕ СУММЫ УГЛОВ СФЕРИЧЕСКОГО ТРЕУГОЛЬНИКА = ", ((UgolAp+UgolBp+UgolCp)*180)/math.pi)



