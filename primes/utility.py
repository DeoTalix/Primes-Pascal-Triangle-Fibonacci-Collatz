import os, re
from .source import Primes



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

    # If filename exists in the directory promt user for overwrite-action.
    if filename in dir_list:
        inp = input(f"{filename} already exists. Overwrite? [y/n]\n: ")
        if inp.lower() == 'n': return
        if inp.lower() == 'y': pass

    max_pfile = get_max_pfile(dir_list)
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
    primes = Primes(limit)
    save_primes(primes)