# 分支结构之1：if-elif-else:
# 最常见的分支结构，if-else，通用的分支结构
# 注意：python中最重要的是流程控制的书写结构，这边没有花括号；

num = 2.4
if num > 3:
    print(f"num is {num}，greater than 3")
elif num > 2:
    print(f"num is {num}，greater than 2 but less than 3")
else:
    print("a normal num")

# 分支结构之swtich case，在python的早期版本中是没有switch语句的，在3.10之后有，但是写法并不是switch，而是match
# 在python里没有default值和break；
# default的值用_表示
match num:
    case 1:
        print("this num is one")
    case 2:
        print("this num is 2")
    case _:
        print("this is a number")