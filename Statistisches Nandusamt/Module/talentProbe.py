import wpf

from System.Windows import Window

class talentProbe(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'talentProbe.xaml')

def Talentprobe(FW,E1,E2,E3,D):
    QS0=0
    QS1=0
    QS2=0
    QS3=0
    QS4=0
    QS5=0
    QS6=0
    E1-=D
    E2-=D
    E3-=D
    for R1 in range(1,21):
        A1=0
        Patzer1=0
        Crit1=0
        if R1==1:
            Crit1=1
        elif R1==20:
            Patzer1=1
            A1=(R1-E1)
        elif R1>E1:
            A1=(R1-E1)
        for R2 in range(1,21):
                A2=0
                Patzer2=0
                Crit2=0
                if R2==1:
                    Crit2=1
                elif R2==20:
                    Patzer2=1
                    A2=(R2-E2)
                elif R2>E2:
                    A2=(R2-E2)
                for R3 in range(1,21):
                    A3=0
                    Patzer3=0
                    Crit3=0
                    if R3==1:
                        Crit3=1
                    elif R3==20:
                        Patzer3=1
                        A3=(R3-E3)
                    elif R3>E3:
                        A3=(R3-E3)
                    P=Patzer1+Patzer2+Patzer3
                    C=Crit1+Crit2+Crit3
                    if P>1:
                        FP=0
                    elif C>1:
                        FP=FW
                    else:
                        FP=FW-A1-A2-A3
                    QS=Qualitätsstufe(FP)
                    if QS == 0:
                        QS0+=1
                    elif QS==1:
                        QS1+=1
                    elif QS==2:
                        QS2+=1
                    elif QS==3:
                        QS3+=1
                    elif QS==4:
                        QS4+=1                    
                    elif QS==5:
                        QS5+=1
                    elif QS==6:
                        QS6+=1
    p0=convert_to_percantage(QS0)   
    p1=convert_to_percantage(QS1)   
    p2=convert_to_percantage(QS2)   
    p3=convert_to_percantage(QS3)   
    p4=convert_to_percantage(QS4)   
    p5=convert_to_percantage(QS5)   
    p6=convert_to_percantage(QS6)   
    res=convert_to_answer(p0,p1,p2,p3,p4,p5,p6)
    return res

def convert_to_percantage(num):
    num=num/8000*100
    num=int(num*100)/100
    return str(num)+'%'

def convert_to_answer(p0,p1,p2,p3,p4,p5,p6):
    res= 'QS0: '+p0+'\n'+'QS1: '+p1+'\n'+'QS2: '+p2+'\n'+'QS3: '+p3+'\n'+'QS4: '+p4+'\n'+'QS5: '+p5+'\n'+'QS6: '+p6+'\n'
    return res

def Qualitätsstufe(FP):
    if FP==0:
        return 1
    elif FP<0:
        return 0
    else:
        return math.ceil(FP/3)

def Erschwernisrotation(FW,E1,E2,E3):
    for D in range(-3,4):
        if D<0:
            print('bei Erleichterung von '+str(-D)+': '+'\n'+Talentprobe(FW,E1,E2,E3,D))
        else:
            print('bei Erschwernis von '+str(D)+': '+'\n'+Talentprobe(FW,E1,E2,E3,D))
