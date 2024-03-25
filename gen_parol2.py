from random import *
from string import *
iskl = 'lI1oO0'
sym = ascii_letters+str(digits)
for i in range(len(iskl)):
    sym = sym.replace(iskl[i], '')
shuffle(list(sym))
n = int(input())
m = int(input())


def generate_password(length):
    flag = False
    while flag != True:
        digits = 0
        up = 0
        down = 0
        x = sample(sym, length)
        for i in x:
            if i.isdigit() == True:
                digits = digits+1
            else:
                if i in ascii_uppercase:
                    up = up+1
                elif i in ascii_lowercase:
                    down = down+1
        if digits >= 1 and up >= 1 and down >= 1:
            flag = True
    return (print(*x, sep=''))


def generate_passwords(count, length):
    for i in range(count):
        generate_password(length)


generate_passwords(n, m)
