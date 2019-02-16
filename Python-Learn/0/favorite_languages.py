#定义字典
favorite_languages={
    'jen':'Python',
    'sarah':'C',
    'edward':'ruby',
    'phil':'python',
}
#安Key值检索Value值
print(favorite_languages['phil'])

user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
#遍历字典
for key,value in user_0.items():
    print('\nkey:'+key)
    print('value:'+value)

for c_name,c_language in favorite_languages.items():#提取整体记录
    print(c_name.title()+"'s favorite lanaguage is " +
          c_language.title())

for a_name in favorite_languages.keys(): #只提取键
    print(a_name)

for a_language in favorite_languages.values():#提取值
    print(a_language)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
names=favorite_languages.keys()
print(names)