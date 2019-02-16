import itchat
itchat.login()
itchat.auto_login()
friends=itchat.get_friends(update=True)[0:]


male=female=other=0

for i in friends[1:]:
    sex=i["Sex"]
    if sex==1:
        male+=1
    elif sex==2:
        female+=1
    else:
        other+=1

total=len(friends[1:])
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable
#调用函数得到各变量，并把数据存到csv文件中，保存到桌面
NickName = get_var("NickName")
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')
from pandas import DataFrame
data = {'NickName': NickName, 'Sex': Sex, 'Province': Province,
        'City': City, 'Signature': Signature}
frame = DataFrame(data)
frame.to_csv('data.csv', index=True)

print(male)
print(female)
print(other)
print("天涯人男性好友比例：%.2f%%"%(float(male)/total*100))
print("天涯人女性好友比例：%.2f%%"%(float(female)/total*100))
print("天涯人不明性别比例：%.2f%%"%(float(other)/total*100))


