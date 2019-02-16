cars=['audi','bmw','subaru','toyota']
for car in cars:   #循环的for in 结构
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

answer=17
if answer!=42:
    print(str(answer)+'That is not the correct answer,and changed it')
    answer=42
print("the answer is right")

requested_toppings=['mushrooms','onions','pineapple'] #中括号为列表，大括号为字典
if 'mushrooms'in requested_toppings:
    print("True")
else:
    print("False")

banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
    print(user.title()+",you can post a respinse if you wish.")

print("-----------------------------------------------------")
age=23
if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
elif age>=65:
    price=5

print(str(price))

alt_color='color'
alt_points='points'
alt_x_position='x_position'
alt_y_position='y_position'

color_items=['green','red','blue','yellow']
for color_item in color_items:
    print(color_item)

alien_0={alt_color:color_items[-1],alt_points:5}
print(alien_0)
alien_0[alt_x_position]=0
alien_0[alt_y_position]=25
print((alien_0))
print(alien_0[alt_color])
print(alien_0[alt_points])
alien_0[alt_color]=color_items[1]
alien_0[alt_y_position]=50
print(alien_0)

