import wpf
import math

from System.Windows import Window

class damageRechnerMitRS(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'damageRechnerMitRS.xaml')



#functions
#vlt lassen sich hammerschlag und todesstoss als w4 einbauen
#TODO catch wenn AT per Ansage auf <0 sinkt was nicht vorkommen sollte
#TODO catch wenn AVGDMG<0 #nicht zwingend notwendig da maximumsbest
def is_empty(liste):
    return liste == []

def avgrechner(avg_helper):
    avg = int(avg_helper[0]) * 3.5 + int(avg_helper[len(avg_helper) - 1])
#TODO if eingabe falls bereits berechnet und falls der mod zweistellig ist
#  (das + finden und alles danach bis ende mitnehmen)
    return avg

def DEFAULTDMG(AT,BE,PA,AVGDMG,RS):
    dmg = (AT - 1 - BE) * 1 / 20 * (1 - 1 / 20 * PA) * (AVGDMG - RS) #die -1 berücksichtigt dass der crit ein seperates ergebnis ist #für
                                                                     #bestaetigung wird dieser jedoch nicht gebraucht 1/400 sind die 1/20 für
                                                                     #bestaetigungswahrscheinlichkeit
    crit = 1 / 20 * (1 - 1 / 20 * math.ceil(PA / 2)) * ((AT - BE) / 20 * ((AVGDMG * 2) - RS) + (1 - (AT - BE) / 20) * (AVGDMG - RS))  
    cdmg = dmg + crit
    return cdmg

def WUCHTSCHLAG1(AT,BE,PA,AVGDMG,RS):
    dmg = (AT - 1 - BE - 2) * 1 / 20 * (1 - 1 / 20 * PA) * (AVGDMG + 2 - RS)
    crit = 1 / 20 * (1 - 1 / 20 * math.ceil(PA / 2)) * ((AT - BE - 2) / 20 * (((AVGDMG + 2) * 2) - RS) + (1 - (AT - BE - 2) / 20) * (AVGDMG + 2 - RS)) 
    cdmg = dmg + crit
    return cdmg

def WUCHTSCHLAG2(AT,BE,PA,AVGDMG,RS):
    dmg = (AT - 1 - BE - 4) * 1 / 20 * (1 - 1 / 20 * PA) * (AVGDMG + 4 - RS)
    crit = 1 / 20 * (1 - 1 / 20 * math.ceil(PA / 2)) * ((AT - BE - 4) / 20 * (((AVGDMG + 4) * 2) - RS) + (1 - (AT - BE - 4) / 20) * (AVGDMG + 4 - RS))  
    cdmg = dmg + crit
    return cdmg

def WUCHTSCHLAG3(AT,BE,PA,AVGDMG,RS):
    dmg = (AT - 1 - BE - 6) * 1 / 20 * (1 - 1 / 20 * PA) * (AVGDMG + 6 - RS)
    crit = 1 / 20 * (1 - 1 / 20 * math.ceil(PA / 2)) * ((AT - BE - 6) / 20 * (((AVGDMG + 6) * 2) - RS) + (1 - (AT - BE - 6) / 20) * (AVGDMG + 6 - RS))  
    cdmg = dmg + crit
    return cdmg

def FINTE1(AT,BE,PA,AVGDMG,RS):
    if PA - 2 <= 0:
        dmg = (AT - 1 - BE - 1) * 1 / 20 * (AVGDMG - RS)
        crit = 1 / 20 * ((AT - BE - 1) / 20 * ((AVGDMG * 2) - RS) + (1 - (AT - BE - 1) / 20) * (AVGDMG - RS)) 

    else:
        dmg = (AT - 1 - BE - 1) * 1 / 20 * (1 - 1 / 20 * (PA - 2)) * (AVGDMG - RS)
        if math.ceil(PA / 2 - 2) > 0:
            crit = 1 / 20 * (1 - 1 / 20 * math.ceil(PA / 2 - 2)) * ((AT - BE - 1) / 20 * ((AVGDMG * 2) - RS) + (1 - (AT - BE - 1) / 20) * (AVGDMG - RS)) #moegliches Problem erst abzuziehen und dann zu runden
        else:
            crit = 1 / 20 * ((AT - BE - 1) / 20 * ((AVGDMG * 2) - RS) + (1 - (AT - BE - 1) / 20) * (AVGDMG - RS))             

    cdmg = dmg + crit
    return cdmg

def FINTE2(AT,BE,PA,AVGDMG,RS):
    if PA - 4 <= 0:
        dmg = (AT - 1 - BE - 2) * 1 / 20 * (AVGDMG - RS)
        crit = 1 / 20 * ((AT - BE - 2) / 20 * ((AVGDMG * 2) - RS) + (1 - (AT - BE - 2) / 20) * (AVGDMG - RS)) 

    else:
        dmg = (AT - 1 - BE - 2) * 1 / 20 * (1 - 1 / 20 * (PA - 4)) * (AVGDMG - RS)
        if math.ceil(PA / 2 - 4) > 0:
            crit = 1 / 20 * (1 - 1 / 20 * math.ceil(PA / 2 - 4)) * ((AT - BE - 2) / 20 * ((AVGDMG * 2) - RS) + (1 - (AT - BE - 2) / 20) * (AVGDMG - RS)) 
        else:
            crit = 1 / 20 * ((AT - BE - 2) / 20 * ((AVGDMG * 2) - RS) + (1 - (AT - BE - 2) / 20) * (AVGDMG - RS))             

    cdmg = dmg + crit
    return cdmg

def FINTE3(AT,BE,PA,AVGDMG,RS):
    if PA - 6 <= 0:
        dmg = (AT - 1 - BE - 3) * 1 / 20 * (AVGDMG - RS)
        crit = 1 / 20 * ((AT - BE - 3) / 20 * ((AVGDMG * 2) - RS) + (1 - (AT - BE - 3) / 20) * (AVGDMG - RS)) 

    else:
        dmg = (AT - 1 - BE - 3) * 1 / 20 * (1 - 1 / 20 * (PA - 6)) * (AVGDMG - RS)
        if math.ceil(PA / 2 - 6) > 0:
            crit = 1 / 20 * (1 - 1 / 20 * math.ceil(PA / 2 - 6)) * ((AT - BE - 3) / 20 * ((AVGDMG * 2) - RS) + (1 - (AT - BE - 3) / 20) * (AVGDMG - RS)) 
        else:
            crit = 1 / 20 * ((AT - BE - 3) / 20 * ((AVGDMG * 2) - RS) + (1 - (AT - BE - 3) / 20) * (AVGDMG - RS))             

    cdmg = dmg + crit
    return cdmg

#sucher des besten wertes bzw der schwellen der PA
def sucher(AT,BE,AVGDMG,RS,SFWoPZ,SFF):
    # die listen
    Default = []
    Wucht1 = []
    Wucht2 = []
    Wucht3 = []
    Finte1 = [] 
    Finte2 = []
    Finte3 = [] #heißen genau wie funktions nur klein ist vlt etwas haesslich
    #standardvalues für deaktivert
    w1 = 0
    w2 = 0
    w3 = 0
    f1 = 0
    f2 = 0
    f3 = 0
    for PA in range(21):
        d = DEFAULTDMG(AT,BE,PA,AVGDMG,RS)
    #if für das vorhandensein anderer sfs

        if 0 < SFWoPZ: #supoptimal in der for schleife
            w1 = WUCHTSCHLAG1(AT,BE,PA,AVGDMG,RS)
        if 1 < SFWoPZ:
            w2 = WUCHTSCHLAG2(AT,BE,PA,AVGDMG,RS)
        if 3 == SFWoPZ:
            w3 = WUCHTSCHLAG3(AT,BE,PA,AVGDMG,RS)
        if 0 < SFF:
            f1 = FINTE1(AT,BE,PA,AVGDMG,RS)
        if 1 < SFF:
            f2 = FINTE2(AT,BE,PA,AVGDMG,RS)
        if 3 == SFF:    
            f3 = FINTE3(AT,BE,PA,AVGDMG,RS)

        list1 = [d,w1,w2,w3,f1,f2,f3]

        m = max(list1)
    
        if d == m:
            Default+=[PA]
        elif f1 == m:
            Finte1+=[PA]
        elif f2 == m:
            Finte2+=[PA]
        elif f3 == m:
            Finte3+=[PA]
        elif w1 == m:
            Wucht1+=[PA]
        elif w2 == m:
            Wucht2+=[PA]
        elif w3 == m:
            Wucht3+=[PA]

    res = 'bei RS ' + str(RS) + ':' + '\n'

    if not is_empty(Default):
        res+='Default ist am besten bei PA Werten von ' + str(Default[0]) + '-' + str(Default[len(Default) - 1]) + '\n'
    if SFWoPZ >= 1:
        if not is_empty(Wucht1):
            res+='Wuchtschlag I bzw Praeziser Stich I ist am besten bei PA Werten von ' + str(Wucht1[0]) + '-' + str(Wucht1[len(Wucht1) - 1]) + '\n'
    if SFWoPZ >= 2:
        if not is_empty(Wucht2):
            res+='Wuchtschlag II bzw Praeziser Stich II ist am besten bei PA Werten von ' + str(Wucht2[0]) + '-' + str(Wucht2[len(Wucht2) - 1]) + '\n'
    if SFWoPZ >= 3:
        if not is_empty(Wucht3):
            res+='Wuchtschlag III bzw Praeziser Stich III ist am besten bei PA Werten von ' + str(Wucht3[0]) + '-' + str(Wucht3[len(Wucht3) - 1]) + '\n'
    if SFF >= 1:
        if not is_empty(Finte1):
            res+='Finte I ist am besten bei PA Werten von ' + str(Finte1[0]) + '-' + str(Finte1[len(Finte1) - 1]) + '\n'
    if SFF >= 2:
        if not is_empty(Finte2):
            res+='Finte II ist am besten bei PA Werten von ' + str(Finte2[0]) + '-' + str(Finte2[len(Finte2) - 1]) + '\n'
    if SFF >= 3:
        if not is_empty(Finte3):
            res+='Finte III ist am besten bei PA Werten von ' + str(Finte3[0]) + '-' + str(Finte3[len(Finte3) - 1]) + '\n'
    print(res)
    #print([Default,Wucht1,Wucht2,Wucht3,Finte1,Finte2,Finte3])
def rsdmg(AT,BE,AVGDMG,SFWoPZ,SFF): #TODO rs von bis einstellbar
    for RS in range(8):
        sucher(AT,BE,AVGDMG,RS,SFWoPZ,SFF)
