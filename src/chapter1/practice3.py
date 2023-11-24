odd = [1,3,5,7,9]
a = list()
print(odd)
print(odd[1])
print(odd[0] + odd[1])
print(odd[-1])
print([1,2,3,['a','b','c']][-1][0])
print(odd[0:2])
print([1,2,3] + [4,5,6])
print([1,2,3] * 3)
print(len([1, 2, 3]))
print(str([1,2,3][2]) + ' year')
list1 = [1,2,3]
list1[0] = 6
print(list1)
del list1[0]
print(list1)
list2 = [3,2,6,1,2]
del list2[2:]
print(list2)
list2.append(4)
print(list2)
list2.sort()
print(list2)
list2.reverse()
print(list2)
print(list2.index(4))
list2.insert(0,11)
list2.insert(2,11)
list2.insert(4,11)
print(list2)
list2.remove(11)
print(list2)
list2.pop()
print(list2)
print(list2.count(11))
list2.extend([15,16,17])
print(list2)
list3 = [1,2,3]
list3 += [6,7]
print(list3)
