l = [1, 2, 7, 3, 5, 7]
print(l)
l.append("список")
l.insert(1, [2])
a = [1, 2, 4, 5, 9]
l.append(a)
immutable_tuple = (4, 5, 6)
l.insert(4, immutable_tuple)
print(l)
l.pop(2)
print(l[-1])
l[0], l[1] = l[1], l[2]
print(l)
