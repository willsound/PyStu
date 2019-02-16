height,weight=eval(input("请输入身高和体重 :"))

def getBMI(bodyHeight,bodyWeight):   #计算BMI值
    return bodyWeight / pow(bodyHeight, 2)

def bmiTest(cvThin, cvNormal, cvFat, bmiNumber):   #计算肥胖度（通用）
    obDegreeStd = ["偏瘦", "正常", "偏胖", "肥胖"]
    obDegree=""
    if bmiNumber < cvThin:
        obDegree = obDegreeStd[0]
    elif cvThin <= bmiNumber < cvNormal:
        obDegree = obDegreeStd[1]
    elif  cvNormal <= bmiNumber< cvFat:
        obDegree = obDegreeStd[2]
    elif bmiNumber> cvFat:
        obDegree = obDegreeStd[3]
    else:
        obDegree="有病"
    return obDegree

def bmiTestCN(bmiNumber):#计算肥胖度（中国标准）
    bmiStdCN = [18.5, 23.9, 27.9]
    return bmiTest(bmiStdCN[0],bmiStdCN[1],bmiStdCN[2],bmiNumber)

def bmiTestIN(bmiNumber):#计算肥胖度（国际标准）
    bmiStdIN = [18.5, 24.9, 29.9]
    return bmiTest(bmiStdIN[0],bmiStdIN[1],bmiStdIN[2],bmiNumber)

def bmiTestAS(bmiNumber):#计算肥胖度（国际标准）
    bmiStdAS = [18.5, 22.9, 24.9]
    return bmiTest(bmiStdAS[0],bmiStdAS[1],bmiStdAS[2],bmiNumber)

bmiNumber=getBMI(height,weight)
bmiDegreeCN=bmiTestCN(bmiNumber)
bmiDegreeIN=bmiTestIN(bmiNumber)

print("您的BMI数值为：{:.2f},\n根据中国标准您的体型为：{}\n根据国际标准您的体型为：{}".format(bmiNumber,bmiDegreeCN,bmiDegreeIN))