
        
import time

def e7():
    primes = [2]
    num_primes = 10001
    def make_n_primes( n ):
        current_counter = primes[-1] + 1

        while len(primes) < n:
            is_prime = True
            for p in primes:
                if p*p > current_counter:
                    break
                if current_counter % p == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append( current_counter )
            current_counter += 1

    make_n_primes( num_primes )
    return primes[-1]

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 7 solution is:",  e7()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
