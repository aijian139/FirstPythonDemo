# 条件判断
# if else
age = 3
if age>18:
    print('你的年纪：',age)
    print('成年')
else:
    print('你的年纪：',age)
    print('未成年')

# if elif else
age = 17
if age>18:
  print('成年')
elif age>14:
  print('青年人')
else:
  print('少年')

# if elif elif else
# if语句从上往下判断 ，如果某个判断为true 就执行该判断，忽略剩下的elif else
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

# input() 读取用户的输入 input返回的数据类型是str
# str 不能直接和整数比较 必须把str转换为整数才能做比较
# int() 函数

s = input('birth:')
birth = int(s)
if birth>2000:
  print('00后')
else:
  print('00前')

  # 练习
  '''
  小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

    低于18.5：过轻
    18.5-25：正常
    25-28：过重
    28-32：肥胖
    高于32：严重肥胖
    用if-elif判断并打印结果：
  '''
  height = 1.75
  weight = 80.5

  bmi = weight / height
  if bmi>32:
    print('严重肥胖')
  elif bmi>28:
    print('肥胖')
  elif bmi>25:
    print('过重')
  elif bmi>18.5:
    print('正常')
  else:
    print('过轻')