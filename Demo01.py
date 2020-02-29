# list 列表 有序的集合 可以动态的添加和删除其中的元素
classmates = ['Michael','Bob','Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
# 获取最后一个元素
print(classmates[-1])
# 获取倒数第二个元素
print(classmates[-2])
# list 往最后添加元素 通过append()方法 len()方法获取列表的大小
classmates.append("tom")
size = len(classmates)
print(size)
print(classmates[-1])

# 可以替换列表的某个元素
classmates[1] = 'yijian'
print("----------------",classmates)

# list 中可以存放不同的数据类型
classmates.append(1)
# 删除一个元素
classmates.remove('yijian')
print(classmates)
# list 中也可以嵌套使用list
s = ['python','java',['asp','php'],'html']
print(s)
print(s[2][0])

# tuple 一种有序列表 ：元组 一旦初始化 就不能修改 
t = ('xh','xq','zs')
print(t)

# 如果要定义一个空的tuple
p = ()
print(p)

# 当只有一个元素的时候 则必须定义为（，）如果写成（1）则会被解释为数学公式的小括号
o = (1,)
print(o)

# 这里t2[2][0] t2[2][1] 指向的是一个list list是可以变的，但是原本的a b 不可变
t2 = ('a','b',['A','B'])
t2[2][0] = 'X'
t2[2][1] = 'Y'
print(t2)

# 练习 
# 请用索引取出下面list的指定元素
L = [
  ['apple','google','microsoft'],
  ['java','python','Ruby','php'],
  ['Admin','Bart','lisa']

]
# 打印Apple
print(L[0][0])

#打印python
print(L[1][1])

#打印 lisa
print(L[2][2])