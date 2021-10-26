def maximo (x, y, z):
    if x >= y >= z:
        return x
    if x >= z >= y:
        return x
    if z >= x >= y:
        return z
    if z >= y >= x:
        return z
    if y >= z >= x:
        return y
    if y >= x >= z:
        return y