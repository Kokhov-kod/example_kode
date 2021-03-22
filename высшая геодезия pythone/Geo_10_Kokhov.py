import math

PI = math.pi
class Variant:
   def zadanie1():
        #rep36 /
        #rep50 /
        #rep77 /
        #rep91 /
        #rep92 /
        #rep60
        #rep52
        #rep36
        Brep36=46.45*PI/180
        UrGeoNumrep36=144.79771#kGal
        GravForcerep36=980887.9#mGal
        anomalGravForcerep36=6#mGal
        gravimAnomHrep36=51.2#mGal
        geodeticHrep36=198.3174#m
        
        Brep50=47.93*PI/180
        UrGeoNumrep50=111.43103#kGal
        GravForcerep50=980866.9#mGal
        anomalGravForcerep50=21#mGal
        gravimAnomHrep50=52.32#mGal
        geodeticHrep50=165.4537
#m
        
        Brep77=47.3*PI/180
        UrGeoNumrep77=49.78489#kGal
        GravForcerep77=980816.2#mGal
        anomalGravForcerep77=5#mGal
        gravimAnomHrep77=50.18#mGal
        geodeticHrep77=100.4063
#m
        
        Brep91=46.96*PI/180
        UrGeoNumrep91=75.889124#kGal
        GravForcerep91=980816.2#mGal
        anomalGravForcerep91=92#mGal
        gravimAnomHrep91=49.75#mGal
        geodeticHrep91=126.5837#m
        
        Brep92=46.96*PI/180
        UrGeoNumrep92=85.390227#kGal
        GravForcerep92=980781.9#mGal
        anomalGravForcerep92=91#mGal
        gravimAnomHrep92=49.74#mGal
        geodeticHrep92=136.9296#m
        
        Brep60=47.6*PI/180
        UrGeoNumrep60=33.609395#kGal
        GravForcerep60=980864.5#mGal
        anomalGravForcerep60=18#mGal
        gravimAnomHrep60=52.61#mGal
        geodeticHrep60=85.8617#m
        
        Brep52=47.9*PI/180
        UrGeoNumrep52=83.208039#kGal
        GravForcerep52=980851.8#mGal
        anomalGravForcerep52=0#mGal
        gravimAnomHrep52=51.5#mGal
        geodeticHrep52=135.7951#m
        
        prev36_50=-34.0116
        prev50_77=-62.8539 
        prev77_91=-26.6212
        prev91_92=9.6872
        prev92_60=-53.3066
        prev60_52=51.0840
        prev52_36=62.7868
         
        sekcia36_50=121.07
        sekcia50_77=105.93
        sekcia77_91=86.96
        sekcia91_92=16
        sekcia92_60=117.92
        sekcia60_52=39
        sekcia52_36=185.87
         
        # prev36_50=-30.0484
        # prev50_77=56.2003
        # prev77_91=-28.2244
        # prev91_92=-6.3207
        # prev92_60=-91.6928
        # prev60_52=24.0567
         
         #sekcia36_50=95.97
         #sekcia50_77=109.89
         #sekcia77_91=36
         #sekcia91_92=95.06
         #sekcia92_60=9
         #sekcia60_52=59.03
        print("----------------------------------------------------------------------------------------------------------------------------")
        print("-----ЗАДАНИЕ НОМЕР 1. ВЫЧИСЛЕНИЕ ГЕОПОТЕНЦИАЛЬНОГО ЧИСЛА-----")
        print("----------------------------------------------------------------------------------------------------------------------------")
        raznpot36_50=GravForcerep36/1000000*prev36_50
        raznpot50_77=GravForcerep50/1000000*prev50_77
        raznpot77_91=GravForcerep77/1000000*prev77_91
        raznpot91_92=GravForcerep91/1000000*prev91_92
        raznpot92_60=GravForcerep92/1000000*prev92_60
        raznpot60_52=GravForcerep60/1000000*prev60_52
        raznpot52_36=GravForcerep52/1000000*prev52_36
        
        sumraznpot=raznpot52_36+raznpot36_50+raznpot50_77+raznpot77_91+raznpot91_92+raznpot92_60+raznpot60_52
        raznpot36_50ur=raznpot36_50-sumraznpot/7
        raznpot50_77ur=raznpot50_77-sumraznpot/7
        raznpot77_91ur=raznpot77_91-sumraznpot/7
        raznpot91_92ur=raznpot91_92-sumraznpot/7
        raznpot92_60ur=raznpot92_60-sumraznpot/7
        raznpot60_52ur=raznpot60_52-sumraznpot/7
        raznpot52_36ur=raznpot52_36-sumraznpot/7
        
        GeoNum50=UrGeoNumrep36+raznpot36_50ur
        GeoNum77=GeoNum50+raznpot50_77ur
        GeoNum91=GeoNum77+raznpot77_91ur
        GeoNum92=GeoNum91+raznpot91_92ur
        GeoNum60=GeoNum92+raznpot92_60ur
        GeoNum52=GeoNum60+raznpot60_52ur
        GeoNum36=GeoNum52+raznpot52_36ur
        
        sumprev=prev36_50+prev50_77+prev77_91+prev91_92+prev92_60+prev60_52+prev52_36
        sumraznpotur=raznpot36_50ur+raznpot50_77ur+raznpot77_91ur+raznpot91_92ur+raznpot92_60ur+raznpot60_52ur+raznpot52_36ur
        print()
        print("Значение параметра разности потенциалов W1-W1 при реперах 50 36 = %.9f" %raznpot36_50)
        print("Значение параметра разности потенциалов W1-W1 при реперах 77 50 = %.9f" %raznpot50_77)
        print("Значение параметра разности потенциалов W1-W1 при реперах 91 77 = %.9f" %raznpot77_91)
        print("Значение параметра разности потенциалов W1-W1 при реперах 92 91 = %.9f" %raznpot91_92)
        print("Значение параметра разности потенциалов W1-W1 при реперах 60 92 = %.9f" %raznpot92_60)
        print("Значение параметра разности потенциалов W1-W1 при реперах 52 60 = %.9f" %raznpot60_52)
        print("Значение параметра разности потенциалов W1-W1 при реперах 36 52 = %.9f" %raznpot52_36)
        print()
        print("Значение параметра уравненной разности потенциалов W1-W2 при реперах 50 36 = %.9f" %raznpot36_50ur)
        print("Значение параметра уравненной разности потенциалов W1-W2 при реперах 77 50 = %.9f" %raznpot50_77ur)
        print("Значение параметра уравненной разности потенциалов W1-W2 при реперах 91 77 = %.9f" %raznpot77_91ur)
        print("Значение параметра уравненной разности потенциалов W1-W2 при реперах 92 91 = %.9f" %raznpot91_92ur)
        print("Значение параметра уравненной разности потенциалов W1-W2 при реперах 60 92 = %.9f" %raznpot92_60ur)
        print("Значение параметра уравненной разности потенциалов W1-W2 при реперах 52 60  = %.9f" %raznpot60_52ur)
        print("Значение параметра уравненной разности потенциалов W1-W2 при реперах 36 52 = %.9f" %raznpot52_36ur)
        print()
        print("Значение параметра геопотенциального числа W0-W при репере 36 = %.9f" %UrGeoNumrep36)
        print("Значение параметра геопотенциального числа W0-W при репере 50 = %.9f" %GeoNum50)
        print("Значение параметра геопотенциального числа W0-W при репере 77 = %.9f" %GeoNum77)
        print("Значение параметра геопотенциального числа W0-W при репере 91 = %.9f" %GeoNum91)
        print("Значение параметра геопотенциального числа W0-W при репере 92 = %.9f" %GeoNum92)
        print("Значение параметра геопотенциального числа W0-W при репере 60 = %.9f" %GeoNum60)
        print("Значение параметра геопотенциального числа W0-W при репере 52 = %.9f" %GeoNum52)
        print()
        print("Значение параметра геопотенциального числа W0-W при репере 36 контрольное = %.9f" %GeoNum36)
        print("Значение параметра суммы превышений = %.9f" %sumprev)
        print("Значение параметра суммы разности потенциалов = %.9f" %sumraznpot)
        print("Значение параметра суммы уравненной разности потенциалов = %.9f" %sumraznpotur)
        print("----------------------------------------------------------------------------------------------------------------------------")
        print("-----ЗАДАНИЕ НОМЕР 2. ВЫЧИСЛЕНИЕ НОРМАЛЬНОЙ И ДИНАМИЧЕСКОЙ ВЫСОТЫ-----")
        print("----------------------------------------------------------------------------------------------------------------------------")
        normHpervrep36=GeoNum36*GravForcerep36/1000000
        normHpervrep50=GeoNum50*GravForcerep50/1000000
        normHpervrep77=GeoNum77*GravForcerep77/1000000
        normHpervrep91=GeoNum91*GravForcerep91/1000000
        normHpervrep92=GeoNum92*GravForcerep92/1000000
        normHpervrep60=GeoNum60*GravForcerep60/1000000
        normHpervrep52=GeoNum52*GravForcerep52/1000000
        normHvtorrep36=GeoNum36/(GravForcerep36-0.91443*normHpervrep36)*1000000
        normHvtorrep50=GeoNum50/(GravForcerep50-0.91443*normHpervrep50)*1000000
        normHvtorrep77=GeoNum77/(GravForcerep77-0.91443*normHpervrep77)*1000000
        normHvtorrep91=GeoNum91/(GravForcerep91-0.91443*normHpervrep91)*1000000
        normHvtorrep92=GeoNum92/(GravForcerep92-0.91443*normHpervrep92)*1000000
        normHvtorrep60=GeoNum60/(GravForcerep60-0.91443*normHpervrep60)*1000000
        normHvtorrep52=GeoNum52/(GravForcerep52-0.91443*normHpervrep52)*1000000
        dinamHrep36=GeoNum36/GravForcerep36*1000000
        dinamHrep50=GeoNum50/GravForcerep50*1000000
        dinamHrep77=GeoNum77/GravForcerep77*1000000
        dinamHrep91=GeoNum91/GravForcerep91*1000000
        dinamHrep92=GeoNum92/GravForcerep92*1000000
        dinamHrep60=GeoNum60/GravForcerep60*1000000
        dinamHrep52=GeoNum52/GravForcerep52*1000000
        raznostH36=(dinamHrep36-normHvtorrep36)*1000
        raznostH50=(dinamHrep50-normHvtorrep50)*1000
        raznostH77=(dinamHrep77-normHvtorrep77)*1000
        raznostH91=(dinamHrep91-normHvtorrep91)*1000
        raznostH92=(dinamHrep92-normHvtorrep92)*1000
        raznostH60=(dinamHrep60-normHvtorrep60)*1000
        raznostH52=(dinamHrep52-normHvtorrep52)*1000
        print("Значение параметра нормальной высоты репера 36 в первом приближении = %.9f" %normHpervrep36)
        print("Значение параметра нормальной высоты репера 50 в первом приближении = %.9f" %normHpervrep50)
        print("Значение параметра нормальной высоты репера 77 в первом приближении = %.9f" %normHpervrep77)
        print("Значение параметра нормальной высоты репера 91 в первом приближении = %.9f" %normHpervrep91)
        print("Значение параметра нормальной высоты репера 92 в первом приближении = %.9f" %normHpervrep92)
        print("Значение параметра нормальной высоты репера 60 в первом приближении = %.9f" %normHpervrep60)
        print("Значение параметра нормальной высоты репера 52 в первом приближении = %.9f" %normHpervrep52)
        print()
        print("Значение параметра нормальной высоты репера 36 во втором приближении = %.9f" %normHvtorrep36)
        print("Значение параметра нормальной высоты репера 50 во втором приближении = %.9f" %normHvtorrep50)
        print("Значение параметра нормальной высоты репера 77 во втором приближении = %.9f" %normHvtorrep77)
        print("Значение параметра нормальной высоты репера 91 во втором приближении = %.9f" %normHvtorrep91)
        print("Значение параметра нормальной высоты репера 92 во втором приближении = %.9f" %normHvtorrep92)
        print("Значение параметра нормальной высоты репера 60 во втором приближении = %.9f" %normHvtorrep60)
        print("Значение параметра нормальной высоты репера 52 во втором приближении = %.9f" %normHvtorrep52)
        print()
        print("Значение параметра динамической высоты репера 36 = %.9f" %dinamHrep36)
        print("Значение параметра динамической высоты репера 50 = %.9f" %dinamHrep50)
        print("Значение параметра динамической высоты репера 77 = %.9f" %dinamHrep77)
        print("Значение параметра динамической высоты репера 91 = %.9f" %dinamHrep91)
        print("Значение параметра динамической высоты репера 92 = %.9f" %dinamHrep92)
        print("Значение параметра динамической высоты репера 60 = %.9f" %dinamHrep60)
        print("Значение параметра динамической высоты репера 52 = %.9f" %dinamHrep52)
        print()
        print("Значение параметра разности динамической высоты и нормальной высоты репера 36 в мм = %.9f" %raznostH36)
        print("Значение параметра разности динамической высоты и нормальной высоты репера 50 в мм = %.9f" %raznostH50)
        print("Значение параметра разности динамической высоты и нормальной высоты репера 77 в мм = %.9f" %raznostH77)
        print("Значение параметра разности динамической высоты и нормальной высоты репера 91 в мм = %.9f" %raznostH91)
        print("Значение параметра разности динамической высоты и нормальной высоты репера 92 в мм = %.9f" %raznostH92)
        print("Значение параметра разности динамической высоты и нормальной высоты репера 60 в мм = %.9f" %raznostH60)
        print("Значение параметра разности динамической высоты и нормальной высоты репера 52 в мм = %.9f" %raznostH52)
        print("----------------------------------------------------------------------------------------------------------------------------")
        print("-----ЗАДАНИЕ НОМЕР 3. ВЫЧИСЛЕНИЕ ТЕОРЕТИЧЕСКОЙ СУММЫ ПРЕВЫШЕНИЙ-----")
        print("----------------------------------------------------------------------------------------------------------------------------")
        gm36_50=(GravForcerep50+GravForcerep36)/2
        gm50_77=(GravForcerep77+GravForcerep50)/2
        gm77_91=(GravForcerep91+GravForcerep77)/2
        gm91_92=(GravForcerep92+GravForcerep91)/2
        gm92_60=(GravForcerep60+GravForcerep92)/2
        gm60_52=(GravForcerep52+GravForcerep60)/2
        gm52_36=(GravForcerep36+GravForcerep52)/2
        g0=gm91_92
        
        gm_g0_36_50=gm36_50-g0
        gm_g0_50_77=gm50_77-g0
        gm_g0_77_91=gm77_91-g0
        gm_g0_91_92=gm91_92-g0
        gm_g0_92_60=gm92_60-g0
        gm_g0_60_52=gm60_52-g0
        gm_g0_52_36=gm60_52-g0
        #вывод превышений
        gm_g0_h_g0_36_50=gm_g0_36_50*prev36_50/g0
        gm_g0_h_g0_50_77=gm_g0_50_77*prev50_77/g0
        gm_g0_h_g0_77_91=gm_g0_77_91*prev77_91/g0
        gm_g0_h_g0_91_92=gm_g0_91_92*prev91_92/g0
        gm_g0_h_g0_92_60=gm_g0_92_60*prev92_60/g0
        gm_g0_h_g0_60_52=gm_g0_60_52*prev60_52/g0
        gm_g0_h_g0_52_36=gm_g0_52_36*prev52_36/g0
        sumgmg0=gm_g0_h_g0_36_50+gm_g0_h_g0_50_77+gm_g0_h_g0_77_91+gm_g0_h_g0_91_92+gm_g0_h_g0_92_60+gm_g0_h_g0_60_52+gm_g0_h_g0_52_36
        urprev36_50=prev36_50+sumgmg0/7
        urprev50_77=prev50_77+sumgmg0/7
        urprev77_91=prev77_91+sumgmg0/7
        urprev91_92=prev91_92+sumgmg0/7
        urprev92_60=prev92_60+sumgmg0/7
        urprev60_52=prev60_52+sumgmg0/7
        urprev52_36=prev52_36+sumgmg0/7
        sumurprev=urprev36_50+urprev50_77+urprev77_91+urprev91_92+urprev92_60+urprev60_52+urprev52_36
        fh=sumprev+sumurprev
        print("Значение параметра gm при реперах 50 36 = %.9f" %gm36_50)
        print("Значение параметра gm при реперах 77 50 = %.9f" %gm50_77)
        print("Значение параметра gm при реперах 91 77 = %.9f" %gm77_91)
        print("Значение параметра gm при реперах 92 91 = %.9f" %gm91_92)
        print("Значение параметра gm при реперах 60 92 = %.9f" %gm92_60)
        print("Значение параметра gm при реперах 52 60 = %.9f" %gm60_52)
        print("Значение параметра gm при реперах 36 52 = %.9f" %gm52_36)
        print()
        print("Значение параметра gm-g0 при реперах 50 36 = %.9f" %gm_g0_36_50)
        print("Значение параметра gm-g0 при реперах 77 50 = %.9f" %gm_g0_50_77)
        print("Значение параметра gm-g0 при реперах 91 77 = %.9f" %gm_g0_77_91)
        print("Значение параметра gm-g0 при реперах 92 91 = %.9f" %gm_g0_91_92)
        print("Значение параметра gm-g0 при реперах 60 92 = %.9f" %gm_g0_92_60)
        print("Значение параметра gm-g0 при реперах 52 60 = %.9f" %gm_g0_60_52)
        print("Значение параметра gm-g0 при реперах 36 52 = %.9f" %gm_g0_52_36)
        print()
        print("Значение превышения при реперах 50 36 = %.9f" %prev36_50)
        print("Значение превышения при реперах 77 50 = %.9f" %prev50_77)
        print("Значение превышения при реперах 91 77 = %.9f" %prev77_91)
        print("Значение превышения при реперах 92 91 = %.9f" %prev91_92)
        print("Значение превышения при реперах 60 92 = %.9f" %prev92_60)
        print("Значение превышения при реперах 52 60 = %.9f" %prev60_52)
        print("Значение превышения при реперах 36 52 = %.9f" %prev52_36)
        print()
        print("Значение параметра (gm-g0)*h/g0 при реперах 50 36 = %.9f" %gm_g0_h_g0_36_50)
        print("Значение параметра (gm-g0)*h/g0 при реперах 77 50 = %.9f" %gm_g0_h_g0_50_77)
        print("Значение параметра (gm-g0)*h/g0 при реперах 91 77 = %.9f" %gm_g0_h_g0_77_91)
        print("Значение параметра (gm-g0)*h/g0 при реперах 92 91 = %.9f" %gm_g0_h_g0_91_92)
        print("Значение параметра (gm-g0)*h/g0 при реперах 60 92 = %.9f" %gm_g0_h_g0_92_60)
        print("Значение параметра (gm-g0)*h/g0 при реперах 52 60 = %.9f" %gm_g0_h_g0_60_52)
        print("Значение параметра (gm-g0)*h/g0 при реперах 36 52 = %.9f" %gm_g0_h_g0_52_36)
        print()
        print("Значение уравненного превышения при реперах 50 36 = %.9f" %urprev36_50)
        print("Значение уравненного превышения при реперах 77 50 = %.9f" %urprev50_77)
        print("Значение уравненного превышения при реперах 91 77 = %.9f" %urprev77_91)
        print("Значение уравненного превышения при реперах 92 91 = %.9f" %urprev91_92)
        print("Значение уравненного превышения при реперах 60 92 = %.9f" %urprev92_60)
        print("Значение уравненного превышения при реперах 52 60 = %.9f" %urprev60_52)
        print("Значение уравненного превышения при реперах 36 52 = %.9f" %urprev52_36)
        print()
        print("Значение параметра суммы (gm-g0)*h/g0 = %.9f" %sumgmg0)
        print("Значение параметра суммы уравненных превышений = %.9f" %sumurprev)
        print("Значение параметра невязки = %.9f" %fh)
        print("----------------------------------------------------------------------------------------------------------------------------")
        print("-----ЗАДАНИЕ НОМЕР 4. ВЫЧИСЛЕНИЕ РАЗНОСТИ НОРМАЛЬНЫХ ВЫСОТ-----")
        print("----------------------------------------------------------------------------------------------------------------------------")
        srAnomalrep50_36=(anomalGravForcerep50+anomalGravForcerep36)/2
        srAnomalrep77_50=(anomalGravForcerep77+anomalGravForcerep50)/2
        srAnomalrep91_77=(anomalGravForcerep91+anomalGravForcerep77)/2
        srAnomalrep92_91=(anomalGravForcerep92+anomalGravForcerep91)/2
        srAnomalrep60_92=(anomalGravForcerep60+anomalGravForcerep92)/2
        srAnomalrep52_60=(anomalGravForcerep52+anomalGravForcerep60)/2
        srAnomalrep36_52=(anomalGravForcerep36+anomalGravForcerep52)/2
        srNormGravForcerep50_36=GravForcerep50-GravForcerep36
        srNormGravForcerep77_50=GravForcerep77-GravForcerep50
        srNormGravForcerep91_77=GravForcerep91-GravForcerep77
        srNormGravForcerep92_91=GravForcerep92-GravForcerep91
        srNormGravForcerep60_92=GravForcerep60-GravForcerep92
        srNormGravForcerep52_60=GravForcerep52-GravForcerep60
        srNormGravForcerep36_52=GravForcerep36-GravForcerep52
        popravRaznNormH=sumurprev/7
        RaznNormH50_36=normHvtorrep50-normHvtorrep36+popravRaznNormH
        RaznNormH77_50=normHvtorrep77-normHvtorrep50+popravRaznNormH
        RaznNormH91_77=normHvtorrep91-normHvtorrep77+popravRaznNormH
        RaznNormH92_91=normHvtorrep92-normHvtorrep91+popravRaznNormH
        RaznNormH60_92=normHvtorrep60-normHvtorrep92+popravRaznNormH
        RaznNormH52_60=normHvtorrep36-normHvtorrep60+popravRaznNormH
        RaznNormH36_52=normHvtorrep36-normHvtorrep60+popravRaznNormH
        rezH36=dinamHrep36
        rezH50=rezH36+RaznNormH50_36
        rezH77=rezH50+RaznNormH77_50
        rezH91=rezH77+RaznNormH91_77
        rezH92=rezH91+RaznNormH92_91
        rezH60=rezH92+RaznNormH60_92
        rezH52=rezH60+RaznNormH52_60
        rezH36kontrol=rezH52+RaznNormH52_60
        print("Значение параметра средней аномалии силы тяжести при реперах 50 36 = %.9f" %srAnomalrep50_36)
        print("Значение параметра средней аномалии силы тяжести при реперах 77 50 = %.9f" %srAnomalrep77_50)
        print("Значение параметра средней аномалии силы тяжести при реперах 91 77 = %.9f" %srAnomalrep91_77)
        print("Значение параметра средней аномалии силы тяжести при реперах 92 91 = %.9f" %srAnomalrep92_91)
        print("Значение параметра средней аномалии силы тяжести при реперах 60 92 = %.9f" %srAnomalrep60_92)
        print("Значение параметра средней аномалии силы тяжести при реперах 52 60 = %.9f" %srAnomalrep52_60)
        print("Значение параметра средней аномалии силы тяжести при реперах 36 52 = %.9f" %srAnomalrep36_52)
        print()
        print("Значение средней нормальной силы тяжести при реперах 50 36 = %.9f" % srNormGravForcerep50_36)
        print("Значение средней нормальной силы тяжести при реперах 77 50 = %.9f" %srNormGravForcerep77_50)
        print("Значение средней нормальной силы тяжести при реперах 91 77 = %.9f" %srNormGravForcerep91_77)
        print("Значение средней нормальной силы тяжести при реперах 92 91 = %.9f" %srNormGravForcerep92_91)
        print("Значение средней нормальной силы тяжести при реперах 60 92 = %.9f" %srNormGravForcerep60_92)
        print("Значение средней нормальной силы тяжести при реперах 52 60 = %.9f" %srNormGravForcerep52_60)
        print("Значение средней нормальной силы тяжести при реперах 36 52 = %.9f" %srNormGravForcerep36_52)
        print()
        print("Значение параметра поправки в превышение = %.9f" %popravRaznNormH)
        print("Значение параметра разности нормальных высот при реперах 50 36 = %.9f" %RaznNormH50_36)
        print("Значение параметра разности нормальных высот при реперах 77 50 = %.9f" %RaznNormH77_50)
        print("Значение параметра разности нормальных высот при реперах 91 77 = %.9f" %RaznNormH91_77)
        print("Значение параметра разности нормальных высот при реперах 92 91 = %.9f" %RaznNormH92_91)
        print("Значение параметра разности нормальных высот при реперах 60 92 = %.9f" %RaznNormH60_92)
        print("Значение параметра разности нормальных высот при реперах 52 60 = %.9f" %RaznNormH52_60)
        print("Значение параметра разности нормальных высот при реперах 36 52 = %.9f" %RaznNormH36_52)
        print()
        print("Значение нормальной высоты репера 36 = %.9f" %rezH36)
        print("Значение нормальной высоты репера 50 = %.9f" %rezH50)
        print("Значение нормальной высоты репера 77 = %.9f" %rezH77)
        print("Значение нормальной высоты репера 91 = %.9f" %rezH91)
        print("Значение нормальной высоты репера 92 = %.9f" %rezH92)
        print("Значение нормальной высоты репера 60 = %.9f" %rezH60)
        print("Значение нормальной высоты репера 36 с контролем = %.9f" %rezH36kontrol)
        print("----------------------------------------------------------------------------------------------------------------------------")
        print("-----ЗАДАНИЕ НОМЕР 5. СПУТНИКОВОЕ НИВЕЛИРОВАНИЕ-----")
        print("----------------------------------------------------------------------------------------------------------------------------")
        Hcrep91=geodeticHrep91-gravimAnomHrep91
        Hcrep92=geodeticHrep92-gravimAnomHrep92
        Hcrep36=geodeticHrep36-gravimAnomHrep36
        Hcrep60=geodeticHrep60-gravimAnomHrep60
        Hm_Hcrep91=rezH91-Hcrep91
        Hm_Hcrep92=rezH92-Hcrep92
        Hm_Hcrep36=rezH36-Hcrep36
        Hm_Hcrep60=rezH60-Hcrep60
        Lrep91=0
        Lrep92=95.06
        Lrep60=95.06+9
        Lrep36=Lrep60+59.03
        k=(Hm_Hcrep91+Hm_Hcrep36)/Lrep36
        Hm_Hcrep91int=Hm_Hcrep91+k*Lrep91
        Hm_Hcrep92int=Hm_Hcrep92+k*Lrep92
        Hm_Hcrep36int=Hm_Hcrep36+k*Lrep36
        Hm_Hcrep60int=Hm_Hcrep60+k*Lrep60
        Hrep91int=Hcrep91+Hm_Hcrep91int
        Hrep92int=Hcrep92+Hm_Hcrep92int
        Hrep60int=Hcrep60+Hm_Hcrep60int
        Hrep36int=Hcrep36+Hm_Hcrep36int
        delHrep91=Hm_Hcrep91-Hm_Hcrep91int
        delHrep92=Hm_Hcrep92-Hm_Hcrep92int
        delHrep60=Hm_Hcrep60-Hm_Hcrep60int
        delHrep36=Hm_Hcrep36-Hm_Hcrep36int
        print("Значение параметра Hc репера 91 = %.9f" %Hcrep91)
        print("Значение параметра Hc репера 92 = %.9f" %Hcrep92)
        print("Значение параметра Hc репера 36 = %.9f" %Hcrep36)
        print("Значение параметра Hc репера 60 = %.9f" %Hcrep60)
        print()
        print("Значение параметра разности высот Молоденского и нормальной спутниковой высоты репера 91 = %.9f" %Hm_Hcrep91)
        print("Значение параметра разности высот Молоденского и нормальной спутниковой высоты репера 92 = %.9f" %Hm_Hcrep92)
        print("Значение параметра разности высот Молоденского и нормальной спутниковой высоты репера 36 = %.9f" %Hm_Hcrep36)
        print("Значение параметра разности высот Молоденского и нормальной спутниковой высоты репера 60 = %.9f" %Hm_Hcrep60)
        print()
        print("Значение параметра расстояния от репера 91 до репера 91 = %.9f" %Lrep91)
        print("Значение параметра расстояния от репера 91 до репера 92 = %.9f" %Lrep92)
        print("Значение параметра расстояния от репера 91 до репера 60 = %.9f" %Lrep60)
        print("Значение параметра расстояния от репера 91 до репера 36 = %.9f" %Lrep36)
        print("Значение параметра k = %.9f" %k)
        print()
        print("Значение параметра интерполированной разности высоты Молоденского и нормальной спутниковой высоты репера 91 = %.9f" %Hm_Hcrep91int)
        print("Значение параметра интерполированной разности высоты Молоденского и нормальной спутниковой высоты репера 92 = %.9f" %Hm_Hcrep92int)
        print("Значение параметра интерполированной разности высоты Молоденского и нормальной спутниковой высоты репера 36 = %.9f" %Hm_Hcrep36int)
        print("Значение параметра интерполированной разности высоты Молоденского и нормальной спутниковой высоты репера 60 = %.9f" %Hm_Hcrep60int)
        print()
        print("Значение параметра интерполированной высоты Молоденского репера 91 = %.9f" %Hrep91int)
        print("Значение параметра интерполированной высоты Молоденского репера 92 = %.9f" %Hrep92int)
        print("Значение параметра интерполированной высоты Молоденского репера 36 = %.9f" %Hrep36int)
        print("Значение параметра интерполированной высоты Молоденского репера 60 = %.9f" %Hrep60int)
        print()
        print("----------------------------------------------------------------------------------------------------------------------------")
        print("-----ЗАДАНИЕ НОМЕР 6. ОЦЕНКА ТОЧНОСТИ-----")
        print("----------------------------------------------------------------------------------------------------------------------------")
        slychoshgeomniv=fh/math.sqrt(sekcia36_50+sekcia50_77+sekcia77_91+sekcia91_92+sekcia92_60+sekcia60_52+sekcia52_36)
        MHc=math.sqrt(((delHrep92*delHrep92)+(delHrep60*delHrep60)+(delHrep36*delHrep36))/3)
        slychoshspytniv=MHc/(math.sqrt(Lrep92+Lrep60+Lrep36))
        print("Значение случайной ошибки геометрического нивелирования в миллиметрах = %.6f" %(slychoshgeomniv*1000))
        print("Значение точности спутникового нивелирования в метрах = %.6f" %MHc)
        print("Значение случайной ошибки спутникового нивелирования в сантиметрах = %.6f" %(slychoshspytniv*100))
print("-------Практическая работа номер 10. Вычисление нормальных и динамических высот. Вариант номер 13--------")
print()
Variant.zadanie1()
