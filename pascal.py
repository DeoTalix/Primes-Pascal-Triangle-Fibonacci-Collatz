def pascal_triangle(X, Y, oper=lambda a,b: a+b, half=False):
    """
    X: iterable, Y: iterable
    """
    
    matrix = [[0]*len(X) for i in range(len(Y))]

    for i in range(1, len(X)):
        matrix[0][i] = X[i-1]

    if half == False:
        for j in range(1, len(Y)):
            matrix[j][0] = Y[j-1] 

    for i in range(1, len(Y)):
        for j in range(i if half else 1, len(X)):
            if half and i == j:
                matrix[i][j] = oper(matrix[i-1][j], matrix[i-1][j])
            else:
                matrix[i][j] = oper(matrix[i-1][j], matrix[i][j-1])

    return matrix

def print_matrix(M, callback=(lambda cell: cell), format=(lambda cell: cell), sep=' '):
    for row in M:
        for v in row:
            v_ = callback(v)
            print(format(v_), end='')
        print()

def main():
    from primes.source import Primes, is_prime
    from primes.utility import save_primes, load_primes

    #X = [1] * 65#range(1,60)
    #Y = [1] * 65#range(1,60)
    #Pt_ones = pascal_triangle(X, Y, half=True)

    if 0:
        primes = load_primes()
        max_val = Pt_ones[-1][-1]
        primes_iter = Primes(max_val, primes)
        
        try:
            while max_val > primes[-1]:
                if len(primes)%1000 == 0:
                    print("Pt max_val =", max_val, "| max prime =", primes[-1])
                    save_primes(primes)
                
                try:
                    next(primes_iter)
                except StopIteration:
                    break
        except KeyboardInterrupt:
            pass

        save_primes(primes)

        prime_set = set(primes)

    # various callbacks
    prime_dots     = (lambda v: '.' if is_prime(v, prime_set) else ' ')
    mod_nine       = (lambda v: v % 9)
    odd_even       = (lambda v: ('o' if v % 10 in [1, 3, 7, 9] else '.') if v % 2 else ' ')
    prime_mod_nine = (lambda v: '*' if v % 9 in [1, 3, 7, 9] else ' ')
    
    # Dotted Serpinski Pattern
    # print_matrix(Pt_ones, format = (lambda v: " ." if v%2 else '  '), sep='')

    # X = [1] * 65#range(1,60)
    # Y = [1] * 65#range(1,60)
    # Pt_ones = pascal_triangle(X, Y, half= False)

    # 3 6 9 pattern
    # print_matrix(Pt_ones, callback=lambda v: v % 9 or 9 if v % 9 in [3,6,0] else ' ', format=lambda v: f"{v} ")

    X = range(1, 60)
    Y = range(1, 60)
    
    Pt_collatz = pascal_triangle(X, Y, oper=lambda a,b: (3*(a+b)+1) if (a+b)%2 else (a+b)//2,)
    print_matrix(
        Pt_collatz, 
        callback=lambda v: v%9 or 9 if v else 0, 
        format=lambda v: f". " if v!=7 else '  ',
    ) # A fractal ?

if __name__ == "__main__":
    main()
