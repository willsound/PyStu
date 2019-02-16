import jieba
strVantone="万通地产是在上海证券交易所挂牌交易的A股上市公司，总股本为5.07亿股。万通地产具备一级开发资质，下设10家控股子公司和1家参股子公司，均为房地产开发公司。"
vantone=jieba.lcut(strVantone)
print(vantone)
vantoneAll=jieba.lcut(strVantone,cut_all=True)  #全模式
print(vantoneAll)
vantoneSearch=jieba.lcut_for_search(strVantone)  #搜索引擎模式
print(vantoneSearch)
def getText():
    txt=open("hamlet.txt","r").read()
    txt=txt.lower()
    return txt
hamletTxt=getText()
words=hamletTxt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))