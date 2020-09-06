#Importamos el archivo con las listas
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

#Asignamos nombre a las listas
productos = lifestore_products #[id_producto, nombre, precio, categoria, inventario]
ventas = lifestore_sales #[id_venta, id_producto, calificacion (1 - 5), fecha, reembolso (1=si , 0=no)]
busquedas = lifestore_searches #[id_busqueda, id_producto]

#Definimos los nombres de cada índice para fácil manejo
id = 0
nom = 1
prec = 2
cat= 3
inv = 4

#print(len(ventas),len(productos), len(busquedas))

#Ordenamos producto por orden alfabético en nombres
#Esto para presentar resultados más amigables a la vista posteriormente
prod = productos[:]
productos = []
 
while prod:
    minimo = prod[0][nom]
    men_may = prod[0]
    for i in prod:
        if i[nom] < minimo:
            minimo = i[nom]
            men_may = i
    productos.append(men_may)
    prod.remove(men_may)

#VentasXProducto
for p in productos:
    count = 0
    for v in ventas:
        if p[0] == v[1]:
            count += 1
    p.append(count)
    
#BusquedasXProducto
for p in productos:
    count = 0
    for b in busquedas:
        if p[0] == b[1]:
            count += 1  
    p.append(count)

#CalificaciónPromedioXProducto
for p in productos:
    suma = 0
    if p[-2] == 0:
        p.append(0.0)
    else:
        for v in ventas:
            if p[id] == v[1]:
                suma += v[2]
        avg = suma/p[-2]
        p.append(avg)
        
#ReembolsoXProducto
for p in productos:
    reemb = 0
    for v in ventas:
        if p[0] == v[1]:
            reemb += v[-1]
    p.append(reemb)

#INDICES DE LISTA PRODUCTOS
ven = -4 #Indice de ventas
bus = -3 #Indice de busquedas
calif = -2 #Indice de calificaciones promedio
reemb = -1 #Indice de reembolso 

#ORDEN BusquedasXProducto Menor a Mayor
bxp = productos[:]
bxp_asc = []

while bxp:
    minimo = bxp[0][bus]
    men_may = bxp[0]
    for i in bxp:
        if i[bus] < minimo:
            minimo = i[bus]
            men_may = i
    bxp_asc.append(men_may)
    bxp.remove(men_may)
    
#ORDEN BusquedasXProducto Mayor a Menor
bxp = productos[:]
bxp_desc = []

while bxp:
    maximo = bxp[0][bus]
    may_men = bxp[0]
    for i in bxp:
        if i[bus] > maximo:
            maximo = i[bus]
            may_men = i
    bxp_desc.append(may_men)
    bxp.remove(may_men)

#ORDEN VentasXProducto Menor a Mayor
vxp = productos[:]
vxp_asc = []
 
while vxp:
    minimo = vxp[0][ven]
    men_may = vxp[0]
    for i in vxp:
        if i[ven] < minimo:
            minimo = i[ven]
            men_may = i
    vxp_asc.append(men_may)
    vxp.remove(men_may)

#ORDEN VentasXProducto Mayor a Menor
vxp = productos[:]
vxp_desc = []
 
while vxp:
    maximo = vxp[0][ven]
    may_men = vxp[0]
    for i in vxp:
        if i[ven] > maximo:
            maximo = i[ven]
            may_men = i
    vxp_desc.append(may_men)
    vxp.remove(may_men)

#ORDEN Ventas(-reembolsos)XProducto Menor a Mayor
vrxp = productos[:]
vrxp_asc = []
 
while vrxp:
    minimo = vrxp[0][ven] - vrxp[0][reemb]
    men_may = vrxp[0]
    for i in vrxp:
        if i[ven] - i[reemb] < minimo:
            minimo = i[ven] - i[reemb]
            men_may = i
    vrxp_asc.append(men_may)
    vrxp.remove(men_may)

#ORDEN Ventas(-reembolsos)XProducto Mayor a Menor
vrxp = productos[:]
vrxp_desc = []
 
while vrxp:
    maximo = vrxp[0][ven] - vrxp[0][reemb]
    may_men = vrxp[0]
    for i in vrxp:
        if i[ven] - i[reemb] > maximo:
            maximo = i[ven] - i[reemb]
            may_men = i
    vrxp_desc.append(may_men)
    vrxp.remove(may_men)
    
#ORDEN CalifPromXProducto Menor a Mayor
cxp = productos[:]
cxp_asc = []
 
while cxp:
    minimo = cxp[0][calif]
    men_may = cxp[0]
    for i in cxp:
        if i[calif] < minimo:
            minimo = i[calif]
            men_may = i
    cxp_asc.append(men_may)
    cxp.remove(men_may)

#ORDEN CalifPromXProducto Mayor a Menor
cxp = productos[:]
cxp_desc = []
 
while cxp:
    maximo = cxp[0][calif]
    may_men = cxp[0]
    for i in cxp:
        if i[calif] > maximo:
            maximo = i[calif]
            may_men = i
    cxp_desc.append(may_men)
    cxp.remove(may_men)

#ORDEN ReembolsoXProducto Menor a Mayor
rxp = productos[:]
rxp_asc = []
 
while rxp:
    minimo = rxp[0][reemb]
    men_may = rxp[0]
    for i in rxp:
        if i[reemb] < minimo:
            minimo = i[reemb]
            men_may = i
    rxp_asc.append(men_may)
    rxp.remove(men_may)

#ORDEN ReembolsoXProducto Mayor a Menor
rxp = productos[:]
rxp_desc = []
 
while rxp:
    maximo = rxp[0][reemb]
    may_men = rxp[0]
    for i in rxp:
        if i[reemb] > maximo:
            maximo = i[reemb]
            may_men = i
    rxp_desc.append(may_men)
    rxp.remove(may_men)

#ORDEN PrecioXProducto Menor a Mayor
pxp = productos[:]
pxp_asc = []
 
while pxp:
    minimo = pxp[0][prec]
    men_may = pxp[0]
    for i in pxp:
        if i[prec] < minimo:
            minimo = i[prec]
            men_may = i
    pxp_asc.append(men_may)
    pxp.remove(men_may)

#ORDEN PrecioXProducto Mayor a Menor
pxp = productos[:]
pxp_desc = []
 
while pxp:
    maximo = pxp[0][prec]
    may_men = pxp[0]
    for i in pxp:
        if i[prec] > maximo:
            maximo = i[prec]
            may_men = i
    pxp_desc.append(may_men)
    pxp.remove(may_men)

#ORDEN InventarioXProducto Menor a Mayor
ixp = productos[:]
ixp_asc = []
 
while ixp:
    minimo = ixp[0][inv]
    men_may = ixp[0]
    for i in ixp:
        if i[inv] < minimo:
            minimo = i[inv]
            men_may = i
    ixp_asc.append(men_may)
    ixp.remove(men_may)

#ORDEN InventarioXProducto Mayor a Menor
ixp = productos[:]
ixp_desc = []
 
while ixp:
    maximo = ixp[0][inv]
    may_men = ixp[0]
    for i in ixp:
        if i[inv] > maximo:
            maximo = i[inv]
            may_men = i
    ixp_desc.append(may_men)
    ixp.remove(may_men)
    
#ORDEN PrecioXProducto Menor a Mayor
pxp = productos[:]
pxp_asc = []
 
while pxp:
    minimo = pxp[0][prec]
    men_may = pxp[0]
    for i in pxp:
        if i[inv] < minimo:
            minimo = i[prec]
            men_may = i
    pxp_asc.append(men_may)
    pxp.remove(men_may)

#ORDEN PrecioXProducto Mayor a Menor
pxp = productos[:]
pxp_desc = []
 
while pxp:
    maximo = pxp[0][prec]
    may_men = pxp[0]
    for i in pxp:
        if i[inv] > maximo:
            maximo = i[prec]
            may_men = i
    pxp_desc.append(may_men)
    pxp.remove(may_men)

#Categorías
categ = []
for p in productos:
    if [p[cat]] not in categ:
        categ.append([p[cat]])

#Ordenamos categorias por orden alfabético 
#Esto para presentar resultados más amigables a la vista posteriormente
ct = categ[:]
categ = []

while ct:
    minimo = ct[0][0]
    men_may = ct[0]
    for i in ct:
        if i[0] < minimo:
            minimo = i[0]
            men_may = i
    categ.append(men_may)
    ct.remove(men_may)

#VentasXCategoría
for c in categ:
    suma = 0
    for p in productos:
        if c[0] == p[cat]:
            suma += p[ven]
    c.append(suma)
    
#BusquedasXCategoría
for c in categ:
    suma = 0
    for p in productos:
        if c[0] == p[cat]:
            suma += p[bus]
    c.append(suma)
    
#CalificacionXCategoria
for c in categ:
    sumac = 0
    sumav = 0
    if c[1] == 0:
        c.append(0.0)
    else:
        for p in productos:
            if c[0] == p[cat] and p[ven]!= 0:
                sumac += p[calif]
                sumav += 1
        c.append(sumac/sumav)
    
#ReembolsoXCategoria
for c in categ:
    suma = 0
    for p in productos:
        if c[0] == p[cat]:
            suma += p[reemb]
    c.append(suma)

#InventarioXCategoria
for c in categ:
    suma = 0
    for p in productos:
        if c[0] == p[cat]:
            suma += p[inv]
    c.append(suma)  


#MontoXCategoria    
for c in categ:
    suma = 0
    for p in productos:
        if c[0] == p[cat]:
            suma += p[prec]
    c.append(suma)  
    
#Monto (-reembolso)XCategoria    
for c in categ:
    suma = 0
    for p in productos:
        if c[0] == p[cat]:
            suma += p[prec] - p[prec]*p[reemb]
    c.append(suma)  

#INDICES DE LISTA CATEG
cnom = 0
cven = 1
cbus = 2
ccalif = 3
creemb = 4
cinv = 5
cmont = 6
cmontr = 7

#ORDEN BusquedasXCategoría Menor a Mayor
bxc = categ[:]
bxc_asc = []

while bxc:
    minimo = bxc[0][cbus]
    men_may = bxc[0]
    for i in bxc:
        if i[cbus] < minimo:
            minimo = i[cbus]
            men_may = i
    bxc_asc.append(men_may)
    bxc.remove(men_may)
    
#ORDEN BusquedasXCategoría Mayor a Menor
bxc = categ[:]
bxc_desc = []

while bxc:
    maximo = bxc[0][cbus]
    may_men = bxc[0]
    for i in bxc:
        if i[cbus] > maximo:
            maximo = i[cbus]
            may_men = i
    bxc_desc.append(may_men)
    bxc.remove(may_men)

#ORDEN VentasXCategoría Menor a Mayor
vxc = categ[:]
vxc_asc = []
 
while vxc:
    minimo = vxc[0][cven]
    men_may = vxc[0]
    for i in vxc:
        if i[cven] < minimo:
            minimo = i[cven]
            men_may = i
    vxc_asc.append(men_may)
    vxc.remove(men_may)

#ORDEN VentasXCategoría Mayor a Menor
vxc = categ[:]
vxc_desc = []
 
while vxc:
    maximo = vxc[0][cven]
    may_men = vxc[0]
    for i in vxc:
        if i[cven] > maximo:
            maximo = i[cven]
            may_men = i
    vxc_desc.append(may_men)
    vxc.remove(may_men)    

#ORDEN Ventas( - reembolsos)XCategoría Menor a Mayor
vrxc = categ[:]
vrxc_asc = []
 
while vrxc:
    minimo = vrxc[0][cven] - vrxc[0][creemb]
    men_may = vrxc[0]
    for i in vrxc:
        if i[cven] - i[creemb] < minimo:
            minimo = i[cven] - i[creemb]
            men_may = i
    vrxc_asc.append(men_may)
    vrxc.remove(men_may)

#ORDEN Ventas(- reembolsos)XCategoría Mayor a Menor
vrxc = categ[:]
vrxc_desc = []
 
while vrxc:
    maximo = vrxc[0][cven] - vrxc[0][creemb]
    may_men = vrxc[0]
    for i in vrxc:
        if i[cven] - i[creemb] > maximo:
            maximo = i[cven] - i[creemb]
            may_men = i
    vrxc_desc.append(may_men)
    vrxc.remove(may_men)    

#ORDEN CalificaciónXCategoría Menor a Mayor
cxc = categ[:]
cxc_asc = []

while cxc:
    minimo = cxc[0][ccalif]
    men_may = cxc[0]
    for i in cxc:
        if i[cbus] < minimo:
            minimo = i[ccalif]
            men_may = i
    cxc_asc.append(men_may)
    cxc.remove(men_may)
    
#ORDEN CalificaciónXCategoría Mayor a Menor
cxc = categ[:]
cxc_desc = []

while cxc:
    maximo = cxc[0][ccalif]
    may_men = cxc[0]
    for i in cxc:
        if i[ccalif] > maximo:
            maximo = i[ccalif]
            may_men = i
    cxc_desc.append(may_men)
    cxc.remove(may_men)
    
#ORDEN ReembolsoXCategoría Menor a Mayor
rxc = categ[:]
rxc_asc = []

while rxc:
    minimo = rxc[0][creemb]
    men_may = rxc[0]
    for i in rxc:
        if i[creemb] < minimo:
            minimo = i[creemb]
            men_may = i
    rxc_asc.append(men_may)
    rxc.remove(men_may)
    
#ORDEN ReembolsoXCategoría Mayor a Menor
rxc = categ[:]
rxc_desc = []

while rxc:
    maximo = rxc[0][creemb]
    may_men = rxc[0]
    for i in rxc:
        if i[creemb] > maximo:
            maximo = i[creemb]
            may_men = i
    rxc_desc.append(may_men)
    rxc.remove(may_men)

#ORDEN InventarioXCategoría Menor a Mayor
ixc = categ[:]
ixc_asc = []
 
while ixc:
    minimo = ixc[0][cinv]
    men_may = ixc[0]
    for i in ixc:
        if i[cinv] < minimo:
            minimo = i[cinv]
            men_may = i
    ixc_asc.append(men_may)
    ixc.remove(men_may)

#ORDEN InventarioXCategoría Mayor a Menor
ixc = categ[:]
ixc_desc = []
 
while ixc:
    maximo = ixc[0][cinv]
    may_men = ixc[0]
    for i in ixc:
        if i[cinv] > maximo:
            maximo = i[cinv]
            may_men = i
    ixc_desc.append(may_men)
    ixc.remove(may_men)    
    
#ORDEN MontoXCategoría Menor a Mayor
mxc = categ[:]
mxc_asc = []
 
while mxc:
    minimo = mxc[0][cmont]
    men_may = mxc[0]
    for i in mxc:
        if i[cmont] < minimo:
            minimo = i[cmont]
            men_may = i
    mxc_asc.append(men_may)
    mxc.remove(men_may)

#ORDEN MontoXCategoría Mayor a Menor
mxc = categ[:]
mxc_desc = []
 
while mxc:
    maximo = mxc[0][cmont]
    may_men = mxc[0]
    for i in mxc:
        if i[cmont] > maximo:
            maximo = i[cmont]
            may_men = i
    mxc_desc.append(may_men)
    mxc.remove(may_men)
    
#ORDEN Monto(-reembolso)XCategoría Menor a Mayor
mrxc = categ[:]
mrxc_asc = []
 
while mrxc:
    minimo = mrxc[0][cmontr]
    men_may = mrxc[0]
    for i in mrxc:
        if i[cmontr] < minimo:
            minimo = i[cmontr]
            men_may = i
    mrxc_asc.append(men_may)
    mrxc.remove(men_may)

#ORDEN Monto(-reembolso)XCategoría Mayor a Menor
mrxc = categ[:]
mrxc_desc = []
 
while mrxc:
    maximo = mrxc[0][cmontr]
    may_men = mrxc[0]
    for i in mrxc:
        if i[cmontr] > maximo:
            maximo = i[cmontr]
            may_men = i
    mrxc_desc.append(may_men)
    mrxc.remove(may_men)    

#Ventas y Monto vendido por mes y reembolsos
meses = []

for m in range(1,13):
    if m == 1:
        nmes = "Enero"
    elif m == 2:
        nmes = "Febrero"
    elif m == 3:
        nmes = "Marzo"
    elif m == 4:
        nmes = "Abril"
    elif m == 5:
        nmes = "Mayo"
    elif m == 6:
        nmes = "Junio"
    elif m == 7:
        nmes = "Julio"
    elif m == 8:
        nmes = "Agosto"
    elif m == 9:
        nmes = "Septiembre"
    elif m == 10:
        nmes = "Octubre"
    elif m == 11:
        nmes = "Noviembre"
    elif m == 12:
        nmes = "Diciembre"
    vxm = 0 #ventas x mes
    montxm = 0 #monto x mes
    reembxm = 0 #reembolsos x mes
    montrxm = 0 # monto reembolsado x mes
    for v in ventas:
        if int(v[3][3:5]) == m:
            vxm += 1
            reembxm += v[4]
            for p in productos:
                if p[id] ==v[1]:
                    montxm += p[prec]
                    montrxm += p[prec]*v[4]
    meses.append([m,nmes, vxm, montxm, reembxm, montrxm])
    
#ORDEN VentasXFecha Menor a Mayor
vxf = meses[:]
vxf_asc = []
 
while vxf:
    minimo = vxf[0][2] - vxf[0][4]
    men_may = vxf[0]
    for i in vxf:
        if i[2] - i[4] < minimo:
            minimo = i[2] - i[4]
            men_may = i
    vxf_asc.append(men_may)
    vxf.remove(men_may)

#ORDEN VentasXFecha Mayor a Menor
vxf = meses[:]
vxf_desc = []
 
while vxf:
    maximo = vxf[0][2] - vxf[0][4]
    may_men = vxf[0]
    for i in vxf:
        if i[2] - i[4] > maximo:
            maximo = i[2] - i[4]
            may_men = i
    vxf_desc.append(may_men)
    vxf.remove(may_men)    

#ORDEN Ventas( - reembolsos)XFecha Menor a Mayor
vrxf = meses[:]
vrxf_asc = []
 
while vrxf:
    minimo = vrxf[0][2] - vrxf[0][4]
    men_may = vrxf[0]
    for i in vrxf:
        if i[2] - i[4] < minimo:
            minimo = i[2] - i[4]
            men_may = i
    vrxf_asc.append(men_may)
    vrxf.remove(men_may)

#ORDEN Ventas(- reembolsos)XFecha Mayor a Menor
vrxf = meses[:]
vrxf_desc = []
 
while vrxf:
    maximo = vrxf[0][2] - vrxf[0][4]
    may_men = vrxf[0]
    for i in vrxf:
        if i[2] - i[4] > maximo:
            maximo = i[2] - i[4]
            may_men = i
    vrxf_desc.append(may_men)
    vrxf.remove(may_men)    

####################################################_INICIO DE SESION_######################################################


#Definimos al usuario administrador
admin = [["EMTECH","proyecto1"]] 

#Definimos los usuarios iniciales con sus respectivas contraseñas
acceso = [["Pepillo", "pp909316"], ["Javier","emtech123"]]

#Bienvenida
print("¡Bienvenido¡ \n")
#Indicadora de inicio de sesión 
sesion = 0
#Indicador del tipo de usuario, 0 - común, 1 - administrador
usr = 0

#Empezamos a pedir acceso a usuarios
while sesion == 0: 
    print("Para acceder necesita ingresar su usuario y su contraseña. \n¿Cuenta con usuario y contraseña registrados? \n 1 - si \n 2 - no\n")
    
    #Recibimos cuenta existente o nueva del usuario
    usuario = input("Ingrese el número que corresponde a su respuesta: ")
    
    #Para cuentas existentes
    if usuario == "1":
      u = input("\nIngrese su usuario: ")
      for user in acceso:
        if u == user[0] or u == admin[0][0]:
          #sesion = 1
          print("\nBienvenido", u)
          p = input("Ingresa tu contraseña: ")
          if ((p == user[1] and u== user[0]) or (p == admin[0][1] and u == admin[0][0])):
            print("\nHas iniciado sesión con éxito\n")
            sesion =1
            if u == admin[0][0]:
              print("Esta es una cuenta de administrador\n")
              usr = 1            
            break
          else:
            i = 0
            while ((p != user[1] and u == user[0]) or (p != admin[0][1] and u == admin[0][0])) and i < 3:
              i += 1
              print("\n Quedan ", str(4-i)," intentos...")
              p = input("Contraseña inválida, porfavor intente denuevo: ")
            if i >= 3 and ((p != user[1] and u == user[0]) or (p != admin[0][1] and u == admin[0][0])):
              print("\nHas alcanzado el número máximo de intentos, vuelve a iniciar sesión.\n\n")
              break
            else: 
              print("\nHas iniciado sesión con éxito\n")
              sesion = 1
              if u == admin[0][0]:
                print("Esta es una cuenta de administrador\n")
                usr = 1
              break
          
      if u != user[0] and u != admin[0][0]: #sesion == 0
        print("No se encontró el usuario, intente denuevo o cree un nuevo perfil.\n")
    
    #Para cuentas nuevas      
    elif usuario == "2":
      u = input("\nRegistre nuevo usuario: ")
      #sesion == 0
      for user in acceso:
        if u == user[0] or u == admin[0][0]:
          print("Ya existe usuario ingresado, intente nuevamente.\n")
          #sesion = 1
          break
      if u != user[0] and u != admin[0][0]: #sesion == 0:
        p = input("Asigne contraseña del nuevo usuario: ")
        pp = input("Confirme su contraseña: ")
        if pp == p:
          print("\nUsuario ", u, " registrado correctamente, sesión iniciada.\n\n")
          sesion = 1
          acceso.append([u,p])
          
        else:
          i = 0
          while p != pp and i < 3:
            i += 1
            print("\n Las contraseñas no coinciden.\n Quedan ", str(4-i), " intentos...")
            p = input("\n Asigne contraseña del nuevo usuario: ")
            pp = input("Confirme su contraseña: ")
          if i >= 3 and p != pp:
            print("\n No se puede registrar el usuario, vuelva a intentarlo. \n \n")
          else:
            print("\n Usuario ", u, " registrado correctamente, sesión iniciada con éxito.")
            sesion = 1
            acceso.append([u,p])
    
    else:
      print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")


#Acciones para usuarios comunes
if sesion == 1 and usr == 0:
    while sesion == 1:
        print("\nMENÚ INICIAL\n\nReporte por categoría:\n")
        for i in range(0,len(vxc_desc)):
            print(str(i+1) + " - " + vxc_desc[i][0] + "\n\tVentas: " + str(vxc_desc[i][cven])  + "\n")
        #Recibimos eleccion de usuario
        eleccion = input("Ingrese el número de la categoría que le interese para acceder.\nPresione '0' para salir.\n\nSelección: ")
        
        if eleccion == "0":
            print("Cerrando sesión...")
            sesion = 0
        
        elif eleccion == "1" or eleccion == "2" or eleccion == "3" or eleccion == "4" or eleccion == "5" or eleccion == "6" or eleccion == "7" or eleccion == "8" :
            for p in range(0, len(vxp_desc)):
                if productos[p][cat] == vxc_desc[int(eleccion)-1][0]:
                    print("PRODUCTO: "+ productos[p][nom] + "\n\tVENTAS: " + str(productos[p][ven]))
            permanecer = input("\n¿Desea volver al menú o salir?\n0 - salir\n1 - volver al menú\n\nIngrese una opción válida: ")
            if permanecer == "0":
                print("Cerrando sesión...")
                sesion = 0
            elif permanecer == "1":
                continue
            else:
                i = 0
                while (permanecer != "0" and permanecer != "1") and i < 3:
                  i += 1
                  print("\n Quedan ", str(4-i)," intentos...")
                  permanecer = input("Intente denuevo con una opción válida: ")
                if i >= 3 and (permanecer != "0" and permanecer != "1"):
                  print("\nHas alcanzado el número máximo de intentos, vuelve a iniciar sesión.\n\n")
                  break
                elif permanecer == "0":
                          print("Cerrando sesión...")
                          sesion = 0
                          break
                else:
                    continue 
        else:
            i = 0
            while (eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4" and eleccion != "5" and eleccion != "6" and eleccion != "7" and eleccion != "8") and i < 3:
              i += 1
              print("\n Quedan ", str(4-i)," intentos...")
              eleccion = input("Intente denuevo con una opción válida: ")
            if i >= 3 and (eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4" and eleccion != "5" and eleccion != "6" and eleccion != "7" and eleccion != "8"):
              print("\nHas alcanzado el número máximo de intentos, vuelve a iniciar sesión.\n\n")
              break
            else:
                for p in range(0, len(vxp_desc)):
                    if productos[p][cat] == vxc_desc[int(eleccion)-1][0]:
                        print("PRODUCTO: "+ productos[p][nom] + "\n\tVENTAS: " + str(productos[p][ven]))
                permanecer = input("\n¿Desea volver al menú o salir?\n0 - salir\n1 - volver al menú\n\nIngrese una opción válida: ")
                if permanecer == "0":
                    print("Cerrando sesión...")
                    sesion = 0
                    break
                elif permanecer == "1":
                    continue
                else:
                    i = 0
                    while (permanecer != "0" and permanecer != "1") and i < 3:
                      i += 1
                      print("\n Quedan ", str(4-i)," intentos...")
                      permanecer = input("Intente denuevo con una opción válida: ")
                    if i >= 3 and (permanecer != "0" and permanecer != "1"):
                      print("\nHas alcanzado el número máximo de intentos, vuelve a iniciar sesión.\n\n")
                      break
                    elif permanecer == "0":
                        print("Cerrando sesión...")
                        sesion = 0
                        break
                    else:
                        continue
#Variable para Tops
z1 = 50 
z2 = 20
#Acciones para administradores
if sesion == 1 and usr == 1:
  while sesion == 1:
    print("\nMENÚ INICIAL\n\nReportes:\n\n1 - Por categorías\n2 - Por fecha\n3 - Por producto")
    eleccion1 = input("Ingrese el número de la opción que desee.\nPresione '0' para salir\n\nSelección: ")
    if eleccion1 == "0":
        print("Cerrando sesión...\n")
        sesion = 0
#1
    elif eleccion1 == "1":
        print("POR CATEGORÍAS: \n\n1 - Ventas brutas x Categoría (sin incluir reembolsos)\n2 - Ventas netas x Categoría (incluyendo reembolsos)\n3 - Búsquedas x Categoría\n4 - Calificaciones x Categoría\n5 - Reembolsos x Categoría\n6 - Inventario x Categoría\n7 - Ingresos Brutos x Categoría\n8 - Ingresos Netos x Categoría")
        eleccion2 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
        if eleccion2 == "0":
            print("Regresando...\n")
#1.1
        elif eleccion2 == "1":
            print("VENTAS BRUTAS X CATEGORÍA: \n\n1 - Mayores ventas brutas\n2 - Menores ventas brutas")
            eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
            if eleccion3 == "0":
                print("Regresando...\n")
#1.1.1
            elif eleccion3 =="1":
                print("MAYORES VENTAS BRUTAS X CATEGORÍA: \n")
                c = 0
                for v in vxc_desc:
                    c += 1
                    print(c, "Categoría: ",v[cnom], "\n\tVentas Brutas: ", v[cven], "\n\t\tMonto Vendido: ", v[cmont],"\n\t\t\tCalif. promedio: ", v[ccalif],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#1.1.2
            elif eleccion3 == "2":
                print("MENORES VENTAS BRUTAS X CATEGORÍA: \n")
                c=0
                for v in vxc_asc:
                    c+=1
                    print(c,"Categoría: ",v[cnom], "\n\tVentas Brutas: ", v[cven] , "\n\t\tMonto Vendido: ", v[cmont],"\n\t\t\tCalif. promedio: ", v[ccalif],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
            else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
                 
#1.2                
        elif eleccion2 == "2":
            print("VENTAS NETAS X CATEGORÍA: \n\n1 - Mayores ventas netas\n2 - Menores ventas netas")
            eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
            if eleccion3 == "0":
                print("Regresando...\n")
#1.2.1
            elif eleccion3 == "1":
                print("MAYORES VENTAS NETAS X CATEGORÍA: \n")
                c=0
                for v in vrxc_desc:
                    c+=1
                    print(c,"Categoría: ",v[cnom], "\n\tVentas Netas: ", v[cven]-v[creemb], "\n\t\tInventario: ", v[cinv], "\n\t\t\tMonto Vendido: ", v[cmontr], "\n\t\t\t\tCalif. promedio: ", v[ccalif],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#1.2.2
            elif eleccion3 == "2":
                print("MENORES VENTAS NETAS X CATEGORÍA: \n")
                c=0
                for v in vrxc_asc:
                    c+=1
                    print(c,"Categoría: ",v[cnom], "\n\tVentas Netas: ", v[cven]-v[creemb], "\n\t\tInventario: ", v[cinv], "\n\t\t\tMonto Vendido: ", v[cmontr], "\n\t\t\t\tCalif. promedio: ", v[ccalif],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
            else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#1.3
        elif eleccion2 == "3":
            print("BÚSQUEDAS X CATEGORÍA: \n\n1 - Mayores busquedas\n2 - Menores busquedas")
            eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
            if eleccion3 == "0":
                print("Regresando...\n")
#1.3.1
            elif eleccion3 == "1":
                print("MAYORES BUSQUEDAS X CATEGORÍA: \n")
                c=0
                for b in bxc_desc:
                    c+=1
                    print(c,"Categoría: ",b[cnom], "\n\tBusquedas: ", b[cbus], "\n\t\tVentas: ", b[cven],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#1.3.2
            elif eleccion3 == "2":
                print("MENORES BUSQUEDAS X CATEGORÍA: \n")
                c=0 
                for b in bxc_asc:
                    c+=1
                    print(c,"Categoría: ",b[cnom], "\n\tBusquedas: ", b[cbus], "\n\t\tVentas: ", b[cven],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
            else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#1.4
        elif eleccion2 == "4":
            print("CALIFICACIONES X CATEGORÍA: \n\n1 - Mejores Calificaciones\n2 - Peores Calificaciones")                
            eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
            if eleccion3 == "0":
                print("Regresando...\n")
#1.4.1
            elif eleccion3 =="1":
                print("MEJORES CALIFICACIONES X CATEGORÍA: \n")
                c=0
                for v in cxc_desc:
                    c+=1
                    print(c,"Categoría: ",v[cnom], "\n\tCalificación: ", v[ccalif], "\n\t\tVentas Brutas: ", v[cven], "\n\t\t\tReembolsos: ", v[creemb],"\n\t\t\t\tVentas Netas: ", v[cven]-v[creemb],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#1.4.2
            elif eleccion3 =="2":
                print("PEORES CALIFICACIONES X CATEGORÍA: \n")
                c=0
                for v in cxc_asc:
                    c+=1
                    print(c,"Categoría: ",v[cnom], "\n\tCalificación: ", v[ccalif], "\n\t\tVentas Brutas: ", v[cven], "\n\t\t\tReembolsos: ", v[creemb],"\n\t\t\t\tVentas Netas: ", v[cven]-v[creemb],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
            else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#1.5
        elif eleccion2 == "5":
             print("REEMBOLSOS X CATEGORÍA: \n\n1 - Mayores reembolsos\n2 - Menores reembolsos")
             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
             if eleccion3 == "0":
                print("Regresando...\n")
#1.5.1               
             elif eleccion3 == "1":
                print("MAYORES REEMBOLSOS X CATEGORÍA: \n")
                c=0
                for v in rxc_desc:
                    c+=1
                    print(c,"Categoría: ",v[cnom], "\n\tReembolsos: ", v[creemb],"\n\t\tCalificación: ",v[ccalif], "\n\t\t\tVentas Brutas: ", v[cven],"\n\t\t\t\tVentas Netas: ", v[cven]-v[creemb],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#1.5.2              
             elif eleccion3 == "2":
                print("MENORES REEMBOLSOS X CATEGORÍA: \n")
                c=0
                for v in rxc_asc:
                    c+=1
                    print(c,"Categoría: ",v[cnom], "\n\tReembolsos: ", v[creemb],"\n\t\tCalificación: ",v[ccalif], "\n\t\t\tVentas Brutas: ", v[cven],"\n\t\t\t\tVentas Netas: ", v[cven]-v[creemb],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
             else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#1.6
        elif eleccion2 == "6":
             print("INVENTARIO X CATEGORÍA: \n\n1 - Mayor inventario\n2 - Menor inventario")
             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
             if eleccion3 == "0":
                print("Regresando...\n")
#1.6.1               
             elif eleccion3 == "1":
                print("MAYOR INVENTARIO X CATEGORÍA: \n")
                c=0
                for v in ixc_desc:
                    c+=1
                    print(c,"Categoría: ",v[cnom], "\n\tInventario: ", v[cinv],"\n\t\tCalificación: ", v[ccalif],"\n\t\t\tVentas Netas: ", v[cven]-v[creemb],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#1.6.2              
             elif eleccion3 == "2":
                print("MENOR INVENTARIO X CATEGORÍA: \n")
                c=0
                for v in ixc_asc:
                    c+=1
                    print(c,"Categoría: ",v[cnom], "\n\tInventario: ", v[inv],"\n\t\tCalificación: ",v[ccalif],"\n\t\t\tVentas Netas: ", v[cven]-v[creemb],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
             else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#1.7
        elif eleccion2 == "7":
             print("INGRESOS BRUTOS X CATEGORÍA: \n\n1 - Mayores ingresos brutos\n2 - Menores ingresos brutos")
             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
             if eleccion3 == "0":
                print("Regresando...\n")
#1.7.1               
             elif eleccion3 == "1":
                print("MAYORES INGRESOS BRUTOS X CATEGORÍA: \n")
                c=0
                for v in mxc_desc:
                    c+=1
                    print(c,"Categoría: ",v[cnom], "\n\tIngresos Brutos: ", v[cmont], "\n\t\tVentas Brutas: ", v[cven],"\n\t\t\tReembolsos: ", v[creemb],"\n\t\t\t\tVentas Netas: ", v[cven]-v[creemb],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#1.7.2              
             elif eleccion3 == "2":
                print("MENORES INGRESOS BRUTOS X CATEGORÍA: \n")
                c=0
                for v in mxc_asc:
                    c+=1
                    print(c,"Categoría: ",v[cnom], "\n\tIngresos Brutos: ", v[cmont], "\n\t\tVentas Brutas: ", v[cven],"\n\t\t\tReembolsos: ", v[creemb],"\n\t\t\t\tVentas Netas: ", v[cven]-v[creemb],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
             else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#1.8
        elif eleccion2 == "8":
             print("INGRESOS NETOS X CATEGORÍA: \n\n1 - Mayores ingresos netos\n2 - Menores ingresos netos")
             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
             if eleccion3 == "0":
                print("Regresando...\n")
#1.8.1               
             elif eleccion3 == "1":
                print("MAYORES INGRESOS NETOS X CATEGORÍA: \n")
                c=0
                for v in mrxc_desc:
                    c+=1
                    print(c,"Categoría: ",v[cnom], "\n\tIngresos Netos: ", v[cmontr], "\n\t\tVentas Netas: ", v[cven]-v[creemb],"\n\t\tCalificación: ",v[ccalif],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#1.8.2              
             elif eleccion3 == "2":
                print("MENORES INGRESOS NETOS X CATEGORÍA: \n")
                c=0
                for v in mrxc_asc:
                    c+=1
                    print(c,"Categoría: ",v[cnom], "\n\tIngresos Netos: ", v[cmontr], "\n\t\tVentas Netas: ", v[cven]-v[creemb],"\n\t\tCalificación: ",v[ccalif],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
             else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
                 
                 
            
                
                
                
                

#2
    elif eleccion1 == "2":
        print("POR FECHA: \n\n1 - Ventas brutas x Fecha (sin incluir reembolsos)\n2 - Ventas netas x Fecha (incluyendo reembolsos)")
        eleccion2 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
        if eleccion2 == "0":
            print("Regresando...\n")
#2.1       
        elif eleccion2 == "1":
            print("VENTAS BRUTAS X FECHA: \n\n1 - Ventas brutas x mes\n2 - Mayores ventas brutas\n3 - Menores ventas brutas")
            eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
            if eleccion3 == "0":
                print("Regresando...\n")        
#2.1.1 
            elif eleccion3 == "1":
                print("VENTAS BRUTAS X MES: \n")
                vt = 0 #Ventas Brutas Totales
                it = 0 #Ingresos Brutos Totales
                c=0
                for mm in meses:
                    c+=1
                    print(c,"Mes: ",mm[1], "\n\tVentas Brutas: ", mm[2], "\n\t\tIngresos Brutos: ", mm[3],"\n")
                    vt += mm[2]
                    it += mm[3]
                print("Ventas Brutas Totales: ",vt,"\nIngresos Brutos Totales: ",it,"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#2.1.2                  
            elif eleccion3 == "2":
                print("MAYORES VENTAS BRUTAS X MES: \n")
                vt = 0 #Ventas Brutas Totales
                it = 0 #Ingresos Brutos Totales
                c=0
                for mm in vxf_desc:
                    c+=1
                    print(c,"Mes: ",mm[1], "\n\tVentas Brutas: ", mm[2], "\n\t\tIngresos Brutos: ", mm[3],"\n")
                    vt += mm[2]
                    it += mm[3]
                print("Ventas Brutas Totales: ",vt,"\nIngresos Brutos Totales: ",it,"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#2.1.3                                     
            elif eleccion3 == "3":
                print("MENORES VENTAS BRUTAS X MES: \n")
                vt = 0 #Ventas Brutas Totales
                it = 0 #Ingresos Brutos Totales
                c=0
                for mm in vxf_asc:
                    c+=1
                    print(c,"Mes: ",mm[1], "\n\tVentas Brutas: ", mm[2], "\n\t\tIngresos Brutos: ", mm[3],"\n")
                    vt += mm[2]
                    it += mm[3]
                print("Ventas Brutas Totales: ",vt,"\nIngresos Brutos Totales: ",it,"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
            else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#2.2       
        elif eleccion2 == "2":
            print("VENTAS NETAS X FECHA: \n\n1 - Ventas netas x mes\n2 - Mayores ventas netas\n3 - Menores ventas netas")
            eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
            if eleccion3 == "0":
                print("Regresando...\n")        
#2.2.1 
            elif eleccion3 == "1":
                print("VENTAS NETAS X MES: \n")
                vrt = 0 #Ventas Netas Totales
                irt = 0 #Ingresos Netos Totales
                c=0
                for mm in meses:
                    c+=1
                    print(c,"Mes: ",mm[1], "\n\tVentas Netas: ", mm[2]-mm[4] , "\n\t\tIngresos Netos: ", mm[3]-mm[5],"\n")
                    vrt += mm[2]-mm[4]
                    irt += mm[3]-mm[5]
                print("Ventas Netas Totales: ",vrt,"\nIngresos Netos Totales: ",irt,"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#2.2.2                  
            elif eleccion3 == "2":
                print("MAYORES VENTAS NETAS X MES: \n")
                vrt = 0 #Ventas Netas Totales
                irt = 0 #Ingresos Netos Totales
                c=0
                for mm in vrxf_desc:
                    c+=1
                    print(c,"Mes: ",mm[1], "\n\tVentas Netas: ", mm[2]-mm[4], "\n\t\tIngresos Netos: ", mm[3]-mm[5],"\n")
                    vrt += mm[2]-mm[4]
                    irt += mm[3]-mm[5]
                print("Ventas Netas Totales: ",vrt,"\nIngresos Netos Totales: ",irt,"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#2.2.3                                     
            elif eleccion3 == "3":
                print("MENORES VENTAS NETAS X MES: \n")
                vrt = 0 #Ventas Netas Totales
                irt = 0 #Ingresos Netos Totales
                c=0
                for mm in vrxf_desc:
                    c+=1
                    print(c,"Mes: ",mm[1], "\n\tVentas Netas: ", mm[2]-mm[4], "\n\t\tIngresos Netos: ", mm[3]-mm[5],"\n")
                    vrt += mm[2]-mm[4]
                    irt += mm[3]-mm[5]
                print("Ventas Netas Totales: ",vrt,"\nIngresos Netos Totales: ",irt,"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
            else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
                
#3        
    elif eleccion1 == "3":
        print("POR PRODUCTO: \n\n1 - Ventas brutas x Producto (sin incluir reembolsos)\n2 - Ventas netas x Producto (incluyendo reembolsos)\n3 - Búsquedas x Producto\n4 - Calificaciones x Producto\n5 - Reembolsos x Producto\n6 - Inventario x Producto\n7 - Precio x Producto")
        eleccion2 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
        if eleccion2 == "0":
            print("Regresando...\n")
#3.1
        elif eleccion2 == "1":
            print("VENTAS BRUTAS X PRODUCTO: \n\n1 - Mayores ventas brutas\n2 - Menores ventas brutas")
            eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
            if eleccion3 == "0":
                print("Regresando...\n")
#3.1.1
            elif eleccion3 =="1":
                print(str(z1),"MAYORES VENTAS BRUTAS X PRODUCTO: \n")
                c=0
                for p in vxp_desc[:z1]:
                    c+=1
                    print(c,"Producto: ",p[nom], "\n\tVentas Brutas: ", p[ven],"\n\t\tPrecio: ", p[prec],"\n\t\t\tCalificación: ",p[calif], "\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#3.1.2
            elif eleccion3 == "2":
                print(str(z1),"MENORES VENTAS BRUTAS X PRODUCTO: \n")
                c=0
                for p in vxp_asc[:z1]:
                    c+=1
                    print(c,"Producto: ",p[nom], "\n\tVentas Brutas: ", p[ven], "\n\t\tPrecio: ", p[prec],"\n\t\t\tCalificación: ",p[calif], "\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
            else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#3.2                
        elif eleccion2 == "2":
            print("VENTAS NETAS X PRODUCTO: \n\n1 - Mayores ventas netas\n2 - Menores ventas netas")
            eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
            if eleccion3 == "0":
                print("Regresando...\n")
#3.2.1
            elif eleccion3 == "1":
                print(str(z1),"MAYORES VENTAS NETAS X PRODUCTO: \n")
                c=0
                for p in vrxp_desc[:z1]:
                    c+=1
                    print(c,"Producto: ",p[nom], "\n\tVentas Netas: ", p[ven] - p[reemb], "\n\t\tInventario: ", p[inv],"\n\t\t\tPrecio: ", p[prec],"\n\t\t\t\tCalificación: ",p[calif], "\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#3.2.2
            elif eleccion3 == "2":
                print(str(z1),"MENORES VENTAS NETAS X PRODUCTO: \n")
                c=0
                for p in vrxp_asc[:z1]:
                    c+=1
                    print(c,"Producto: ",p[nom], "\n\tVentas Netas: ", p[ven]-p[reemb], "\n\t\tInventario: ", p[inv],"\n\t\t\tPrecio: ", p[prec],"\n\t\t\t\tCalificación: ",p[calif], "\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
            else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#3.3
        elif eleccion2 == "3":
            print("BÚSQUEDAS X PRODUCTO: \n\n1 - Mayores busquedas\n2 - Menores busquedas")
            eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
            if eleccion3 == "0":
                print("Regresando...\n")
#3.3.1
            elif eleccion3 == "1":
                print(str(z1),"MAYORES BUSQUEDAS X PRODUCTO: \n")
                c=0
                for b in bxp_desc[:z1]:
                    c+=1
                    print(c,"Producto: ",b[nom], "\n\tBusquedas: ", b[bus], "\n\t\tVentas: ", b[ven],"\n\t\t\tCalificación: ", b[calif],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#3.3.2
            elif eleccion3 == "2":
                print(str(z1),"MENORES BUSQUEDAS X PRODUCTO: \n")
                c=0
                for b in bxp_asc[:z1]:
                    c+=1
                    print(c,"Producto: ",b[nom], "\n\tBusquedas: ", b[bus], "\n\t\tVentas: ", b[ven],"\n\t\t\tCalificación: ", b[calif],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
            else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#3.4
        elif eleccion2 == "4":
            print("CALIFICACIONES X PRODUCTO: \n\n1 - Mejores Calificaciones\n2 - Peores Calificaciones")                
            eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
            if eleccion3 == "0":
                print("Regresando...\n")
#3.4.1
            elif eleccion3 =="1":
                print(str(z2),"MEJORES CALIFICACIONES X PRODUCTO: \n")
                c=0
                for v in cxp_desc[:z2]:
                    c+=1
                    print(c,"Producto: ",v[nom], "\n\tCalificación: ", v[calif], "\n\t\tVentas Brutas: ", v[ven], "\n\t\t\tReembolsos: ", v[reemb],"\n\t\t\t\tVentas Netas: ", v[ven]-v[reemb],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#3.4.2
            elif eleccion3 =="2":
                print(str(z2),"PEORES CALIFICACIONES X PRODUCTO: \n")
                c=0
                for v in cxp_asc[:z2]:
                    c+=1
                    print(c,"Producto: ",v[nom], "\n\tCalificación: ", v[calif], "\n\t\tVentas Brutas: ", v[ven], "\n\t\t\tReembolsos: ", v[reemb],"\n\t\t\t\tVentas Netas: ", v[ven]-v[reemb],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
            else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#3.5
        elif eleccion2 == "5":
             print("REEMBOLSOS X PRODUCTO: \n\n1 - Mayores reembolsos\n2 - Menores reembolsos")
             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
             if eleccion3 == "0":
                print("Regresando...\n")
#3.5.1               
             elif eleccion3 == "1":
                print(str(z1),"MAYORES REEMBOLSOS X PRODUCTO: \n")
                c=0
                for v in rxp_desc[:z1]:
                    c+=1
                    print(c,"Producto: ",v[nom], "\n\tReembolsos: ", v[reemb],"\n\t\tCalificación: ",v[calif], "\n\t\t\tVentas Brutas: ", v[ven],"\n\t\t\t\tVentas Netas: ", v[ven]-v[reemb],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#3.5.2              
             elif eleccion3 == "2":
                print(str(z1),"MENORES REEMBOLSOS X PRODUCTO: \n")
                c=0
                for v in rxp_asc[:z1]:
                    c+=1
                    print(c,"Producto: ",v[nom], "\n\tReembolsos: ", v[reemb],"\n\t\tCalificación: ",v[calif], "\n\t\t\tVentas Brutas: ", v[ven],"\n\t\t\t\tVentas Netas: ", v[ven]-v[reemb],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
             else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
#3.6
        elif eleccion2 == "6":
             print("INVENTARIO X PRODUCTO: \n\n1 - Mayor inventario\n2 - Menor inventario")
             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
             if eleccion3 == "0":
                print("Regresando...\n")
#3.6.1               
             elif eleccion3 == "1":
                print(str(z1),"MAYOR INVENTARIO X PRODUCTO: \n")
                c=0
                for v in ixp_desc[:z1]:
                    c+=1
                    print(c,"Producto: ",v[nom], "\n\tInventario: ", v[inv],"\n\t\tCalificación: ", v[calif],"\n\t\t\tVentas Netas: ", v[ven]-v[reemb],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#3.6.2              
             elif eleccion3 == "2":
                print(str(z1),"MENOR INVENTARIO X PRODUCTO: \n")
                c=0
                for v in ixp_asc[:z1]:
                    c+=1
                    print(c,"Producto: ",v[nom], "\n\tInventario: ", v[inv],"\n\t\tCalificación: ",v[calif],"\n\t\t\tVentas Netas: ", v[ven]-v[reemb],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
             else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#3.7
        elif eleccion2 == "7":
             print("PRECIOS X PRODUCTO: \n\n1 - Mayores precios\n2 - Menores precios")
             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
             if eleccion3 == "0":
                print("Regresando...\n")
#3.7.1               
             elif eleccion3 == "1":
                print(str(z1),"MAYORES PRECIOS X PRODUCTO: \n")
                c=0
                for v in pxp_desc[:z1]:
                    c+=1
                    print(c,"Producto: ",v[nom], "\n\tPrecio: ", v[prec], "\n\t\tVentas Brutas: ", v[ven],"\n\t\t\tReembolsos: ", v[reemb],"\n\t\t\t\tVentas Netas: ", v[ven]-v[reemb],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#3.7.2              
             elif eleccion3 == "2":
                print(str(z1),"MENORES PRECIOS X PRODUCTO: \n")
                c=0
                for v in pxp_asc[:z1]:
                    c+=1
                    print(c,"Producto: ",v[nom], "\n\tPrecio: ", v[prec], "\n\t\tVentas Brutas: ", v[ven],"\n\t\t\tReembolsos: ", v[reemb],"\n\t\t\t\tVentas Netas: ", v[ven]-v[reemb],"\n")
                permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
                if permanecer == "0":
                    sesion = 0
                elif permanecer == "1":
                    continue
                else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
             else:
                 print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
        
        else:
            print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            
            
    else:
        print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
            




