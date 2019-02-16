import jieba
import wordcloud
import string
from scipy.misc import imread
excludes={"所以","一下","就是","一般","而且","不能","还是","因为","其实","直接","认为","可能","然而"}
mask=imread("d:/tc/sd.jpg")
f=open("d:/tc/ms.txt","r")
t=f.read()
for word in excludes:
    t.maketrans(word,"  ")
f.close()
ls=jieba.lcut(t,cut_all=False)

txt=" ".join(ls)
w=wordcloud.WordCloud( font_path="msyh.ttc",min_font_size=4,font_step=1,max_font_size=72,mask=mask,width=1000,height=700,background_color="white",max_words=50,collocations=False)
w.generate(txt)
w.to_file("d:/tc/sdms.png")