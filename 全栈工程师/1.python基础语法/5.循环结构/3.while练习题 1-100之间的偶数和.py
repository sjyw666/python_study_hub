#研发者：时间遗忘
#开发时间：2022/9/30 10:05

'''计算1-100之间的偶数和'''#偶数和为2550     奇数和为2500
#自己写的
sum=0
a=0
while a<101 and a%2!=1:
    sum+=a
    a+=2
print('和为：',sum)


#老师写的
sum=0
'''初始化变量'''
a=1                          #1开始所以初始化变量为1
'''条件判断'''
while a<=100:
    if a%2==0:
        sum+=a
    '''改变变量'''
    a+=1
print('1-100之间的偶数和：',sum)


sum=0
'''初始化变量'''
a=1
'''条件判断'''
while a<=100:
    if a%2:                  #原本a%2==0也可以，但是0的布尔值为false，修改后条件判断不运行
        sum+=a
    '''改变变量'''
    a+=1
print('1-100之间的奇数和：',sum)#所以最后结果为奇数和


sum=0
'''初始化变量'''
a=1
'''条件判断'''
while a<=100:
    if not bool(a%2):         #也可以是not bool()进行取反，条件判断有多种方法
        sum+=a
    '''改变变量'''
    a+=1
print('1-100之间的偶数和：',sum)
