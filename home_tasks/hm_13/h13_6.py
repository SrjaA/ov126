def fctrl(n):
    if n == 0:
        return 1
    return fctrl(n-1) * n


print(fctrl(int(input('enter number:\t'))))


