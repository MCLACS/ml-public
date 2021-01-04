def readFile(filename):
    l = []
    file = open(filename, 'r')
    for line in file:
        if '\n' in line:
            line = line[:-1]
        tokens = line.split(',')
        print(tokens)
        l.append(tokens)
    return l
    

l = readFile('data.txt')
print(l)