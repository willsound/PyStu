#字符串有正向递增序号（从0开始）和返向从（-1开始)递减序号两种表达方式。
#字符串切片操作<字符串>[M:N],M缺失表示至开头，N缺失表示至结尾。[M:N:K]K为步长；[::-1]将字符串反向
#字符串操作：X+Y,连接两个字符串；n*X或X*n,复制n次字符串X；X in S,如果X是S的子串，返回True
#字符串处理函数：len(x);str(),转换成字符串；eval()从字符串转换成其他数据类型；ord()返回对应字符的编码值，chr()返回对应编码的字符
#字符串常用方法：lower(),upper();split(sep=None),返回一个列表，根据sep被分割的部分组成；count(sub),返回子串sub出现的次数；replace(old,new),字符替换；
#字符串常用方法：center(width[,fillchar]),根据宽度句中；strip(chars),去掉左右侧chars中列出的字符；join(iter),在iter变量除最后元素外每个元素后增加一个",",主要用于字符串分割
#字符串格式化：.format(),{}为槽，:<填充><对齐>（<>^）<宽度><,千分位><.精度>
#转意符\b,回退；\n换行；\r回车

sunhx="孙会想山东省德州市宁津县张大庄前村"
print(sunhx[:3])
print(sunhx[3:6:2])
print(sunhx[-1:-17:-1])
print(len(sunhx))
print(sunhx[0],ord(sunhx[0]))
print("{0:=^30}".format("会想"))
print("{0:*>20}".format("孙"))
print("{:10}".format("德州"))
print("{0} 的编码是 {1}".format(sunhx[0],ord(sunhx[0])))
print("{0:,.2f}".format(123456.6789))
print("{0:e},{0:E},{0:f},{0:%}".format(3.14))

print(sunhx.split(sep="会"))
print(sunhx.count("县"))
print(sunhx.replace("张大庄","张大庄镇"))
print(sunhx[0].center(20,"*"))


def charPyramid(chars,charsNum):
    for i in range(charsNum):
        tierChar="{0:^"+str(charsNum)+"}"
        if i%2 not in [0]:
            print(tierChar.format(chars*i))
def charPyramidA(Pychars,PyWidth):
    for i in range(PyWidth):
        if i % 2  in [0]:
            print(str(Pychars).center(i,"*"))

#charPyramid("A",8)
#charPyramidA("A",8)


import time
t=time.gmtime()
print(time.time(),time.ctime(),time.gmtime())

print(time.strftime("%Y-%m-%d %H:%M:%S",t))
print(time.strftime("%Y-%B-%d %A %H:%M:%S",t))

import math
print(dir(math))

print(math.pi)
print(math.e)