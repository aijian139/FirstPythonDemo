print('hello')
print('hello')

'''
name = input("请输入名字")
age = input("请输入年纪")
print("{},{}".format(name,age))
'''
#转义符 \
print('i"\"m ok')
print('i am ok')

print(3>2)
# 占位符的使用 %% 表示 一个百分号 {:.1f}保留一位小数 
print('整数的占位符%d' %(1))
print('{:.1f}'.format(3.14156))

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

#format() 函数
print("{name},{age}".format(name="yijian",age="22"))
print("{0},{1},{0}".format("yijian","22"))

