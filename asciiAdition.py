import re

p = 'MATH'
x = 'fgiq'
list1 = [*p]
list2 = [*x]
ascii1=[ord(x) for x in list1 ]
ascii2=[ord(x) for x in list2 ]
sum = []
for i in range(len(ascii1)-1):
    sum.append(ascii1[i] +ascii2[i])
    res = (re.sub('.', lambda x: r'% 4X' % ord(x.group()), str(sum[i])))
    print(res)




print(list1)
print(ascii1)
print(list2)
print(ascii2)
print(sum)
# for i , j in p:
#     print(j)