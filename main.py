
from primes.utility import load_primes



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
        print(str(n).rjust(int_max), end='\t')
        print(bin(n)[2:].replace('0',' ').replace('1','.').rjust(bin_max,' '), end='\t')
        print(form_mods(n, [10]))#, end='\t')
        #print((n-1)%3, end='\n' if i==0 else '\t')
        #if i > 0: print(f"{primes[i] - primes[i-1]}")
    


if __name__ == "__main__":
    main()