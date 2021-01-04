
def tempByZip(filename):
    result = {}
    f = open(filename, 'r')
    for line in f:
        tokens = line[:-1].split(',')
        for i in range(1, len(tokens)):
            tokens[i] = int(tokens[i])
        for i in range(1, len(tokens)):
            if tokens[i] not in result:
                result[tokens[i]] = []
            if tokens[0] not in result[tokens[i]]:
                result[tokens[i]].append(tokens[0])
    print(result)
    
def tempByZip2(filename):
    result = {}
    f = open(filename, 'r')
    for line in f:
        tokens = line[:-1].split(',')
        for i in range(1, len(tokens)):
            tokens[i] = int(tokens[i])
        zc = tokens[0]
        for temp in tokens[1:]: 
            if temp not in result:
                result[temp] = []
            if zc not in result[temp]:
                result[temp].append(zc)
    print(result)
    
tempByZip2('test.txt')