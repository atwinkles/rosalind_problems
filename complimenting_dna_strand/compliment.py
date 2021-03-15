import sys, time

def main():
    
    start = time.time()

    dna_string = open(sys.argv[1],"r").read()[::-1].strip()
    dna_dict = {"A":"T","C":"G","G":"C","T":"A"}
    compliment = ""
    for i in dna_string:
        compliment+= dna_dict[i]

    stop = (time.time() - start)*1000

    print(compliment)
    print('Code ran in %f milliseconds' % stop)

if __name__ == "__main__":
    main()
