
        
import time


num_letters = {  0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3,
                            11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6,
                            30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 100:10,
                            200:10, 300:12, 400:11, 500:11, 600:10, 700:12, 800:12, 900:11, 1000:11 }

def e17():
    def num_word_length( num ):
        if num in num_letters:
            return num_letters[num]

        if num >= 100:
            huns = num / 100
            hunRem = num % 100
            return num_word_length( huns * 100 ) + 3 + num_word_length( hunRem )

        ones = num % 10
        tens = num / 10 % 10

        return num_word_length( tens * 10 ) + num_word_length( ones )

    end_range = 1000
    return sum( num_word_length(i) for i in xrange(1, end_range + 1)  )

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 17 solution is:",  e17()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
