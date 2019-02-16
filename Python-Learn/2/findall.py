html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

#可以根据标签名，属性，内容查找文档
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all('ul'))
print(type(soup.find_all('ul')[0]))

for ul in soup.find_all('ul'):
    print(ul.find_all('li'))

#attrs 可以传入字典的方式来查找标签，但是这里有个特殊的就是class,因为class在python中是特殊的字段，
# 所以如果想要查找class相关的可以更改attrs={'class_':'element'}或者soup.find_all('',{"class":"element})，
# 特殊的标签属性可以不写attrs，例如id
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))

#text 返回的是查到的所有的text='Foo'的文本
print(soup.find_all(text='Foo'))


#通过select()直接传入CSS选择器就可以完成选择
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))

#通过get_text()就可以获取文本内容

for li in soup.select('li'):
    print(li.get_text())


#可以通过[属性名]或者attrs[属性名]获取属性

for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])