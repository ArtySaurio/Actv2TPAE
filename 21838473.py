import matplotlib.pyplot as plt
import warnings
import numpy as np
from random import randint

warnings.filterwarnings("ignore")

usuario = '21838473@live.uem.es'
contrasena = '123'


################################################################################################ EJERCICIO A

def mediana(n):
    vr1 = np.random.randint(1, 30, n)
    vr2 = np.random.randint(1, 30, n)
    vr1.sort()
    vr2.sort()

    print("\nVector aleatorio 1:")
    print(vr1)
    print("\nVector aleatorio 2:")
    print(vr2)

    # Ordenamos y concatenamos con .concatenate el array
    v = np.concatenate([vr1, vr2])
    v.sort()
    print(v)
    i = int(len(v) / 2)
    mediana = ((v[i - 1] + v[i]) / 2)
    print("Mediana:", mediana)


################################################################################################ EJERCICIO B

def veceq(n):
    vr3 = np.random.randint(1, 30, n)
    vr4 = np.random.randint(1, 30, n)

    print("\nVector aleatorio 3:")
    print(vr3)
    print("\nVector aleatorio 4:")
    print(vr4)
    return vecrec(vr3, vr4)


# Dividimos array en otros dos arrays iguales
def divarrays(arr):
    cont = 1
    arr1 = []
    arr2 = []

    for i in arr:
        if (cont <= (len(arr) / 2)):
            arr1.append(i)
        else:
            arr2.append(i)
        cont += 1
    res = [arr1, arr2]
    return res


# Aplicamos divide y venceras comprobando los nmors
def vecrec(arr, brr):
    if (len(arr) == 1):
        if (arr == brr):
            return True
        else:
            return False
    else:
        res1 = divarrays(arr)
        res2 = divarrays(brr)
        if (vecrec(res1[0], res2[0]) and vecrec(res1[1], res2[1])):
            return True
        else:
            return False


################################################################################################ EJERCICIO C

def mtraspuesta(A):
    p = A.shape[0]
    q = A.shape[1]

    if p == 0 or q == 0:
        return A
    elif p == 1:
        return fila_columna(A)
    elif q == 1:
        return columna_fila(A)
    else:
        MA11 = A[:p // 2, :q // 2]
        MA12 = A[:p // 2, q // 2:]
        MA21 = A[p // 2:, :q // 2]
        MA22 = A[p // 2:, q // 2:]

        MATRA = np.vstack(
            (np.hstack((mtraspuesta(MA11), mtraspuesta(MA21))), np.hstack((mtraspuesta(MA12), mtraspuesta(MA22)))))
        return MATRA


# Cast filas a columnas con base de origen y venceras
def fila_columna(A):
    p = A.shape[0]
    q = A.shape[1]

    if p == 1 and q == 1:
        return A
    else:
        return np.vstack((A[:, 0:1], fila_columna(A[:, 1:])))


# Cast columnas a filas con base de origen y venceras
def columna_fila(A):
    p = A.shape[0]
    q = A.shape[1]

    if p == 1 and q == 1:
        return A
    else:
        return np.hstack((A[0:1, :], columna_fila(A[1:, :])))


################################################################################################ EJERCICIO D

def peak_valley(n):
    print("\nCreo y verifico array")

    arr = creamosarray(n)
    loops = 0
    arr_verified = verifarray(arr, loops)
    imprarray(arr_verified)

    print("\nCarga de los picos y los valles")
    pico_o_valle(arr_verified)
    dibujargrafico(arr_verified)
    max_dist = encontrardistancia(arr_verified, arr_verified)

    print("\nMax distancia entre los picos y los valles: ", max_dist)
    plt.show()


# Creamos clase y almacenamos dentro los valores de antes y despues para saber distinguir entre pico y valle
class nmor:
    def __init__(self, data, prev, next, indice):
        self.data = data
        # Valor previo y valor siguiente
        self.prev = prev
        self.next = next
        self.indice = indice
        # Tipo o pico o valle
        self.tipo = None

    def __str__(self):
        template = "data:{} prev:{} next:{} indice:{} tipo:{}"
        return template.format(self.data, self.prev, self.next, self.indice, self.tipo)

    def __repr__(self):
        return str(self)


# Funcion para crear array aleatorio
def creamosarray(n):
    arrayaleat = np.random.randint(20, size=n)
    numesarray = []

    for i in range(n):
        if (i == 0):
            numb = nmor(arrayaleat[i], None, arrayaleat[i + 1], i)
        elif (i == (n - 1)):
            numb = nmor(arrayaleat[i], arrayaleat[i - 1], None, i)
        else:
            numb = nmor(arrayaleat[i], arrayaleat[i - 1], arrayaleat[i + 1], i)
        numesarray.append(numb)
    return numesarray


# Comprobamos que el array cumple requisitos
def comprobarray(a):
    for i in a:
        if (i.data == i.next):
            return False
    return True


# Creamos funcion para verificar array, si no cumple requisitos loop de generarlo
def verifarray(a, loops):
    if (comprobarray(a)):
        print("\nVeces necesarias para validar el array: ", loops)
        print("\nEl array ha sido verificado correctamente")
        return a
    else:
        loops += 1
        new_arr = creamosarray(len(a))
        return verifarray(new_arr, loops)


# Creamos una funcion para hacer print al array
def imprarray(arrn):
    sample = []

    for i in arrn:
        sample.append(i.data)
    print(sample)


# Creamos funcion para dividir array
def divarray(a):
    half = len(a) // 2
    res = [a[:half], a[half:]]
    return res


# Creamos funcion para declarar si el array sera pico o sera valle
def pico_o_valle(a):
    if (len(a) == 1):
        numb = a[0]
        if (numb.prev == None or numb.next == None):
            pass
        elif (numb.prev < numb.data > numb.next):
            numb.tipo = 'pico'
        elif (numb.prev > numb.data < numb.next):
            numb.tipo = 'valle'
    else:
        res = divarray(a)
        pico_o_valle(res[0])
        pico_o_valle(res[1])


# Creacion de funcion para ver la distancia entre puntos array
def encontrardistancia(arr, full_arr):
    l = 0
    r = 0

    if (len(arr) == 1):
        num = arr[0]
        if (num.tipo == 'pico'):
            l = encontrarpunto(num, 1, full_arr, 'valle')
            r = encontrarpunto(num, -1, full_arr, 'valle')
        elif (num.tipo == 'valle'):
            l = encontrarpunto(num, 1, full_arr, 'pico')
            r = encontrarpunto(num, -1, full_arr, 'pico')
        else:
            return 0
    else:
        res = divarray(arr)
        l = encontrardistancia(res[0], full_arr)
        r = encontrardistancia(res[1], full_arr)
    if (l > r):
        return l
    else:
        return r


# Encontramos el punto lejano maximo que hay entre un pico y entr un valle
def encontrarpunto(num, orientation, full_arr, tipo):
    if (orientation == -1):
        for i in range(1, num.indice):
            if (full_arr[num.indice - i].tipo == tipo):
                return i
    else:
        for i in range(1, len(full_arr) - num.indice):
            if (full_arr[num.indice + i].tipo == tipo):
                return i
    return 0


# Tendremos que de¡ibujar un grafico
def dibujargrafico(a):
    x = []

    for i in range(len(a)):
        x.append(i)
    y = []

    for j in a:
        y.append(j.data)
    fig = plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='red', linestyle='-', linewidth=3, marker='o', markerfacecolor='blue', markersize=8)

    plt.ylim(0, 21)
    plt.xlim(-1, len(a))

    for k in range(len(a)):
        label = "data:{} ({})".format(a[k].data, a[k].tipo)
        plt.annotate(label, (k, a[k].data), textcoords="offset points", xytext=(0, 10), ha='center')

    plt.xlabel('Indice')
    plt.ylabel('Dato')

    plt.title('Distancia maxima entre picos y valles')
    ax = plt.axes()
    ax.set_facecolor("white")
    plt.show(block=False)


################################################################################################ EJERCICIO E

def genMatrix(n):
    newMarix = []

    for i in range(0, n):
        dataline = []
        for j in range(0, n):
            dataline.append(randint(0, 10))

        for j in range(0, n):
            Vals = list(map(float, dataline))

        newMarix.append(Vals)
    return newMarix


def split(matrix):
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]


def strassen(x, y):
    if len(x) == 1:
        return x * y

    a, b, c, d = split(x)
    e, f, g, h = split(y)

    p1 = strassen(a, f - h)
    p2 = strassen(a + b, h)
    p3 = strassen(c + d, e)
    p4 = strassen(d, g - e)
    p5 = strassen(a + d, e + h)
    p6 = strassen(b - d, g + h)
    p7 = strassen(a - c, e + f)
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

    return c


################################################################################################

def clr(lines=50):
    print('\n' * lines)


def menu(ex):
    choice = '0'
    bool = False
    while bool != True:
        print("\nPreparando el menu para la siguiente opcion que desee...")

        clr()

        print("|------------------------------------------------------------|")
        print("|    ****** UNIVERSIDAD EUROPEA DE MADRID ******             |")
        print("|    Escuela de Arquitectura, Ingenieria y Disenio           |")
        print("|                                                            |")
        print("|    A: Hallar mediana vector                                |")
        print("|    B: Vectores iguales en todas sus posiciones             |")
        print("|    C: Matriz transpuesta                                   |")
        print("|    D: Maxima diferencia entre pico y valle consecutivos    |")
        print("|    E: Multiplicar matrices algoritmo Strassen              |")
        print("|    F: Elementos mas grandes por fila y columna             |")
        print("|    S: SALIR                                                |")
        print("|------------------------------------------------------------|")

        choice = input("\nIntroduzca su opcion: ")

        if choice == "S" or choice == "s":
            print("\nGracias por usar nuestra aplicacion")
            bool = True
        elif choice == "A" or choice == "a":
            mediana(ex)
        elif choice == "B" or choice == "b":
            if (veceq(ex) == True):
                print("\nLos vectores son iguales")
            else:
                print("\nLos vectores son distintos entre si")
        elif choice == "C" or choice == "c":
            A = np.random.randint(1, 20, (ex, ex))
            print("\nLa matriz original y aleatoria es: ")
            print(A)
            print("\nLa matriz final y traspuesta es: ")
            print(mtraspuesta(A))
        elif choice == "D" or choice == "d":
            peak_valley(ex)
        elif choice == "E" or choice == "e":
            sN = tN = ex
            matrizA = genMatrix(sN)
            matrizB = genMatrix(tN)
            matrizA = np.matrix(matrizA)
            matrizB = np.matrix(matrizB)

            print(strassen(matrizA, matrizB))
        else:
            print("\nError seleccione una opcion entre A y H")


fin = False
while (fin == False):

    print("""
       ______________________________________________________________
     .'  __________________________________________________________  '.
     : .'                                                          '. :
     | |      ________________________________________________      | |
     | |    .:________________________________________________:.    | |
     | |    |                                                  |    | |
     | |    |           ACTIVIDAD EXTRAORDINARIA TPA           |    | |
     | |    |                                                  |    | |
     | |    |           Arturo Alba Sanchez-Mayoral            |    | |
     | |    |                                                  |    | |
     | |    |                                                  |    | |
     | |    |           Expediente: 21838473                   |    | |
     | |    |                                                  |    | |
     | |    |                                                  |    | |
     | |    |                                                  |    | |
     | |    |                                                  |    | |
     | |    |            __________________________            |    | |
     | |    |           |  |  |  |  |  |  |  |  |  |           |    | |
     | |    '.__________|__|__|__|__|__|__|__|__|__|__________.'    | |
     | |                                                            | |
     | |                            iMac                            | |
     : '.__________________________________________________________.' :
      ".____________________________\__/____________________________."
      """)

    u = input("\nIntroduzca el email de la universidad: ")
    c = input("\nIntroduzca la contrasena: ")
    if usuario == u and contrasena == c:
        print("\nLogin correcto")
        exp = int(input("\nIntroduzca el numero de su expediente: "))
        fin = True
        clr()
        menu(exp)
    else:
        print("\nError login incorrecto")
        clr()
