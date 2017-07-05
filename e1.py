

        
import time

def e1():
    end_range, total = 1000, 0
    for i in xrange(1, end_range ):
        if i % 3 == 0 or i % 5 ==0:
            total += i
    return total

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 1 solution is:",  e1()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
