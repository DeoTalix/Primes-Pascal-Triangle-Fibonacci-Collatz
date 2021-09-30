
from primes.utility import load_primes
from pascal import main as pascal_main



def form_mods(n, mods):
    s = ''
    for mod in mods:
        m = n % mod
        s += str(m).rjust(m+1).ljust(mod)
    return s

def main():
    primes = load_primes()[:1000]
    int_max = len(str(primes[-1]))
    bin_max = len(bin(primes[-1])[2:])

    for i,n in enumerate(primes):
        # Primes
        print(str(n).rjust(int_max), end='\t')
        
        # Binary representation dotted pattern
        print(bin(n)[2:].replace('0',' ').replace('1','.').rjust(bin_max,' '), end='\t')
        
        # Mod 9 remainder spiral pattern
        print(form_mods(n, [9]))
    
    print()

    

if __name__ == "__main__":
    #main()
    pascal_main()