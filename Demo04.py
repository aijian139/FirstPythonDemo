# dict 字典
# 类似于map 使用键-值（key-value）存储
d = {
  'tom':95,
  'bob':75,
  'marry':85,
  }
print("tom的成绩为：",d['tom'])

# 除了初始化指定外，还可以通过key放入
d['tom'] = 88
print('tom修改后的成绩为：',d['tom']
)

# 避免key不存在的错误
# 1.通过 in 判断 key 是否存在
f = 'jack' in d
print(f)

# 通过字典dict 提供的get()方法，如果key不存在返回None，或者返回指定的value
f = d.get('jack','no value')
print(f)
# 注意：返回None的时候Python的交互环境不显示结果。

# 删除一个 key ，用pop(key)方法 ，对应的value也会在dict中删除
d.pop('tom')
for name in d:
 print(name ,' : ',d[name])

 # !!! 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
 '''
 和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。
 '''


 # set 集合
 # 也是一组key 的集合 但不存储value。切key不能重复
 # 要创建一个set 需要提供一个list 作为输入集合
 s = set([1,2,3])
 print(s)
'''
注意，传入的参数[1, 2, 3]是一个list，
而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，
显示的顺序也不表示set是有序的。。重复元素在set 中会被自动过滤
'''
# add(key) 方法添加元素到set中，可以重复添加 但不会有效果
s.add(4)
s.add(5)
print('添加数据后的集合：',s)

# remove(key) 删除元素
s.remove(1)
print('删除数据后的集合：',s)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
# 交集
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1&s2)
# 并集
print(s1|s2)

'''
可变对象： 内部的内容是会变化的
不可变对象：调用对象自身的任意方法，都不会改变该对象自身的内容。
这些方法会创建新的对象并返回，这样就保证了不可变对象本身永远是不可变的。
'''