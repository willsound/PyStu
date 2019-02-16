alt_color='color'
alt_points='points'
alt_x_position='x_position'
alt_y_position='y_position'
alt_speed='speed'
speed_items=['low','middle','fast']
color_items=['red','yellow','blue','black']

alien_1={alt_x_position:0,alt_y_position:25}  #定义字典，键值对应
alien_1[alt_color]=color_items[-1] #对特定键赋值
alien_1[alt_points]=5
alien_1[alt_speed]=speed_items[-1]

print('The '+alien_1[alt_color]+' Saucer man position is ('+ str(alien_1[alt_x_position])+','+str(alien_1[alt_y_position])+')')

if alien_1[alt_speed]==speed_items[0]:
    x_increment = 1
elif alien_1[alt_speed]==speed_items[1]:#别忘了条件判断后的冒号
    x_increment = 3
else :
    x_increment = 5

alien_1[alt_x_position]=alien_1[alt_x_position]+x_increment
print('The '+alien_1[alt_color]+' Saucer man NEW position is ('+ str(alien_1[alt_x_position])+','+str(alien_1[alt_y_position])+')')
print(alien_1)
del alien_1[alt_x_position]
print(alien_1)
alien_1.pop(alt_y_position)
print(alien_1)