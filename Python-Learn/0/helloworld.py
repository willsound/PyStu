msg="hello world test  hxsun"
name="   sun huixiang  "
age=str(23)
bicycles=['trek','cannondale','redline',name]
fgx="-------------------"
print("中文")
print(name.upper())
print("\t"+name.upper())
print("\n"+name)
print(msg.upper()+name.rstrip())
print(name.lstrip())
print(name.rstrip())
print(name.strip())
print(0.2+0.1)
print(0.2**4)
print(age)
print("hello")
print(msg.lstrip())
print(bicycles)
print(bicycles[0])
print(bicycles[3].strip())
print(bicycles[2].title())
print(bicycles[-1])
print(fgx)
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
print(motorcycles[0],motorcycles[1])
motorcycles[0]='feige'
print(motorcycles[0].title())
print(motorcycles[-1])
motorcycles.append('fenghuang')
print(motorcycles[-1])
motorcycles.insert(0,'ofo')
print(motorcycles)
motorcycles.__delitem__(0)
print(motorcycles)
motorcycles.__delitem__(-1)
print(motorcycles)
print(motorcycles.pop())
print(fgx)
cars=['bmw','audi','toyota','subaru','吉利']
print(cars)
cars.reverse()
print('reverse()',cars)
cars.sort(reverse=True)
print('reverse=ture',cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
len(cars)
print(len(cars))
cars.pop(-1)
print(len(cars))
print('chapter 4'+fgx)
magicians=['alice','david','carolina']
magicians.insert(1,'hello')
magicians.sort()
magicians.append("sunhuixiang")
for magician in magicians:
    print(magician)

print("finished")
print(fgx)
for valuenum in range(-9,5):
    print(valuenum)
print(fgx)
numbers=list(range(-1,15,5))
print(numbers)
print(fgx)
squares=[]
for value in range(1,20):
    squares.append(value**2)
    print(value,'乘以',value,'等于',squares[-1])

print(min(squares),max(squares),sum(squares))

squares2=[value2**2 for value2 in range(1,11)]
print(squares2)
print(fgx)
players=['charles','martina','michael','florence','eli']
print(players[0:3])

my_foods=['pizza','falafel','carrot cake']

tom_foods=my_foods[0:2]
print(my_foods)
tom_foods.append('baozi')
print(tom_foods)

dimensions=(200,50)
print(dimensions[0],dimensions[1])

print(msg)