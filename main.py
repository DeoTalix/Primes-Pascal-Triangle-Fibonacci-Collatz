
from primes.utility import load_primes



def form_mods(n, mods):
    s = ''
    for mod in mods:
        m = n % mod
        s += str(m).rjust(m+1).ljust(mod)
    return s

def as_binary_dots(n):
    """Converts n to binary in the form of dotts. Example: 101011 -> '. . ..'"""
    return bin(n)[2:].replace('0',' ').replace('1','.')

def main():
    primes = load_primes()[:1000]
    int_max = len(str(primes[-1]))
    bin_max = len(bin(primes[-1])[2:])

    for i,n in enumerate(primes):
        # Primes
        print(str(n).rjust(int_max), end='\t')
        
        # Binary representation dotted pattern
        print(as_binary_dots(n).rjust(bin_max,' '), end='\t')
        
        # Mod 9 remainder spiral pattern
        print(form_mods(n, [9]))
    
    print()

    

if __name__ == "__main__":
    from pascal import pt_serpinski, pt_fibonacci, pt_collatz
    from collatz import draw_collatz
    from mandelbrot import draw_mandelbrot

    from threading import Thread
    
    functions = [pt_serpinski, pt_fibonacci, 
                 pt_collatz, draw_collatz, 
                 draw_mandelbrot, main]
    threads = []
    for f in functions:

        t = Thread(target=f)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    