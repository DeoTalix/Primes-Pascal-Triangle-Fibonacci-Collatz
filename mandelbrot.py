def Mandelbrot(c, max_iter=100):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def draw_mandelbrot(max_iter=100):
    from PIL import Image, ImageDraw

    # Image size (pixels)
    W = 600
    H = 400

    # Plot window
    RE_START = -2
    RE_END = 1
    IM_START = -1
    IM_END = 1

    palette = []

    image = Image.new('RGB', (W, H), (0, 0, 0))
    draw = ImageDraw.Draw(image)

    for x in range(0, W):
        for y in range(0, H):
            # Convert pixel coordinate to complex number
            c = complex(RE_START + (x / W) * (RE_END - RE_START),
                        IM_START + (y / H) * (IM_END - IM_START))
            # Compute the number of iterations
            m = Mandelbrot(c, max_iter)
            # The color depends on the number of iterations
            color = 255 - int(m * 255 / max_iter)
            # Plot the point
            draw.point([x, y], (color, color, color))

    image.save('images/mandelbrot.bmp')
    print("Image saved to images/mandelbrot.bmp")