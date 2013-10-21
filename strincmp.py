def indel(a):
	return 1

def match(a, b):
	if a == b:
		return 0
	return 1

def strincmp(a,b, x, y):
	lowest_cost = 0
	cost = []
	space = ' '
	if x == 0:
		return y
	if y == 0:
		return x
	cost.append(strincmp(a,b,x-1, y-1) + match(a[x], b[y]))
	cost.append(strincmp(a, b, x, y-1) + 1)
	cost.append(strincmp(a, b, x-1, y) + 1)
	lowest_cost = cost[0]
	for k in xrange(1, 3):
		if cost[k] < lowest_cost:
			lowest_cost = cost[k]
	return lowest_cost

if __name__ == '__main__':
	stringa = "hello"
	stringb = "jelly"
	print(str(len(stringa)))
	print(str(strincmp(stringa, stringb, len(stringa) - 1, len(stringb) - 1)))
