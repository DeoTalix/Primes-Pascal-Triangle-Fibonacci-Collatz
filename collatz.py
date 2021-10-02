from random import randint
from PIL import Image, ImageDraw



def Collatz(n):
    return 3*n+1 if n%2 else n//2

def draw_collatz():    
    W, H = 1_000,  1_000
    image = Image.new("RGB", (W, H))
    draw  = ImageDraw.Draw(image)
    fill = (255, 255, 255)

    x, y = randint(1, 1000), randint(1, 1000)

    f = lambda v, N: N // (v % 9 or 9)

    while x > 4 or y > 4:
        #print(x, y)

        x_ = Collatz(x)
        y_ = Collatz(y)

        xa, ya = f(x,W), f(y,H)
        xb, yb = f(x_,W),f(y_,H)
        
        draw.line([(xa, ya), (xb, yb)], fill)
        draw.point((xb,yb), fill=0)

        x, y = x_, y_

    image.save("images/cl_random.bmp")
    print("Image saved to images/cl_random.bmp")
        