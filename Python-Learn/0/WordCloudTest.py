import wordcloud
txt="life is short,you need python"

w = wordcloud.wordcloud()
w.generate(txt)
w.to_file("Pywordcloud.png")