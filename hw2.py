import fileinput, random, time

def concat(*args):
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
    result = {}
    prefix = ""
    suffix = ""
    overlap = 0
    for i in xrange(len(m)):
        for j in xrange(len(n)):
            current_overlap = 0
            if(m[i] == n[j]):
                current_overlap = current_overlap + 1
                while((i + current_overlap) < len(m)-1) and ((j + current_overlap) < len(n)-1):
                    if(m[i + current_overlap] == n[j + current_overlap]):
                        current_overlap = current_overlap + 1
                    else:
                        break
                if(current_overlap > overlap):
                    overlap = current_overlap
                    if(i < j):
                        prefix = n
                        suffix = m
                    else:
                        prefix = m
                        suffix = n
    result['overlap'] = overlap
    result['prefix'] = prefix
    result['suffix'] = suffix
    return result


def gen_strings(input):
    strings = []
    random.seed()
    size = random.randint(5, len(input) - 2)
    sample = random.randint(1, len(input) + 100)
    print("Fragment size: " + str(size) + ", " + str(sample) + " fragments")
    while sample > 0:
        temp_index = random.randint(0, len(input))
        if(temp_index + size) < len(input):
            strings.append(input[temp_index:temp_index + size])
            sample = sample - 1
    return strings



def duplicates(frags):
    unique = {}
    for frag in frags:
        keys = unique.keys()
        if(frag in keys):
            unique[str(frag)] = unique[str(frag)] + 1
        else:
            unique[str(frag)] = 1
    return unique

if __name__ == '__main__':
    for line in fileinput.input():
        start_time = time.time()
        random.seed()
        strings = gen_strings(line)
        result = duplicates(strings).keys()
        print("Unique fragments(" + str(len(result)) + "): " + str(result))
        while(len(result) > 1):
            stringm = ""
            stringn = ""
            overlap = 0
            for r in result:
                for s in result:
                    if(r != s):
                        temp = _overlap(r, s)
                        if(temp['overlap'] >= overlap):
                            overlap = temp['overlap']
                            stringm = temp['prefix']
                            stringn = temp['suffix']
            result.append(concat(stringm, stringn))
            if(len(stringm) > 0):
                result.remove(stringm)
            if(len(stringn) > 0):
                result.remove(stringn)
        print("Superstring:" + str(result) + ", Length: " + str(len(result[0])))
        print("Time to execute: " + str(time.time() - start_time) + ", Length of input: " + str(len(line)))