import os, re
from .source import Primes_gen



def get_pfile_num(fname):
    """Extract number of primes from the filename."""
    return int(fname.split(' ')[0])

def filter_pfiles(dir_list):
    """Find all file names matching "<number> primes" (pfile)."""
    return list(filter(lambda fname: re.match(r"\d+ primes", fname), dir_list))

def get_max_pfile(dir_list=None):
    """Find pfile with max number of primes."""
    if dir_list == None:
        dir_list = os.listdir()

    pfiles = filter_pfiles(dir_list)

    if len(pfiles) > 1:
        mx = 0
        for pfile in pfiles:
            n = get_pfile_num(pfile)
            mx = max(n, mx)
        max_pfile = f"{mx} primes"

        remove_lesser_pfiles(max_pfile, pfiles)

        return max_pfile

    elif len(pfiles) == 1:
        return pfiles[0]
    
    return None


def remove_lesser_pfiles(max_pfile, pfiles):
    """Remove all pfiles except max_pfile."""
    for pfile in pfiles:
        if pfile != max_pfile:
            os.remove(pfile)

def save_primes(data:list):
    filename = f"{len(data)} primes"

    dir_list = os.listdir()

    if filename in dir_list:
        print(f"{filename} exists already.")
        return

    max_pfile = get_max_pfile(dir_list) # str or None
    if max_pfile is not None:
        # If number of primes in max_pfile is greater than length of data, then do not save data.
        if len(data) < get_pfile_num(max_pfile):
            print("A file with greater number of primes exists.")
            return

    with open(filename, 'w', encoding="utf-8") as file:
        file.write(str(data))

    max_pfile = get_max_pfile(os.listdir())
    print("Saved to", max_pfile)


def load_primes():
    primes = None
    max_pfile = get_max_pfile()
    if max_pfile is not None and get_pfile_num(max_pfile) > 4:
        filename = max_pfile
        with open(filename, 'r', encoding="utf-8") as file:
            text = file.read()

        primes = eval(text)
    else:
        return [2, 3, 5, 7]
    
    if primes:
        print(f"Loaded {len(primes)} primes")
    return primes

def more_primes(limit):
    """Loads primes if any. Generates new ones and saves them each time prime count is divisible by 1000 (to preserve data from accidential loss). If process of generation takes too long, it can be canceled with Ctrl+c, and the generated data will be saved to file."""
    primes = load_primes()

    primes_gen = Primes_gen(limit, primes)
    
    try:
        while limit > primes[-1]:
            if len(primes)%1000 == 0:
                print("limit =", limit, "| max prime =", primes[-1])
                save_primes(primes)
            
            try:
                next(primes_gen)
            except StopIteration:
                break
    except KeyboardInterrupt:
        pass

    save_primes(primes)
    return primes