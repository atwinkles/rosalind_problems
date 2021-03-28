import sys, time

def main():
    start = time.time()
    rabbit_params = open(sys.argv[1],"r").read().split(" ")
    n = int(rabbit_params[0])
    k = int(rabbit_params[1])
    
    def rab_fib(n,k):
        if n <= 1: 
            return n 
        return rab_fib(n-1,k) + k*rab_fib(n-2,k) 
    

    stop = (time.time() - start)*1000

    print(rab_fib(n,k))
    print('Code ran in %f milliseconds' % stop)
    

if __name__ == "__main__":
    main()
