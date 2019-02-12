def loadX():
    mvp_X = []
    fileX = open('mvp_X.csv', 'r')
    for line in fileX:
        tokens = line.strip().split(',')
        l = []
        l.append(int(tokens[0]))
        l.append(int(tokens[1]))
        l.append(int(tokens[2]))
        l.append(float(tokens[3]))
        l.append(float(tokens[4]))
        l.append(float(tokens[5]))
        mvp_X.append(l)
    return mvp_X

def loadY():    
    mvp_y = []
    fileY = open('mvp_y.csv', 'r')
    for line in fileY:
        tokens = line.strip().split(',')
        for t in tokens:
            mvp_y.append(int(t))
    return mvp_y