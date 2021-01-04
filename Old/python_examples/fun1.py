
def main():
    ch = ''
    l = []
    while ch != 'q':
        print("Enter a string:")
        ch = input()
        if ch != 'q':
            l.append(ch)
    print(l)
    
main()