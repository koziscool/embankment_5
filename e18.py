        
import time

def e18():

    triangle_string = '''75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

    lines = triangle_string.split('\n')

    numbers, best_path = [], []
    for s in lines:
        numbers.append( [ int(cc) for cc in s.strip().split(' ') ] )
        best_path.append( [ 0 for cc in s.strip().split(' ') ] )

    def best_path_ending( row_number ):
        for i in xrange( row_number ):
            if i == 0:
                best_path[i][i] = numbers[i][i]
            for j in xrange(i+1):
                if j == 0:
                    best_path[i][j] = best_path[i-1][j] + numbers[i][j]
                if j == i:
                    best_path[i][j] = best_path[i-1][j-1] + numbers[i][j]
                if j > 0 and j < i:
                    best_path[i][j] = max( best_path[i-1][j], best_path[i-1][j-1] ) + numbers[i][j]
        return max( best_path[ row_number - 1 ]  )  

    return best_path_ending( len(numbers) )  

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 18 solution is:",  e18()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
