def pascal_triangle(X, Y, oper=lambda a,b: a+b, symmetrical=True):
    """
    X and Y: iterables or generators

    Generates matrix with 'X' as x-coordinate, and 'Y' as y-coordinate,
    and other cells filled with values produced by 'oper' callback
    where 'a' is a cell of a previous 'i' (row) and current 'j' (column)
    and 'b' is a cell of a current 'i' (row) and previous 'j' (column).
    """
    
    matrix = [[0]]

    # Builds first row with values from X
    for i,v in enumerate(X, 1):
        matrix[0].append(v)

    # Width of the matrix
    W = len(matrix[0])

    # Builds other rows filled with zeroes
    # Copies values from Y to the first column
    for j,v in enumerate(Y, 1):
        matrix.append([0] * W)

    # Height of the matrix
    H = len(matrix)

    # Fills the rest of the matrix with values produced by oper(a,b) 
    if symmetrical:
        for i in range(1, H):
            for j in range(i, W):
                if i == j:
                    # Since matrix is symmetrical on the diagonal
                    # apply oper(a, a) when i and j are the same.
                    matrix[i][j] = oper(matrix[i-1][j], matrix[i-1][j])
                else:
                    matrix[i][j] = oper(matrix[i-1][j], matrix[i][j-1])
                    matrix[j][i] = matrix[i][j]
    else:
        for i in range(1, H):
            for j in range(1, W):
                # Since matrix is not symmetrical calculate every cell.
                matrix[i][j] = oper(matrix[i-1][j], matrix[i][j-1])

    return matrix

def output_matrix(M, output_cell=(lambda cell,x,y: print(cell, end=' ')), 
                     new_line=(lambda cell,x,y: print())):
    """Iterates through the matrix, and applies the output_cell callback to each cell. 
    Use the new_line callback to control the transition to the next row."""
    
    for y,row in enumerate(M):
        for x,v in enumerate(row):
            output_cell(v, x, y)
        new_line(v, x, y)

def default_fill_method(cell):
    """Default callback for the draw_matrix fill_method"""
    cell = cell % 9 or 9 if cell else 0
    if cell != 0:
        val = 255//cell
    else:
        val = 0
    return (val, val, val) # RGB

def draw_matrix(M, image_name, fill_method=default_fill_method):
    """Outputs matrix in an image file."""
    from PIL import Image, ImageDraw

    W = len(M[0])
    H = len(M)

    image = Image.new("RGB", (W, H))
    draw  = ImageDraw.Draw(image)
  
    def draw_method(cell, x, y):
        draw.point((x,y), fill=fill_method(cell, x, y))

    output_matrix(M, output_cell=draw_method, new_line=(lambda *a: None))

    image.save(image_name)
    print(f"Image saved to {image_name}")

def pt_serpinski():
    """Serpinski Pattern in Pascal Triangle."""
    X = Y = [1] * 1_000
    
    Pt = pascal_triangle(X, Y)
    #method = (lambda v: print(" ." if v%2 else '  ', end=''))
    #output_matrix(Pt, output_cell = method)
    def method(cell, x, y):
        #r = 256 // (cell % 9 or 9)
        r = 255 * (cell % 2 == 0)
        g = 255 * (cell % 2 != 0)
        b = round(y / 1_000 * r)
        return (r, g, b)

    draw_matrix(Pt, "images/pt_serpinski.bmp", fill_method=method)

def pt_fibonacci():
    """Pascal Triangle with x and y coordinates as a Fibonacci sequence."""
    from fibonacci import Fibonacci_gen

    X = Fibonacci_gen(1_000)
    Y = Fibonacci_gen(1_000)
    
    Pt = pascal_triangle(X, Y)
    #method = (lambda v: print(f"{v % 9 or 9}" if v and v % 9 in [3,6,0] else ' ', end=' '))
    #output_matrix(Pt_ones, output_cell=method)
    def method(cell, x, y):
        r = 256 // (cell % 9 or 9)
        g = 256 // (cell % 2 + 1)
        b = round(y / 1_000 * 255)
        return (r, g, b)

    draw_matrix(Pt, "images/pt_fibonacci.bmp", fill_method=method)

def pt_collatz():
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
    X = range(1, size)
    Y = range(1, size)
    
    Pt = pascal_triangle(X, Y, oper=( lambda a,b: (3*(a+b)+1) if (a+b)%2 else (a+b)//2 ))

    def method(cell, x, y):
        r = 256 // (cell % 9 or 9)
        g = 256 // (cell % 2 + 1)
        b = round(y / 1_000 * 255)
        return (r, g, b)

    draw_matrix(Pt, "images/pt_collatz.bmp", fill_method=method)
