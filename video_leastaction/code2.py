def sin(x):
    return numpy.sin(x)
def cos(x):
    return numpy.cos(x)

def ddf1(f1, f2, df1, df2):
    return (-sin(f1 - f2) * (cos(f1 - f2) * df1 ** 2 + df2 ** 2)
            - g / l * (2 * sin(f1) + cos(f1 - f2) * sin(f2))) / (2 - cos(f1 - f2) ** 2)


def ddf2(f1, f2, df1, df2):
    return (sin(f1 - f2) * (cos(f1 - f2) * df2 ** 2 + 2 * df1 ** 2)
            - g / l * (2 * sin(f2) + cos(f1 - f2) * sin(f1))) / (2 - cos(f1 - f2) ** 2)
