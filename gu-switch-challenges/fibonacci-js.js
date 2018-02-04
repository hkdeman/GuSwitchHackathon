var l = [1,1];
print(l[0]);
print(l[1]);

var i;
for(i=2;i<100;i++) {
	l.push(l[i-1]+l[i-2])
	print(l[i])
}
