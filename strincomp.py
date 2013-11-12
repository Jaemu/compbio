def pretty_print(matrix, row):
    for i in range(row):
        print("{}".format(matrix[i]))

def indel(a):
	return 1

def match(a, b):
	if a == b:
		return 0
	return 2

def create_matrix(row,col):
	A = [0] * row
	for i in range(row):
		A[i] = [0] * col
	return A

def strincmp(a,b, matrix):
	result = ''
	parent = []
	for i in xrange(1, len(a)):
		for j in xrange(1, len(b)):
			cost = []
			cost.append(matrix[i-1][j-1] + match(a[i], b[j]))
			cost.append(matrix[i][j-1] + match(a[i], b[j - 1]))
			cost.append(matrix[i-1][j] + match(a[i - 1], b[j]))
			matrix[i][j] = cost[0]
			parent.append(0)
			for k in xrange(1, 3):
				if cost[k] < matrix[i][j]:
					matrix[i][j] = cost[k]
					parent.pop()
					parent.append(k)
	pretty_print(matrix, len(stringa))
	#posx = 1
	#posy = 1
	#result = result + a[0]
	#result = result + b[0]
	#for i in xrange(len(parent)):
	#	if(posy < len(a)) or (posx < len(b)):
	#		if(parent[i] == 0):
	#			result = result + a[posy]
	#			posx = posx + 1
	#			posy = posy + 1
	#		if parent[i] == 1:
	#			result = result + a[posy]
	#			posy = posy + 1
	#		if parent[i] == 2:
	#			result = result + b[posx]
	#			posx = posx + 1
	#print(result)
	return matrix

if __name__ == '__main__':
	stringa = "goodbye"
	stringb = "hello"
	matrix = create_matrix(len(stringa), len(stringb))
	matrix = strincmp(stringa, stringb, matrix)
	print(matrix[len(stringa) - 1][len(stringb)-1])