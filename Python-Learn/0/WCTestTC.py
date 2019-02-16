import jieba
import wordcloud
import string
from scipy.misc import imread
excludes={"在座","然而"}
mask=imread("d:/tc/tc1.jpg")
f=open("d:/tc/tc.txt","r")
t=f.read()
for word in excludes:
    t.maketrans(word,"  ")
f.close()
ls=jieba.lcut(t,cut_all=False)

txt=" ".join(ls)
w=wordcloud.WordCloud( font_path="msyh.ttc",min_font_size=24,font_step=1,max_font_size=140,width=1000,height=700,background_color="white",max_words=100,collocations=False)
w.generate(txt)
w.to_file("d:/tc/tc.png")