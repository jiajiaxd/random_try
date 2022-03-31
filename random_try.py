import random
import os
def cont():
    k=0
    x=float(input("输入一个概率（百分比）："))
    s=int(input("输入尝试几次："))
    for i in range (1,s+1):
        if(i%1000==0):
            print("已经进行到",i,"/",s,"次运算。")
        if(random.random()*100<x):
            k+=1
    print("在",s,"次随机数生成中，对于你的人品来计算的概率为：",round(k/s*100,2),"%")
    os.system('pause')
    cont()
cont()