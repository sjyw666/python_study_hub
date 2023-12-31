#研发者：时间遗忘
#开发时间：2023/4/26 19:48
'''
zip() 接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个 tuple，然后返回由这些 tuple 组成的 list。

若传入参数的长度不等，则返回 list 的长度和参数中长度最短的对象相同。

利用 * 号操作符，可以将 list 解压。

Python3.0开始，zip()函数已经不返回 list 了，而是返回 iterable(可迭代对象)。这个可迭代对象需要特别注意，只能进行一次迭代遍历，第二次遍历就是空了。

'''
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9, 10, 11]

ab = zip(a, b)
print(list(ab))     # [(1, 4), (2, 5), (3, 6)]
# zip()之后的结果只能“使用一次”
# zip()实际上是一个生成器对象，故使用list()获取zip()结果时，已经相当于是完成一次迭代遍历
# 第二次再次使用list()时迭代已经结束，所以返回[]
print(list(ab))     # []

ac = zip(a, c)
# print(list(ac))     # [(1, 4), (2, 5), (3, 6)]，以短的为准

_ac = zip(*ac)      # 与 zip 相反，可理解为解压，返回二维矩阵式
print(list(_ac))    # [(1, 2, 3), (7, 8, 9)]，如果没把上面的 print(list(ac)) 注掉，这里的显示结果就是[]了


print('应用示例一')
name = ('jack', 'alex', 'sony', 'joey')
age = (25, 28, 21, 30)
for a, n in zip(name, age):
    print(a, n)

print('应用示例二：二维矩阵行列转换')
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(map(list, zip(*a))))  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]], map()函数把zip(*a)后的每一个元素转化为list
