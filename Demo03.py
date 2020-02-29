# 循环
# for in 循环
names = ['tom','rose','jack']
for name in names:
  print(name)

# 计算1-10 的整数之和
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
   sum+=x
# 注意代码的缩进的不同效果也不一样
   print(sum)
print(sum)

# rang()函数 生成一个整数序列
# list()函数 可以转换为list
a = list(range(5))
print(a)

# 生成0-100的整数序列 然后相加
sum = 0
for x in range(100):
  sum += x
print("0-100相加得到的结果为：",sum)

# while 循环
# 只要满足条件就不断循环，条件不满足时就退出循环


# 计算100以内所有奇数的和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

sum = 0
n = 1
while n<100:
  sum+=n
  n+=2
print(sum)

# 练习 
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ["Bart","Lisa","Adam"]
for name in L:
  print("hello,",name,"!")