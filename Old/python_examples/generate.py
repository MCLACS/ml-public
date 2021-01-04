import random

zips = ('01247', '11001', '02048', '01201', '08701', '01237')
lows = (-4, 45)
highs = (46, 72)
lines = 100
pairs = 5

def generate(filename):
    f = open(filename, 'w')
    for l in range(0, lines):
        index = random.randint(0, len(zips)-1)
        zc = zips[index]
        pairString = ''
        for p in range(0, pairs): 
            low = random.randint(lows[0],lows[1])  
            high = random.randint(highs[0],highs[1]) 
            pairString += str(low) + ', ' + str(high)
            if p < pairs-1:
                pairString += ', '
        f.write(zc + ', ' + pairString+'\n')
    f.close()
    
        
        
generate('test.txt')