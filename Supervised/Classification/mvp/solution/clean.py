i = {
    'name': 0, 
    'pa' : 5,
    'hr' : 11,
    'rbi' : 12,
    'ba' : 17,
    'obp' : 18,
    'slg' : 19,
    'mvp' : 29}


def cleanName(name):
    ret = name.split('\\')[0]
    if ret.endswith('*') or ret.endswith('#'):
        ret = ret[:-1]
    return ret

def main():
    inFile = open('data.csv', 'r')
    outFileX = open('mvp_X.csv', 'w')
    outFileY = open('mvp_y.csv', 'w')
    outFileNames = open('names.csv', 'w')
        
    firstLine = True
    for line in inFile:
        if not firstLine:
            tokens = line.split(',')
            ba = tokens[i['ba']].strip()
            obp = tokens[i['obp']].strip()
            slg = tokens[i['slg']].strip()
            if ba != '' or obp != '' or slg != '':
                name = cleanName(tokens[i['name']].strip())
                pa = tokens[i['pa']].strip()
                hr = tokens[i['hr']].strip()
                rbi = tokens[i['rbi']].strip()
                mvp = tokens[i['mvp']].strip()
                
                outFileX.write('{},{},{},{},{},{}\n'.format(pa, hr, rbi, ba, obp, slg))
                outFileY.write('{}\n'.format(mvp))
                outFileNames.write('{}\n'.format(name))
        firstLine = False
        
    outFileX.close()
    outFileY.close()
    outFileNames.close()
            
main()