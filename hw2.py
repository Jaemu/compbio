import fileinput

def concat(args):
    result = ''
    for arg in args:
        result = _concat(result, arg)
    return result

def _concat(a, b):
    la = len(a)
    lb = len(b)
    for i in range(la):
        j = i
        k = 0
        while j < la and k < lb and a[j] == b[k]:
            j += 1
            k += 1
        if j == la:
            n = k
            break
    else:
        n = 0
    return a + b[n:]

def _overlap(m, n):
    overlap = 0
    for i in xrange(len(m)):
        for j in xrange(len(n)):
            current_overlap = 0
            if(m[i] == n[j]):
                current_overlap = current_overlap + 1
                while((i + current_overlap) < len(m) - 1) and ((j + current_overlap) < len(n) - 1):
                    if(m[i + current_overlap] == n[j + current_overlap]):
                        current_overlap = current_overlap + 1
                    else:
                        break
                if(current_overlap > overlap):
                    overlap = current_overlap
    return overlap

if __name__ == '__main__':
    strings = []
    for line in fileinput.input():
        strings.append(str(line)[0:len(line) - 1])
    superstring = strings[0]
    while(len(strings) != 0):
        overlap = 0
        candidate = ""
        for i in xrange(1, len(strings)):
            temp = _overlap(superstring, strings[i])
            if (temp > overlap):
                candidate = strings[i]
                overlap = temp
        print("current: " + superstring + ", candidate: " + candidate + ".  Overlap = " + str(overlap))
        if(len(candidate) > 0):
            if(ord(candidate[0]) < ord(superstring[0])):
                superstring = concat(candidate, superstring)
            else:
                superstring = concat(superstring, candidate)
            print("super so far: " + superstring)
            strings.remove(candidate)
        else:
            strings.remove(strings[0])
    print(superstring)