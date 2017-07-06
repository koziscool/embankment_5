
        
import time

def e15():
    end_range = 100
    collatz_len = { 1:1, 2:2, 4:3 }

    def collatz_length( n ):
        if n in collatz_len:
            return collatz_len[n]
        else:
            answer = collatz_length( n//2 ) + 1 if n%2 == 0 else collatz_length( 3*n + 1 ) + 1
            collatz_len[n] = answer
            return answer

    for i in xrange(1, 10 ** 6):
        collatz_length(i)

    return  max(collatz_len, key=collatz_len.get)


if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 15 solution is:",  e15()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
