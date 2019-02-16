#GRIT

def dayUpWithWeekend(df,rdf):  #计算工作日力量，df为正增值，rdf为负增值
    dayup=1
    for i in range(365):
        if i%7 in [6,0]:
            dayup=dayup*(1-rdf)
        else:
            dayup=dayup*(1+df)
    return dayup

def dayUpNoWeekend(df):#计算连续努力力量

    return pow(1+df,365)

dayfactor=0.01 #初始定义正增值为0.01
rdayfactor=0.01 #初始定义负增值为0.01

while dayUpWithWeekend(dayfactor,rdayfactor)<dayUpNoWeekend(0.01):
    dayfactor+=0.01

print("工作日的努力参数是：{:.3f}".format(dayfactor))