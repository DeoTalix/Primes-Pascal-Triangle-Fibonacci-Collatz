from bisect import bisect



def scan_primes(n, primes:list):
    for p in primes:
        if n % p == 0:
            return False
    return True

def is_prime(n, primes):
    if isinstance(primes, set):
        return n in primes
    elif isinstance(primes, list):
        i = bisect(primes, n)
        return primes[i-1] == n
    else:
        raise TypeError(f"'primes' must be list or set.")

def Primes(limit, primes=[2,3,5,7]):
    i = primes[-1]

    if i >= limit:
        j = bisect(primes, limit)
        return primes[:j]

    while i < limit:
        if scan_primes(i, primes):
            primes.append(i)
            yield i
        i += 2