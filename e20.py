        
import time

def e20():
    return sum( map( lambda c: int(c), str( reduce( lambda a, b: a*b, xrange(1, 101) ) )))

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 20 solution is:",  e20()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
