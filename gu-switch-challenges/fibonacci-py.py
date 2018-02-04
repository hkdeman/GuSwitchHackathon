l = [1,1]

for e in l:
	print(e)
for i in range(2,100):
	l.append(l[i-1]+l[i-2])
	print(l[i])
