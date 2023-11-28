a = 1
b = "python"
c = [1,2,3]
print(id(b))
aa = a
print(a is aa)
cc = [1,2,3]
print(c is cc)
ccc = c[:]

from copy import copy
bb = copy(b)
print(bb)

s,d = ('python', 'life')
print(s,d)
s1,d1 = 'python', 'life'
print(s1,d1)
a1 = 3
b1 = 6
a1, b1 = b1, a1
print(a1)
print(b1)

