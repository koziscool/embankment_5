
import time
from collections import defaultdict

def e12():

    primes_limit = 10 ** 6

    def primes_up_to( limit ):
        primes = [2]
        current_counter = 3

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
        return primes


    def num_factors( num, primes ):
        factors_dic = defaultdict(int)
        primes_index = 0
        currentQuotient = num
        while currentQuotient > 1:
            p = primes[ primes_index ]
            while currentQuotient % p == 0:
                currentQuotient /= p
                factors_dic[p] +=1
            primes_index += 1

        ret_val = 1
        for v in factors_dic.values():
            ret_val *= v + 1
        return ret_val

    triangle = lambda n: n * (n+1) / 2

    primes =  primes_up_to(primes_limit)
    triangle_index = 1

    while num_factors( triangle( triangle_index ), primes ) <= 500:
        triangle_index += 1

    return triangle(triangle_index)

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 12 solution is:",  e12()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
