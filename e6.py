
        
import time

def e6():
    my_range = xrange(1, 101)
    square_sum = sum( my_range ) ** 2
    sum_square = sum(map( lambda n: n*n, my_range )) 
    return square_sum - sum_square

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 6 solution is:",  e6()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
