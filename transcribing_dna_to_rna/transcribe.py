import sys,time

def main():
    
    start = time.time()

    dna_string = open(sys.argv[1],"r").read()
    rna_string = ""

    for i in dna_string:
        if i.lower() != "t":
            rna_string+= i
        elif i.lower() == "t":
            rna_string+= "U"

    stop = (time.time() - start)*1000
    print(rna_string)
    print('Code ran in %f milliseconds' % stop)

if __name__ == "__main__":
    main()
