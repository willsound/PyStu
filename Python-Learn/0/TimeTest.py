import time

barLength=6
scale=50
barSleepTime=0.1
print("执行开始".center(scale,"-"))
for i in range(scale+1):  #V1
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    print("{:^3.0f}%[{}-->{}]".format(c,a,b))
    time.sleep(barSleepTime)
print("执行结束".center(scale,"-"))


#scale=50
print("执行开始".center(scale//2,"-"))
start=time.perf_counter()
for i in range(scale+1):  #V2
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))
for i in range(101):
    print("\r{:3}%".format(i),end="")  #\r使光标退回到行首
    time.sleep(barSleepTime)