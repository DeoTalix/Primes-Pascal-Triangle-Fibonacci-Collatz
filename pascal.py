def pascal_triangle(X, Y, oper=lambda a,b: a+b, half=False):
    """
    X: iterable, Y: iterable
    """
    
    matrix = [[0]]#*len(X) for i in range(len(Y))]

    for i,v in enumerate(X, 1):
        matrix[0].append(v)

    W = len(matrix[0])

    for j,v in enumerate(Y, 1):
        matrix.append([0] * W)
        if half == True: v = 0
        matrix[j][0] = v

    H = len(matrix)

    for i in range(1, H):
        for j in range(i if half else 1, W):
            if half and i == j:
                matrix[i][j] = oper(matrix[i-1][j], matrix[i-1][j])
            else:
                matrix[i][j] = oper(matrix[i-1][j], matrix[i][j-1])

    return matrix

def output_matrix(M, 
                 output_cell=(lambda cell: print(cell, end=' ')), 
                 new_line=print):

    for row in M:
        for v in row:
            output_cell(v)
        new_line()

def default_fill_method(cell):
    cell = cell % 9 or 9 if cell else 0
    if cell != 0:
        val = 255//cell
    else:
        val = 0
    return (val, val, val) # RGB

def draw_matrix(M, image_name, fill_method=default_fill_method):
    from PIL import Image, ImageDraw

    W = len(M[0])
    H = len(M)

    image = Image.new("RGB", (W, H))
    draw  = ImageDraw.Draw(image)

    x, y = 0, 0
    
    def draw_method(cell):
        nonlocal x,y
        draw.point((x,y), fill=fill_method(cell))
        x += 1

    def new_line():
        nonlocal x,y
        x, y = 0, y + 1

    output_matrix(M, output_cell=draw_method, new_line=new_line)

    image.save(image_name)


def pascal_primes():
    from primes.source import Primes_gen, is_prime
    from primes.utility import save_primes, load_primes, more_primes

    X = Y = [1] * 65

    Pt_ones = pascal_triangle(X, Y, half=True)

    max_val = Pt_ones[-1][-1]
    primes = more_primes(max_val)

    prime_set = set(primes)

    # various callbacks
    prime_dots     = (lambda v: '.' if is_prime(v, prime_set) else ' ')
    mod_nine       = (lambda v: v % 9)
    odd_even       = (lambda v: ('o' if v % 10 in [1, 3, 7, 9] else '.') if v % 2 else ' ')
    prime_mod_nine = (lambda v: '*' if v % 9 in [1, 3, 7, 9] else ' ')

def pascal_serpinski():
    """Dotted Serpinski Pattern"""
    X = Y = [1] * 1_000
    
    Pt = pascal_triangle(X, Y, half=False)
    #method = (lambda v: print(" ." if v%2 else '  ', end=''))
    #output_matrix(Pt, output_cell = method)
    def method(cell):
        r = 256 // (cell % 9 or 9)
        g = 256 // (cell % 2 + 1)
        b = cell % 256
        return (r, g, b)

    draw_matrix(Pt, "images/pt_serpinski.bmp", fill_method=method)

def pascal_fibonacci():
    from fibonacci import Fibonacci

    X = Fibonacci(1_000)
    Y = Fibonacci(1_000)
    
    Pt = pascal_triangle(X, Y, half=False)
    #method = (lambda v: print(f"{v % 9 or 9}" if v and v % 9 in [3,6,0] else ' ', end=' '))
    #output_matrix(Pt_ones, output_cell=method)
    def method(cell):
        r = 256 // (cell % 9 or 9)
        g = 256 // (cell % 2 + 1)
        b = cell % 256
        return (r, g, b)

    draw_matrix(Pt, "images/pt_fibonacci.bmp", fill_method=method)

def pascal_collatz():
    size = 1_000

    def X_gen(limit, n=1):
        while limit > 0:
            yield n
            n = 3*n+1
            limit -= 1

    def Y_gen(limit, n=1):
        while limit > 0:
            yield n
            n *= 2
            limit -= 1

    #X = X_gen(size)
    #Y = Y_gen(size)
    X = Y = range(1, size)
    
    Pt = pascal_triangle(X, Y, oper=( lambda a,b: (3*(a+b)+1) if (a+b)%2 else (a+b)//2 ))

    def method(cell):
        r = 256 // (cell % 9 or 9)
        g = 256 // (cell % 2 + 1)
        b = cell % 256
        return (r, g, b)

    draw_matrix(Pt, "images/pt_collatz.bmp", fill_method=method)

    



def main():
   pascal_serpinski()
   #pascal_fibonacci()
   #pascal_collatz()


if __name__ == "__main__":
    main()
