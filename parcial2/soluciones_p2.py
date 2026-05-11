'''
Punto 1.1
'''
def G1():
    a,b,c = 1,1,1
    while True:
        yield a
        a,b,c = b,c,a+b+c

'''
Punto 1.2
'''
def tresfibonacci(n):
    cont = 0
    a,b,c = 1,1,1
    while cont<n:
        yield a
        a,b,c = b,c,a+b+c

'''
Punto 2
'''
def f2(func):
    cont = [0]
    def wrapper(*args, **kwargs):
        while cont[0] < 3:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                cont[0] += 1
                print(f'Ha cometido {cont[0]} error(es): {type(e).__name__}')
                return None
        print("Leer la documentación")
    return wrapper    