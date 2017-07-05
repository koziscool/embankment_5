
        
import time

def e4():
    largest_pal = 0
    def is_pal(n):
        return str(n) == str(n)[::-1]

    for i in xrange(100, 1000):
        for j in xrange(i, 1000):
            if is_pal( i*j ) and i*j > largest_pal:
                largest_pal = i*j
    return largest_pal

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 4 solution is:",  e4()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
