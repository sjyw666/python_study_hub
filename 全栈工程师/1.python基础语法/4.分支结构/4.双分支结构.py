#研发者：时间遗忘
#开发时间：2022/9/21 16:05

#双分支结构：如果...不满足...就...
#二选一执行
'''语法结构：if 条件表达式：
              条件执行体1
           else：
                条件执行体2
'''
#从键盘录入一个整数，编写让计算机判断是奇数还是偶数
a=int(input('请输入一个整数：'))
if a%2==1:
    print(a,'这个数为奇数')
else:
    print(a,'这个数为偶数')

