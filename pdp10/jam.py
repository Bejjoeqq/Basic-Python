maxDetik=86400
Jam={
    "jam":0,
    "menit":0,
    "detik":0
}
def ResetJam(J):
    global Jam
    Jam["jam"]=0
    Jam["menit"]=0
    Jam["detik"]=0
def IsJValid(H,M,S):
    if H<24 and M<60 and S<60:
        return True
    else:
        return False
def MakeJam(HH,MM,SS):
    Jam={}
    if IsJValid(HH,MM,SS)==True:
        Jam["jam"]=HH
        Jam["menit"]=MM
        Jam["detik"]=SS
        return Jam
    else:
        print("Invalid Jam")
def MakeJamTest(HH,MM,SS):
    j=MakeJam(HH,MM,SS)
    TulisJam(j)
def GetHour(J):
    return J["jam"]
def GetMinute(J):
    return J["menit"]
def GetSecond(J):
    return J["detik"]
def SetHH(J,newHH):
    global Jam
    Jam["jam"]=newHH
    Jam["menit"]=J["menit"]
    Jam["detik"]=J["detik"]
    return newHH
def SetMM(J,newMM):
    global Jam
    Jam["jam"]=J["jam"]
    Jam["menit"]=newMM
    Jam["detik"]=J["detik"]
    return newMM
def SetSS(J,newSS):
    global Jam
    Jam["jam"]=J["jam"]
    Jam["menit"]=J["menit"]
    Jam["detik"]=newSS
    return newSS
def BacaJam(J):
    h,m,s=map(int, input("Baca Jam : ").split(":"))
    MakeJam(h,m,s)
def TulisJam(J):
    if IsJValid(J["jam"], J["menit"], J["detik"])==True:
        print("{}:{}:{}".format(J["jam"], J["menit"], J["detik"]))
    else:
        print("Invalid Jam")
def Jam2Detik(J):
    return (J["jam"]*3600)+(J["menit"]*60)+J["detik"]
def Detik2Jam(N):
    global Jam
    jam=N//3600
    sisa=N%3600
    menit=sisa//60
    sisa=sisa%60
    Jam["jam"]=jam
    Jam["menit"]=menit
    Jam["detik"]=sisa
    return Jam
def JEQ(J1,J2):
    return Jam2Detik(J1)==Jam2Detik(J2)
def JNEQ(J1,J2):
    return Jam2Detik(J1)!=Jam2Detik(J2)
def JLT(J1,J2):
    return Jam2Detik(J1)<Jam2Detik(J2)
def JGT(J1,J2):
    return Jam2Detik(J1)>Jam2Detik(J2)
def JPlus(J1,J2):
    global Jam
    dtsm=J1["detik"]+J2["detik"]
    mtsm=J1["menit"]+J2["menit"]
    jmsm=J1["jam"]+J2["jam"]
    if dtsm>59:
        Jam["detik"]=dtsm-60
        mtsm+=1
    else:
        Jam["detik"]=dtsm
    if mtsm>59:
        Jam["menit"]=mtsm-60
        jmsm+=1
    else:
        Jam["menit"]=mtsm
    if jmsm>23:
        Jam["jam"]=jmsm-24
        print("+1 hari ",end="")
    else:
        Jam["jam"]=jmsm
def JMinus(J1,J2):
    global Jam
    Jam["jam"]=J1["jam"]-J2["jam"]
    Jam["menit"]=J1["menit"]-J2["menit"]
    Jam["detik"]=J1["detik"]-J2["detik"]
def NextDetik(J):
    global Jam
    dtsm=J["detik"]+1
    mtsm=J["menit"]
    jmsm=J["jam"]
    if dtsm>59:
        Jam["detik"]=dtsm-60
        mtsm+=1
    else:
        Jam["detik"]=dtsm
    if mtsm>59:
        Jam["menit"]=mtsm-60
        jmsm+=1
    else:
        Jam["menit"]=mtsm
    if jmsm>23:
        Jam["jam"]=jmsm-24
        print("+1 hari ",end="")
    else:
        Jam["jam"]=jmsm
    return Jam
def NextNDetik(J,N):
    global Jam
    dtsm=J["detik"]+N
    mtsm=J["menit"]
    jmsm=J["jam"]
    if dtsm>59:
        Jam["detik"]=dtsm-60
        mtsm+=1
    else:
        Jam["detik"]=dtsm
    if mtsm>59:
        Jam["menit"]=mtsm-60
        jmsm+=1
    else:
        Jam["menit"]=mtsm
    if jmsm>23:
        Jam["jam"]=jmsm-24
        print("+1 hari ",end="")
    else:
        Jam["jam"]=jmsm
    return Jam
def PrevDetik(J):
    global Jam
    dtsm=J["detik"]-1
    mtsm=J["menit"]
    jmsm=J["jam"]
    if dtsm<0:
        Jam["detik"]=dtsm+60
        mtsm-=1
    else:
        Jam["detik"]=dtsm
    if mtsm<0:
        Jam["menit"]=mtsm+60
        jmsm-=1
    else:
        Jam["menit"]=mtsm
    if jmsm<0:
        Jam["jam"]=jmsm+24
        print("-1 hari ",end="")
    else:
        Jam["jam"]=jmsm
    return Jam
def PrevNDetik(J,N):
    global Jam
    dtsm=J["detik"]-N
    mtsm=J["menit"]
    jmsm=J["jam"]
    if dtsm<0:
        Jam["detik"]=dtsm+60
        mtsm-=1
    else:
        Jam["detik"]=dtsm
    if mtsm<0:
        Jam["menit"]=mtsm+60
        jmsm-=1
    else:
        Jam["menit"]=mtsm
    if jmsm<0:
        Jam["jam"]=jmsm+24
        print("-1 hari ",end="")
    else:
        Jam["jam"]=jmsm
    return Jam
def Durasi(Jaw,Jakh):
    if Jam2Detik(Jakh)<Jam2Detik(Jaw):
        return None
    else:
        return Jam2Detik(Jakh)-Jam2Detik(Jaw)

