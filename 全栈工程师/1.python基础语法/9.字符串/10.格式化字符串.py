#研发者：时间遗忘
#开发时间：2023/6/14 20:10
'''为什么需要格式化字符串（按一定格式输出一个字符串）：保证有些东西固定不变，有些是可变的
格式化字符串的方式：
%作为占位符

%s--》字符串    %i或%d--》整数      %f--》浮点数

{}作为占位符


'''
#（%）占位符
name='张三'
age=20
print('我叫%s，今年%d岁' % (name,age))


# {}占位符/format方法
print('我叫{0}，今年{1}岁'.format(name,age))


# f-string
print(f'我叫{name}，今年{age}岁')     #3.0以上才能用的f


'''字符串的宽度'''
print('%10d' % 99)          #10表示的是整个行的宽度，文本放在宽度的最后面
print('%f' % 3.1415926)     #表示精度，保留小数，最后一位四舍五入
print('%.3f' % 3.1415926)   #.3表示保留小数点后三位，保留3位小数
#同时表示宽度和精度
print('%10.3f' % 3.1415926) #一共总宽度为10，小数点后3位
print('hellohello')


print('-'*70)

print('{0}'.format(3.1415926))  #少写百分号的情况下

print('{0:.3}'.format(3.1415926))   #.3表示的是一共是3位数

print('{0:.3f}'.format(3.1415926))  #3f表示的是3位小数，0表示的是占位符的顺序，0可以省略不写

print('{0:10.3f}'.format(3.1415926))  #同时设置宽度和精度，一共是10位，（.3）前面加上宽度