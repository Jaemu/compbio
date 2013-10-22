def pretty_print(matrix, row):
    for i in range(row):
        print("{}".format(matrix[i]))

def indel(a):
	return 1

def match(a, b):
	if a == b:
		return 0
	return 1

def create_matrix(row,col):
	A = [0] * row
	for i in range(row):
		A[i] = [0] * col
	return A

def strincmp(a,b, matrix):
	for i in range(len(a)):
		for j in range(len(b)):
			if a[i] == b[j]:
				matrix[i][j] = 1

	for i in xrange(1, len(a)):
		for j in xrange(1, len(b)):
			cost = []
			cost.append(matrix[i-1][j-1] + match(a[i], b[j]))
			cost.append(matrix[i][j-1] + indel(b[j]))
			cost.append(matrix[i-1][j] + indel(a[i]))
			matrix[i][j] = cost[0]
			for k in xrange(1, 3):
				if cost[k] < matrix[i][j]:
					matrix[i][j] = cost[k]
	return matrix

if __name__ == '__main__':
	stringa = "hello there"
	stringb = "jelly rolls"
	matrix = create_matrix(len(stringa), len(stringa))
	matrix = strincmp(stringa, stringb, matrix)
	print(matrix[len(stringa) - 1][len(stringb)-1])