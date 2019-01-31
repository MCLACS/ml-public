
def highest(filename):
    result = {}
    f = open(filename, 'r')
    for line in f:
        line = line[:-1]
        tokens = line.split(',')
        for i in range(1, len(tokens)):
            tokens[i] = int(tokens[i])
        result[tokens[0]] = max(tokens[1:])
    print(result)
        
highest('test.txt')