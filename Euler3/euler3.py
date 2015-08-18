def readprimes (filename):
    var = str(filename)
    lines = []
    primes = []
    file = open(filename, 'r')
    #trailing and preceding whitespace removal
    all = [ line.rstrip() for line in file.readlines() ]

    #ignore empty lines
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    numstring = ''
    for line in lines:
        linesplit = line.strip(' ')
        for k in linesplit:
            if k == ' ' and numstring[-1] == ' ':
                continue
            else:
                numstring += k

    primes = numstring.split(' ')
    out = []
    for char in primes:
        out.append(int(char))
    return out


