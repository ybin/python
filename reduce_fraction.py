import sys

def gcd(m, n):
    while n:
        m, n = n, m % n
    return m

def reduce_fraction(num_0, num_1):
    gcd_ = gcd(num_0, num_1)
    return (num_0/gcd_, num_1/gcd_)

if __name__ == '__main__':
    print('fraction:: %d : %d' % reduce_fraction(int(sys.argv[1]), int(sys.argv[2])))
