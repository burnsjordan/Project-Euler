c = 0
for i in range(1,1000):
	for j in range(1, 100):
		if(j == len(str(i**j))):
			c += 1
			print(str(i**j))

print(c)
