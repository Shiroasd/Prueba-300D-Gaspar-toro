import csv
import Menu
agregarCliente = True
agregarCompra = True
listaProductos = []
data = []
listaProductosClientes =[]
valor = 0
valorDeVenta = 0
ValorDeCompra = 0

def no_valido():
    print("No valido intente nuevamente")

def no_disponible():
    print("No Disponible Intenta nuevamente")

def menu_productos():
    print("Productos/Precios")
    print("1.Abono / 1.200$")
    print("2.Tierra / 1.000$")
    print("3.Lirio / 1.100$")
    print("4.Rosas rojas / 1.700$")
    print("5.Margaritas / 1.100$")
    print("0.Salir")



print("**Bienvenido a green garden**")
print("**Ingresa tus datos personales a continuacion**") 


while agregarCliente:
    listaProductosClientes.clear()
    print("Ingresa tus datos")

    nombre = input("Nombre: ")
    while not nombre.isalpha():
        no_valido()
        nombre=input("Nombre: ")

    telefono = input("Telefono: ")
    while not telefono.isdigit() or len(telefono)<9 or len(telefono)>9:
        if len(telefono)<9 or len(telefono)>9:
            print("Debe tener 9 digitos")
        else:
            no_valido()
        telefono = input("Telefono: ")

    direccion = input("Direccion: ")



agregarCompra = True
listaProductos.clear()
valorDeVenta = 0
while agregarCompra:
    menu_productos

    producto = input("Ingrese el numero de tu producto:")
    if int(producto) == 0:
        agregarCliente=False
        break


while not producto.isdigit() or int(producto)<0 or int(producto)<5:
    if producto.isdigit():
        if int(producto)<0 or int(producto)>5:
            no_disponible()
    elif producto.lower() == "M":
        menu_productos

    else:   
        no_valido

    producto = input("ingrese El numero del producto /para ver menu Oprimir letra M ")

unidades_productos = input ("Unidades: ")
while not unidades_productos.isdigit() or int(producto)<0:

    if unidades_productos.isdigit():
        if int(producto)<0:
            no_disponible()
    else:
        no_valido
        unidades_productos = input("unidades: ")


    if int(producto) == 1:
        valor =1200
    elif int(producto) ==2:
        valor =1000
    elif int(producto) ==3:
        valor =1100
    elif int(producto) ==4:
        valor =1700
    elif int(producto) ==5:
        valor =1100


valorDeVenta+=valor*int(unidades_productos)
ValorDeCompra=valor*int(unidades_productos)
listaProductosClientes.append ([f"code:{producto}",f"units:{unidades_productos}"])
listaProductos.append(["producto {producto}",f"cantidad{unidades_productos}",f"valor: {ValorDeCompra}"])


compra = input("ingrese la compra: 1.si / 2.no")
while not compra.isdigit() or int(compra)!=1 and int(compra)!=2:

    if not compra.isdigit():
        no_valido()
    elif int(compra)!=1 or int (compra)!=2:
        no_disponible

    compra = input ("agregar compra: 1.si/2.no")

if int(compra)==2:
    agregarCompra = False



data.append([nombre,telefono,direccion,listaProductosClientes])


print("*****Boleta*****")






nuevoCliente = input("Ingresar un nuevo cliente 1.si / 2.no")
while not nuevoCliente.isdigit() or int(nuevoCliente)!=1 and int(nuevoCliente)!=2:

    if not nuevoCliente.isdigit():
        no_valido
    elif int(nuevoCliente)!=1 or int(nuevoCliente)!=2:
        no_disponible()


    nuevoCliente = input("ingresa un nuevo cliente: 1.si/2.no")
if int (nuevoCliente)==2:
    agregarCliente= False
print("saliendo")





with open ('Info.csv', 'w') as archivoCsv:

    escritorCsv = csv.writer(archivoCsv)

    escritorCsv.writerow(["nombre","telefono","direccion","productos"])

    escritorCsv.writerows(data)