def alpha_number(n):
	temp = []
	for j in str(n):
		temp.append(int(j))
	temp.sort()
	c = ""
	for j in temp:
		c += str(j)
	return c



cubes = []
a_cubes = {}
for i in range(100000):
	c = alpha_number(i**3)
	if(c in a_cubes):
		a_cubes[c] = a_cubes[c] + 1
	else:
		a_cubes[c] = 1
	cubes.append(i**3)

p_cubes = []

for i in a_cubes:
	if(a_cubes[i] == 5):
		p_cubes.append(i)
n_cubes = []

for i in cubes:
	if(alpha_number(i) in p_cubes):
		n_cubes.append(i)

n_cubes.sort()

print(n_cubes[0])
