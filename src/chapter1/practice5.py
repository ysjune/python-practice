dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
dic['age'] = 14
print(dic)
del dic['age']
print(dic)
print(dic["name"])
print(dic.keys())
for k in dic.keys():
    print(k)

print(list(dic.keys()))
print(dic.values())
print(dic.items())
tempDic = {'name':'p', 'phone':"111"}
print(tempDic)
tempDic.clear()
print(tempDic)
print(dic.get("name"))
print(dic.get("alias"))
print(dic.get("name", "원숭이"))
print(dic.get("alias", "원숭이"))
print('name' in dic)
print('alias' in dic)