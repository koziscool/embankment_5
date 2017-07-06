
        
import time

def e10():
    primes = [2]
    primes_limit = 2 * 10 ** 6
    def primes_up_to( limit ):
        current_counter = primes[-1] + 1

        while primes[-1] < limit:
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
        primes.pop()

    primes_up_to( primes_limit )
    return sum(primes)

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 10 solution is:",  e10()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
