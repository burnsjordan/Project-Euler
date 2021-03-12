import math


# Define the polygonal number formulas
def three(n):
	return int(n*(n+1)/2)

def four(n):
	return int(n*n)

def five(n):
	return int(n*(3*n-1)/2)

def six(n):
	return int(n*(2*n-1))

def seven(n):
	return int(n*(5*n-3)/2)

def eight(n):
	return int(n*(3*n-2))

# Check that the polygonal number formulas are working
if(three(1) == 1 and three(2) == 3 and three(3) == 6 and three(4) == 10 and three(5) == 15):
	print("3 works!")
else:
	print("3 failed ---------------")
if(four(1) == 1 and four(2) == 4 and four(3) == 9 and four(4) == 16 and four(5) == 25):
	print("4 works!")
else:
	print("4 failed ---------------")
if(five(1) == 1 and five(2) == 5 and five(3) == 12 and five(4) == 22 and five(5) == 35):
	print("5 works!")
else:
	print("5 failed ---------------")
if(six(1) == 1 and six(2) == 6 and six(3) == 15 and six(4) == 28 and six(5) == 45):
	print("6 works!")
else:
	print("6 failed ---------------")
if(seven(1) == 1 and seven(2) == 7 and seven(3) == 18 and seven(4) == 34 and seven(5) == 55):
	print("7 works!")
else:
	print("7 failed ---------------")
if(eight(1) == 1 and eight(2) == 8 and eight(3) == 21 and eight(4) == 40 and eight(5) == 65):
	print("8 works!")
else:
	print("8 failed ---------------")



# Create an array of these formulas
p_array = [three, four, five, six, seven, eight]


def has_all(c, n):
	hall = True
	h = []
	js = []
	ivs = []
	for i in range(n):
		n_polys = []
		j = 1
		v = p_array[i](j)
		has = False
		while(v < 10000):
			if(v > 999):
				n_polys.append(v)
			j += 1
			v = p_array[i](j)
		for k in c:
			if(k in n_polys):
				has = True
				h.append(k)
				js.append(j)
				ivs.append(i)

		if(not has):
			hall = False
	if(hall):
		print(h)
		print(js)
		print(ivs)
	return hall

def has_n(c, n):
	hall = True
	h = []
	for i in range(n):
		n_polys = []
		j = 1
		v = p_array[i](j)
		has = False
		while(v < 10000):
			if(v > 999):
				n_polys.append(v)
			j += 1
			v = p_array[i](j)
		for k in c:
			if(k in n_polys):
				has = True
				h.append(i)

	if(len(list(set(h))) >= n):
		return True
	else:
		return False

def narrow_cyclic_polys(cyclic_polys, z):
	no_good = []
	for a in range(len(cyclic_polys)**z):
		inds = []
		m = z - 1
		while(m >= 0):
			inds.append(math.floor(a / (len(cyclic_polys)**m)) % len(cyclic_polys))
			m -= 1
		
		cycle = []
		is_cycle = True
		o = len(inds)
		p = 0
		while(is_cycle and p < o):
			if(str(cyclic_polys[inds[(p % o)]])[0:2] == str(cyclic_polys[inds[(p - 1) % o]])[2:] and cyclic_polys[inds[(p % o)]] != cyclic_polys[inds[(p - 1) % o]]):
				cycle.append(cyclic_polys[inds[(p % o)]])
			else:
				is_cycle = False

			p += 1

		if(is_cycle):
#		if(is_cycle and has_n(cycle, z)):
			for y in cycle:
				no_good.append(y)
	return list(set(cyclic_polys) - set(no_good))

def get_cycles(cyclic_polys, z):
	cycles = []
	for a in range(len(cyclic_polys)**z):
		inds = []
		m = z - 1
		while(m >= 0):
			inds.append(math.floor(a / (len(cyclic_polys)**m)) % len(cyclic_polys))
			m -= 1
		
		cycle = []
		is_cycle = True
		o = len(inds)
		p = 0
		while(is_cycle and p < o):
			if(str(cyclic_polys[inds[(p % o)]])[0:2] == str(cyclic_polys[inds[(p - 1) % o]])[2:] and cyclic_polys[inds[(p % o)]] != cyclic_polys[inds[(p - 1) % o]]):
				cycle.append(cyclic_polys[inds[(p % o)]])
			else:
				is_cycle = False

			p += 1

		if(is_cycle):
			cycles.append(cycle)
	return cycles


def check_cyclic_4_digit(n):
	last_digits = []
	first_digits = []
	polys = []
	for i in range(n):
		j = 1
		v = p_array[i](j)
		while(v < 10000):
			if(v > 999):
				last_digits.append(str(v)[2:])
				first_digits.append(str(v)[0:2])
				polys.append(v)
			j += 1
			v = p_array[i](j)
	
	both_digits = []
	for f in first_digits:
		for l in last_digits:
			if(f == l):
				both_digits.append(f)	

	pre_cyclic_polys = []
	for p in polys:
		if(str(p)[2:] in both_digits and str(p)[0:2] in both_digits):
			pre_cyclic_polys.append(p)

	pcp_last = []
	pcp_first = []
	for pcp in pre_cyclic_polys:
		pcp_last.append(str(pcp)[2:])
		pcp_first.append(str(pcp)[0:2])

	pcp_both = []
	for f in pcp_first:
		for l in pcp_last:
			if(f == l):
				pcp_both.append(f)

	cyclic_polys = []
	for pcp in pre_cyclic_polys:
		if(str(pcp)[2:] in pcp_both and str(pcp)[0:2] in pcp_both):
			cyclic_polys.append(pcp)

	print(len(cyclic_polys))
	
	pair2 = []
	for a in cyclic_polys:
		for b in cyclic_polys:
			if(str(a)[2:] == str(b)[0:2]):
				pair2.append(str(a)+str(b))

	pair2 = list(set(pair2))
	print(len(pair2))

	pair4 = []
	for a in pair2:
		for b in pair2:
			if(str(a)[6:] == str(b)[0:2]):
				pair4.append(str(a)+str(b))

	pair4 = list(set(pair4))
	print(len(pair4))

	pair6 = []
	for a in pair4:
		for b in pair2:
			if(str(a)[14:] == str(b)[0:2] and str(b)[6:] == str(a)[0:2]):
				pair6.append(str(a)+str(b))


	pair6 = list(set(pair6))
	print(len(pair6))

	split6 = []
	for a in pair6:
		temp = [int(a[0:4]), int(a[4:8]), int(a[8:12]), int(a[12:16]), int(a[16:20]), int(a[20:])]
#		temp.sort()
#		if(temp not in split6):
		split6.append(temp)
	

	has6 = []
	for a in split6:
		if(has_all(a, 6) and sum(a) not in has6):
			has6.append(sum(a))
	for a in has6:
		print(a)


check_cyclic_4_digit(6)
