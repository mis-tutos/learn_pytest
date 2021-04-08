def suma(x, y):
    """
    funcion que devuelve 2 argumentos y devuelve la suma
    """
    return x + y

print(suma(2,4))


def escribir(fpath, data_in):
    with open(fpath, "w") as file_in:
        file_in.write(data_in)


class calculadora:
    def sumar(x,y):
        return suma(x,y)