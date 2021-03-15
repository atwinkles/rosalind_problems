import sys,time

def main():

    start = time.time()

    dna_string = open(sys.argv[1],"r").read()
    a = 0
    c = 0
    g = 0
    t = 0

    for i in dna_string:
        if i.lower() == "a":
            a += 1
        elif i.lower() == "c":
            c += 1
        elif i.lower() == "g":
            g += 1
        elif i.lower() == "t":
            t += 1

    stop = (time.time() - start)*1000

    print(('%d %d %d %d' % (a,c,g,t)))
    print('Code ran in %f milliseconds' % stop)

if __name__ == "__main__":
    main()
