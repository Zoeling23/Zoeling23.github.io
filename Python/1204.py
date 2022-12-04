print("hello")

salary=877
workhour=6
savemoney=12888

InputMoney=salary*workhour*15 #15天領一次錢
HalfMonth=InputMoney-savemoney #半個月剩下可以花的錢
print(salary*workhour) #一天的薪水
print(HalfMonth*24) #一年可以花的錢

"""
多行註解
"""

print(4/4) #1.0,除法都會變成浮點數
print(id(salary)) #出現記憶體存的位置

#指派運算子
a=2;b=4
c=a+b
print(c) #6

a+=b
print(a) #6

a-=b
print(a) #2

d=1
d*=c
print(d) #6

ve=10
ve%=3
print(ve)

f=12
f/=c
print(f)

f**=a
print(f)

print(100//15) #取地板(除完最靠近的整數)

import math
print(math.ceil(100/15)) #天花板
print(math.floor(100/15)) #地板
