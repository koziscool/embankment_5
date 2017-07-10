
        
import time

def e15():
    factorial  = lambda n:  reduce(lambda x,y:x*y, [1]+range(1,n+1))
    combinations = lambda n, r: factorial(n) // factorial(r) // factorial(n - r)
    pascals_row = lambda n: map( lambda i: combinations(n, i), range(n+1) )

    end_range = 20
    end_row = pascals_row( end_range )

    return sum( i*i for i in end_row )

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 15 solution is:",  e15()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
