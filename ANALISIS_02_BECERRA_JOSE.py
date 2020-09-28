# -*- coding: utf-8 -*-
import csv
#Leemos y almacenamos la base de datos de Synergy Logistics 
dbl = []
with open("synergy_logistics_database.csv", "r", encoding = 'utf-8-sig') as archivo_csv:
    lector = csv.DictReader(archivo_csv) 
    for linea in lector:
        dbl.append(linea)


#3. ANALISIS POR PAIS
#Pais que consideraremos como pagador en importacion/exportacion
def situacion(imports_exports):
    if imports_exports == "Exports":
        situacion = "origin"
    elif imports_exports == "Imports":
        situacion = "destination"
    else: 
        return "ARGUMENTO INCORRECTO"
    return situacion

#Cantidad de ganancia por importacion/exportacion TOTAL
def monto_total(dbl,imports_exports):
    if imports_exports == "Exports" or imports_exports == "Imports":
        suma_total = 0
        for l in dbl:
            if l["direction"] == imports_exports:
                suma_total += float(l["total_value"])
        return suma_total
    else:
        return "ARGUMENTO INCORRECTO"
    
#Cantidad de ganancia por pais en importacion/exportacion
def monto_pais(dbl,pais,imports_exports):
    if imports_exports == "Exports" or imports_exports == "Imports":
        suma_parcial = 0
        for l in dbl:
          if l[situacion(imports_exports)] == pais and l["direction"] == imports_exports:
              suma_parcial += float(l["total_value"])
        return suma_parcial    
    else:
        return "ARGUMENTO INCORRECTO"
    
#Porcentaje de ganancia del país respecto al total en importacion/exportacion
def porcentaje_monto_pais(dbl,pais,imports_exports):
    if imports_exports == "Exports" or imports_exports == "Imports":
        porc = monto_pais(dbl,pais,imports_exports)/monto_total(dbl,imports_exports)
        return round(porc*100,2)
    else:
        return "ARGUMENTO INCORRECTO"    
    
#Cantidad total de veces que se comerció en importacion/exportacion
def operaciones_total(dbl,imports_exports):
    if imports_exports == "Exports" or imports_exports == "Imports":
        suma_total = 0
        for l in dbl:
            if l["direction"] == imports_exports:
                suma_total += 1
        return suma_total
    else:
        return "ARGUMENTO INCORRECTO"
    
#Cantidad de veces que se comerció en importacion/exportacion por pais
def operaciones_pais(dbl, pais, imports_exports):
    if imports_exports == "Exports" or imports_exports == "Imports":
        suma_parcial = 0
        for l in dbl:
          if l[situacion(imports_exports)] == pais and l["direction"] == imports_exports:
              suma_parcial += 1
        return suma_parcial    
    else:
        return "ARGUMENTO INCORRECTO"

#Porcentaje de operaciones  del país respecto al total en importacion/exportacion
def porcentaje_operaciones_pais(dbl,pais,imports_exports):
    if imports_exports == "Exports" or imports_exports == "Imports":
        porc = operaciones_pais(dbl,pais,imports_exports)/operaciones_total(dbl,imports_exports)
        return round(porc*100,2)
    else:
        return "ARGUMENTO INCORRECTO"    
    
#Conjunto de los países 
def cjto_paises(dbl,imports_exports):
    if imports_exports == "Exports" or imports_exports == "Imports":
        cjto = set()
        for l in dbl:
            if l["direction"] == imports_exports:
                cjto.add(l[situacion(imports_exports)])
        return cjto
    elif imports_exports == "Imports_Exports":
        cjto = cjto_paises(dbl,"Exports").union(cjto_paises(dbl,"Imports"))
        return cjto
    else:
        return "ARGUMENTO INCORRECTO"
      
#Nos muestra las características importantes del análisis por país        
def info_pais(dbl,imports_exports,monto_operaciones):
    lista = []
    if imports_exports in ["Imports", "Exports"]:
        for pais in cjto_paises(dbl, imports_exports):
            mont = monto_pais(dbl,pais,imports_exports)
            porcm = porcentaje_monto_pais(dbl,pais,imports_exports)
            op = operaciones_pais(dbl,pais,imports_exports)
            porco = porcentaje_operaciones_pais(dbl,pais,imports_exports)
            lista.append({"Pais":pais,   
                          "Direccion":imports_exports,
                         "Monto":mont, 
                         "Porcentaje Monto": porcm,
                         "Operaciones":op,
                         "Porcentaje Operaciones": porco,
                         "Monto Promedio": mont/op
                         })
            l1 = sorted(lista, key = lambda x : x[monto_operaciones], reverse = True)
        return l1
    elif imports_exports == "Imports_Exports":
        for pais in cjto_paises(dbl, imports_exports):
            mont = monto_pais(dbl,pais,"Imports") + monto_pais(dbl,pais,"Exports")
            porcm = mont/(monto_total(dbl,"Imports") + monto_total(dbl,"Exports"))
            op = operaciones_pais(dbl,pais,"Imports") + operaciones_pais(dbl,pais,"Exports")
            porco = op/(operaciones_total(dbl,"Imports") + operaciones_total(dbl,"Exports"))
            lista.append({"Pais":pais,   
                          "Direccion":imports_exports,
                         "Monto":mont,
                         "Porcentaje Monto": round(porcm*100,2),
                         "Operaciones":op,
                         "Porcentaje Operaciones": round(porco*100,2),
                         "Monto Promedio": mont/op
                         })
            l1 = sorted(lista, key = lambda x : x[monto_operaciones], reverse = True)
        return l1

#VARIABLES CON INFORMACION RELEVANTE POR PAIS
exp_monto_p = info_pais(dbl,"Exports", "Monto")
exp_operaciones_p = info_pais(dbl,"Exports", "Operaciones")
imp_monto_p = info_pais(dbl,"Imports", "Monto")
imp_operaciones_p = info_pais(dbl,"Imports", "Operaciones")
ie_monto_p = info_pais(dbl,"Imports_Exports", "Operaciones")
ie_operaciones_p = info_pais(dbl,"Imports_Exports", "Operaciones")

#Nos muestra de forma amigable los datos necesarios para la toma de decisiones
def insights_pais(info):
    for x in info:
      print(f"Pais {x['Direccion']}: {x['Pais']}\n\tOperaciones: {x['Operaciones']} ({x['Porcentaje Operaciones']}%)\n\t\tMonto: {x['Monto']} ({x['Porcentaje Monto']}%)\n\t\tMonto promedio: {x['Monto Promedio']}")

#insights_pais(ie_monto_p)

#Devuelve una lista con los paises/transportes que abarcan un 80% del monto/operaciones
def top(lista, monto_operaciones,pais_transporte, porc):
    porcentaje = 0
    paises_porc = []
    i = 0
    while porcentaje < porc:
        porcentaje += lista[i]["Porcentaje " + monto_operaciones]
        paises_porc.append(lista[i][pais_transporte])
        i += 1
    return paises_porc 
    
   

#2. ANÁLISIS DE MEDIO DE TRANSPORTE
#Cantidad de ganancia por transporte en importacion/exportacion
def monto_transporte(dbl,transporte,imports_exports):
    if imports_exports == "Exports" or imports_exports == "Imports":
        suma_parcial = 0
        for l in dbl:
          if l["transport_mode"] == transporte and l["direction"] == imports_exports:
              suma_parcial += float(l["total_value"])
        return suma_parcial    
    else:
        return "ARGUMENTO INCORRECTO"

#Cantidad de veces que se comerció en importacion/exportacion por transporte
def operaciones_transporte(dbl, transporte, imports_exports):
    if imports_exports == "Exports" or imports_exports == "Imports":
        suma_parcial = 0
        for l in dbl:
          if l["transport_mode"] == transporte and l["direction"] == imports_exports:
              suma_parcial += 1
        return suma_parcial    
    else:
        return "ARGUMENTO INCORRECTO"

#Porcentaje de ganancia usando el medio de transporte respecto al total en importacion/exportacion
def porcentaje_monto_transporte(dbl,transporte,imports_exports):
    if imports_exports == "Exports" or imports_exports == "Imports":
        porc = monto_transporte(dbl,transporte,imports_exports)/monto_total(dbl,imports_exports)
        return round(porc*100,2)
    else:
        return "ARGUMENTO INCORRECTO"    

#Porcentaje de operaciones con el medio de transporte respecto al total en importacion/exportacion
def porcentaje_operaciones_transporte(dbl,transporte,imports_exports):
    if imports_exports == "Exports" or imports_exports == "Imports":
        porc = operaciones_transporte(dbl,transporte,imports_exports)/operaciones_total(dbl,imports_exports)
        return round(porc*100,2)
    else:
        return "ARGUMENTO INCORRECTO"    
    
#Conjunto de los medios de transporte 
def cjto_transporte(dbl,imports_exports):
    if imports_exports == "Exports" or imports_exports == "Imports":
        cjto = set()
        for l in dbl:
            if l["direction"] == imports_exports:
                cjto.add(l["transport_mode"])
        return cjto
    elif imports_exports == "Imports_Exports":
        cjto = cjto_transporte(dbl,"Exports").union(cjto_transporte(dbl,"Imports"))
        return cjto
    else:
        return "ARGUMENTO INCORRECTO"

#Nos muestra las características importantes del análisis por transporte       
def info_transporte(dbl,imports_exports,monto_operaciones):
    lista = []
    if imports_exports in ["Imports", "Exports"]:
        for transporte in cjto_transporte(dbl, imports_exports):
            mont = monto_transporte(dbl,transporte,imports_exports)
            porcm = porcentaje_monto_transporte(dbl,transporte,imports_exports)
            op = operaciones_transporte(dbl,transporte,imports_exports)
            porco = porcentaje_operaciones_transporte(dbl,transporte,imports_exports)
            lista.append({"Transporte":transporte,   
                          "Direccion":imports_exports,
                         "Monto":mont, 
                         "Porcentaje Monto": porcm,
                         "Operaciones":op,
                         "Porcentaje Operaciones": porco,
                         "Monto Promedio": mont/op
                         })
            l1 = sorted(lista, key = lambda x : x[monto_operaciones], reverse = True)
        return l1
    elif imports_exports == "Imports_Exports":
        for transporte in cjto_transporte(dbl, imports_exports):
            mont = monto_transporte(dbl,transporte,"Imports") + monto_transporte(dbl,transporte,"Exports")
            porcm = mont/(monto_total(dbl,"Imports") + monto_total(dbl,"Exports"))
            op = operaciones_transporte(dbl,transporte,"Imports") + operaciones_transporte(dbl,transporte,"Exports")
            porco = op/(operaciones_total(dbl,"Imports") + operaciones_total(dbl,"Exports"))
            lista.append({"Transporte":transporte,   
                          "Direccion":imports_exports,
                         "Monto":mont,
                         "Porcentaje Monto": round(porcm*100,2),
                         "Operaciones":op,
                         "Porcentaje Operaciones": round(porco*100,2),
                         "Monto Promedio": mont/op
                         })
            l1 = sorted(lista, key = lambda x : x[monto_operaciones], reverse = True)
        return l1

#VARIABLES CON INFORMACION RELEVANTE POR TRANSPORTE
exp_monto_t = info_transporte(dbl,"Exports", "Monto")
exp_operaciones_t = info_transporte(dbl,"Exports", "Operaciones")
imp_monto_t = info_transporte(dbl,"Imports", "Monto")
imp_operaciones_t = info_transporte(dbl,"Imports", "Operaciones")
ie_monto_t = info_transporte(dbl,"Imports_Exports", "Operaciones")
ie_operaciones_t = info_transporte(dbl,"Imports_Exports", "Operaciones")

#Nos muestra de forma amigable los datos necesarios para la toma de decisiones
def insights_transporte(info):
    for x in info:
      print(f"Transporte {x['Direccion']}: {x['Transporte']}\n\tOperaciones: {x['Operaciones']} ({x['Porcentaje Operaciones']}%)\n\t\tMonto: {x['Monto']} ({x['Porcentaje Monto']}%)\n\t\tMonto promedio: {x['Monto Promedio']}\n")

#insights_transporte(info_transporte(dbl,"Imports_Exports", "Monto Promedio"))
#print(top(ie_operaciones_t,"Operaciones","Transporte", 80))

#1. ANÁLISIS X RUTA 
#Conjunto de rutas comerciales
def cjto_ruta(dbl,imports_exports):
    if imports_exports == "Exports" or imports_exports == "Imports":
        cjto = set()
        for l in dbl:
            if l["direction"] == imports_exports:
                cjto.add((l["origin"],l["destination"]))
        return cjto
    elif imports_exports == "Imports_Exports":
        cjto = cjto_ruta(dbl,"Exports").union(cjto_ruta(dbl,"Imports"))
        return cjto
    else:
        return "ARGUMENTO INCORRECTO"

#Cantidad de ganancia por ruta en importacion/exportacion
def monto_ruta(dbl,ruta,imports_exports):
    if imports_exports == "Exports" or imports_exports == "Imports":
        suma_parcial = 0
        for l in dbl:
          if (l["origin"],l["destination"]) == ruta and l["direction"] == imports_exports:
              suma_parcial += float(l["total_value"])
        return suma_parcial    
    else:
        return "ARGUMENTO INCORRECTO"

#print(monto_ruta(dbl,("Japan", "China"),"Exports")) 

#Cantidad de operaciones que tuvo la ruta
def operaciones_ruta(dbl, ruta, imports_exports):
    if imports_exports == "Exports" or imports_exports == "Imports":
        suma_parcial = 0
        for l in dbl:
          if (l["origin"],l["destination"]) == ruta and l["direction"] == imports_exports:
              suma_parcial += 1
        return suma_parcial    
    else:
        return "ARGUMENTO INCORRECTO"
#print(operaciones_ruta(dbl,("China","Japan"),"Imports_Exports"))

#Porcentaje de ganancia de la ruta respecto al total en importacion/exportacion
def porcentaje_monto_ruta(dbl,ruta,imports_exports):
    if imports_exports == "Exports" or imports_exports == "Imports":
        porc = monto_ruta(dbl,ruta,imports_exports)/monto_total(dbl,imports_exports)
        return round(porc*100,2)
    else:
        return "ARGUMENTO INCORRECTO"    

#Porcentaje de operaciones de la ruta respecto al total en importacion/exportacion
def porcentaje_operaciones_ruta(dbl,ruta,imports_exports):
    if imports_exports == "Exports" or imports_exports == "Imports":
        porc = operaciones_ruta(dbl,ruta,imports_exports)/operaciones_total(dbl,imports_exports)
        return round(porc*100,2)
    else:
        return "ARGUMENTO INCORRECTO"    
    

#Nos muestra las características importantes del análisis por ruta      
def info_ruta(dbl,imports_exports,monto_operaciones):
    lista = []
    if imports_exports in ["Imports", "Exports"]:
        for ruta in cjto_ruta(dbl, imports_exports):
            mont = monto_ruta(dbl,ruta,imports_exports)
            porcm = porcentaje_monto_ruta(dbl,ruta,imports_exports)
            op = operaciones_ruta(dbl,ruta,imports_exports)
            porco = porcentaje_operaciones_ruta(dbl,ruta,imports_exports)
            lista.append({"Ruta":ruta,   
                          "Direccion":imports_exports,
                         "Monto":mont, 
                         "Porcentaje Monto": porcm,
                         "Operaciones":op,
                         "Porcentaje Operaciones": porco,
                         "Monto Promedio": mont/op
                         })
            l1 = sorted(lista, key = lambda x : x[monto_operaciones], reverse = True)
        return l1
    elif imports_exports == "Imports_Exports":
        for ruta in cjto_ruta(dbl, imports_exports):
            mont = monto_ruta(dbl,ruta,"Imports") + monto_ruta(dbl,ruta,"Exports")
            porcm = mont/(monto_total(dbl,"Imports") + monto_total(dbl,"Exports"))
            op = operaciones_ruta(dbl,ruta,"Imports") + operaciones_ruta(dbl,ruta,"Exports")
            porco = op/(operaciones_total(dbl,"Imports") + operaciones_total(dbl,"Exports"))
            lista.append({"Ruta":ruta,   
                          "Direccion":imports_exports,
                         "Monto":mont,
                         "Porcentaje Monto": round(porcm*100,2),
                         "Operaciones":op,
                         "Porcentaje Operaciones": round(porco*100,2),
                         "Monto Promedio": mont/op
                         })
            l1 = sorted(lista, key = lambda x : x[monto_operaciones], reverse = True)
        return l1

#VARIABLES CON INFORMACION RELEVANTE POR RUTA
exp_monto_r = info_ruta(dbl,"Exports", "Monto")
exp_operaciones_r = info_ruta(dbl,"Exports", "Operaciones")
imp_monto_r = info_ruta(dbl,"Imports", "Monto")
imp_operaciones_r = info_ruta(dbl,"Imports", "Operaciones")
ie_monto_r = info_ruta(dbl,"Imports_Exports", "Operaciones")
ie_operaciones_r = info_ruta(dbl,"Imports_Exports", "Operaciones")

#Nos muestra de forma amigable los datos necesarios para la toma de decisiones
def insights_ruta(info):
    for x in info:
      print(f"Ruta {x['Direccion']}: {x['Ruta']}\n\tOperaciones: {x['Operaciones']} ({x['Porcentaje Operaciones']}%)\n\t\tMonto: {x['Monto']} ({x['Porcentaje Monto']}%)\n\t\tMonto promedio: {x['Monto Promedio']}\n")

#insights_ruta(info_ruta(dbl,"Imports_Exports", "Monto")[:10])
#print(top(ie_operaciones_t,"Operaciones","Transporte", 80))




#HUBIESE QUERIDO ADAPTAR ESTE CODIGO DEL PROYECTO PASADO 
#PARA QUE HUBIERA UNA INTERACCION CON EL USUARIO 
#NO TUVE MUCHA DISPONIBILIDAD DE TIEMPO LA ULTIMA SEMANA
#LO LAMENTO


# =============================================================================
# 
# 
# 
# 
# #####ACCESO
# 
# #Definimos al usuario administrador
# admin = [["EMTECH","proyecto1"]] 
# 
# #Definimos los usuarios iniciales con sus respectivas contraseñas
# acceso = [["Pepillo", "pp909316"], ["Javier","emtech123"]]
# 
# #Bienvenida
# print("¡Bienvenido¡ \n")
# #Indicadora de inicio de sesión 
# sesion = 0
# #Indicador del tipo de usuario, 0 - común, 1 - administrador
# usr = 0
# 
# #Empezamos a pedir acceso a usuarios
# while sesion == 0: 
#     print("Para acceder necesita ingresar su usuario y su contraseña. \n¿Cuenta con usuario y contraseña registrados? \n 1 - si \n 2 - no\n")
#     
#     #Recibimos cuenta existente o nueva del usuario
#     usuario = input("Ingrese el número que corresponde a su respuesta: ")
#     
#     #Para cuentas existentes
#     if usuario == "1":
#       u = input("\nIngrese su usuario: ")
#       for user in acceso:
#         if u == user[0] or u == admin[0][0]:
#           #sesion = 1
#           print("\nBienvenido", u)
#           p = input("Ingresa tu contraseña: ")
#           if ((p == user[1] and u== user[0]) or (p == admin[0][1] and u == admin[0][0])):
#             print("\nHas iniciado sesión con éxito\n")
#             sesion =1
#             if u == admin[0][0]:
#               print("Esta es una cuenta de administrador\n")
#               usr = 1            
#             break
#           else:
#             i = 0
#             while ((p != user[1] and u == user[0]) or (p != admin[0][1] and u == admin[0][0])) and i < 3:
#               i += 1
#               print("\n Quedan ", str(4-i)," intentos...")
#               p = input("Contraseña inválida, porfavor intente denuevo: ")
#             if i >= 3 and ((p != user[1] and u == user[0]) or (p != admin[0][1] and u == admin[0][0])):
#               print("\nHas alcanzado el número máximo de intentos, vuelve a iniciar sesión.\n\n")
#               break
#             else: 
#               print("\nHas iniciado sesión con éxito\n")
#               sesion = 1
#               if u == admin[0][0]:
#                 print("Esta es una cuenta de administrador\n")
#                 usr = 1
#               break
#           
#       if u != user[0] and u != admin[0][0]: #sesion == 0
#         print("No se encontró el usuario, intente denuevo o cree un nuevo perfil.\n")
#     
#     #Para cuentas nuevas      
#     elif usuario == "2":
#       u = input("\nRegistre nuevo usuario: ")
#       #sesion == 0
#       for user in acceso:
#         if u == user[0] or u == admin[0][0]:
#           print("Ya existe usuario ingresado, intente nuevamente.\n")
#           #sesion = 1
#           break
#       if u != user[0] and u != admin[0][0]: #sesion == 0:
#         p = input("Asigne contraseña del nuevo usuario: ")
#         pp = input("Confirme su contraseña: ")
#         if pp == p:
#           print("\nUsuario ", u, " registrado correctamente, sesión iniciada.\n\n")
#           sesion = 1
#           acceso.append([u,p])
#           
#         else:
#           i = 0
#           while p != pp and i < 3:
#             i += 1
#             print("\n Las contraseñas no coinciden.\n Quedan ", str(4-i), " intentos...")
#             p = input("\n Asigne contraseña del nuevo usuario: ")
#             pp = input("Confirme su contraseña: ")
#           if i >= 3 and p != pp:
#             print("\n No se puede registrar el usuario, vuelva a intentarlo. \n \n")
#           else:
#             print("\n Usuario ", u, " registrado correctamente, sesión iniciada con éxito.")
#             sesion = 1
#             acceso.append([u,p])
#     
#     else:
#       print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# 
# 
# #Acciones para usuarios comunes
# if sesion == 1 and usr == 0:
#     while sesion == 1:
#         print("\nMENÚ INICIAL\n\nReporte por pais:\n")
#         for i in range(0,len(vxc_desc)):
#             print(str(i+1) + " - " + vxc_desc[i][0] + "\n\tVentas brutas: " + str(vxc_desc[i][cven])  + "\n")
#         
#         #Recibimos eleccion de usuario
#         eleccion = input("Ingrese el número de la categoría que le interese para ver los productos.\nPresione '0' para salir.\n\nSelección: ")
#         if eleccion == "0":
#             print("Cerrando sesión...")
#             sesion = 0
#         
#         elif eleccion == "1" or eleccion == "2" or eleccion == "3" or eleccion == "4" or eleccion == "5" or eleccion == "6" or eleccion == "7" or eleccion == "8" :
#             for p in range(0, len(vxp_desc)):
#                 if vxp_desc[p][cat] == vxc_desc[int(eleccion)-1][0]:
#                     print("PRODUCTO: "+ vxp_desc[p][nom] + "\n\tVENTAS: " + str(vxp_desc[p][ven]))
#             permanecer = input("\n¿Desea volver al menú o salir?\n0 - salir\n1 - volver al menú\n\nIngrese una opción válida: ")
#             if permanecer == "0":
#                 print("Cerrando sesión...")
#                 sesion = 0
#             elif permanecer == "1":
#                 continue
#             else:
#                 i = 0
#                 while (permanecer != "0" and permanecer != "1") and i < 3:
#                   i += 1
#                   print("\n Quedan ", str(4-i)," intentos...")
#                   permanecer = input("Intente denuevo con una opción válida: ")
#                 if i >= 3 and (permanecer != "0" and permanecer != "1"):
#                   print("\nHas alcanzado el número máximo de intentos, vuelve a iniciar sesión.\n\n")
#                   break
#                 elif permanecer == "0":
#                           print("Cerrando sesión...")
#                           sesion = 0
#                           break
#                 else:
#                     continue 
#         else:
#             i = 0
#             while (eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4" and eleccion != "5" and eleccion != "6" and eleccion != "7" and eleccion != "8") and i < 3:
#               i += 1
#               print("\n Quedan ", str(4-i)," intentos...")
#               eleccion = input("Intente denuevo con una opción válida: ")
#             if i >= 3 and (eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4" and eleccion != "5" and eleccion != "6" and eleccion != "7" and eleccion != "8"):
#               print("\nHas alcanzado el número máximo de intentos, vuelve a iniciar sesión.\n\n")
#               break
#             else:
#                 for p in range(0, len(vxp_desc)):
#                     if productos[p][cat] == vxc_desc[int(eleccion)-1][0]:
#                         print("PRODUCTO: "+ productos[p][nom] + "\n\tVENTAS: " + str(productos[p][ven]))
#                 permanecer = input("\n¿Desea volver al menú o salir?\n0 - salir\n1 - volver al menú\n\nIngrese una opción válida: ")
#                 if permanecer == "0":
#                     print("Cerrando sesión...")
#                     sesion = 0
#                     break
#                 elif permanecer == "1":
#                     continue
#                 else:
#                     i = 0
#                     while (permanecer != "0" and permanecer != "1") and i < 3:
#                       i += 1
#                       print("\n Quedan ", str(4-i)," intentos...")
#                       permanecer = input("Intente denuevo con una opción válida: ")
#                     if i >= 3 and (permanecer != "0" and permanecer != "1"):
#                       print("\nHas alcanzado el número máximo de intentos, vuelve a iniciar sesión.\n\n")
#                       break
#                     elif permanecer == "0":
#                         print("Cerrando sesión...")
#                         sesion = 0
#                         break
#                     else:
#                         continue
# #Variable para Tops
# z1 = 50 
# z2 = 20
# #Acciones para administradores
# if sesion == 1 and usr == 1:
#   while sesion == 1:
#     print("\nMENÚ INICIAL\n\nReportes:\n\n1 - Por categorías\n2 - Por fecha\n3 - Por producto")
#     eleccion1 = input("Ingrese el número de la opción que desee.\nPresione '0' para salir\n\nSelección: ")
#     if eleccion1 == "0":
#         print("Cerrando sesión...\n")
#         sesion = 0
# #1
#     elif eleccion1 == "1":
#         print("POR CATEGORÍAS: \n\n1 - Ventas brutas x Categoría (sin incluir reembolsos)\n2 - Ventas netas x Categoría (incluyendo reembolsos)\n3 - Búsquedas x Categoría\n4 - Calificaciones x Categoría\n5 - Reembolsos x Categoría\n6 - Inventario x Categoría\n7 - Ingresos Brutos x Categoría\n8 - Ingresos Netos x Categoría")
#         eleccion2 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#         if eleccion2 == "0":
#             print("Regresando...\n")
# #1.1
#         elif eleccion2 == "1":
#             print("VENTAS BRUTAS X CATEGORÍA: \n\n1 - Mayores ventas brutas\n2 - Menores ventas brutas")
#             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#             if eleccion3 == "0":
#                 print("Regresando...\n")
# #1.1.1
#             elif eleccion3 =="1":
#                 print("MAYORES VENTAS BRUTAS X CATEGORÍA: \n")
#                 c = 0
#                 for v in vxc_desc:
#                     c += 1
#                     print(c, "Categoría: ",v[cnom], "\n\tVentas Brutas: ", v[cven], "\n\t\tMonto Vendido: ", v[cmont],"\n\t\t\tCalif. promedio: ", v[ccalif],"\n")
#                 
#                 eleccion4 = input("Ingrese el número de la categoría que le interese para ver los productos.\nPresione '0' para salir al MENÚ INICIAL.\n\nSelección: ")
#                 if eleccion4 == "0":
#                     continue
#                 elif eleccion4 == "1" or eleccion4 == "2" or eleccion4 == "3" or eleccion4 == "4" or eleccion4 == "5" or eleccion4 == "6" or eleccion4 == "7" or eleccion4 == "8" :
#                     for p in range(0, len(vxp_desc)):
#                         if vxp_desc[p][cat] == vxc_desc[int(eleccion4)-1][0]:
#                             print("PRODUCTO: "+ vxp_desc[p][nom] + "\n\tVENTAS: " + str(vxp_desc[p][ven]))
#                     per = input("\n¿Desea volver al menú o salir?\n0 - salir\n1 - volver al menú\n\nIngrese una opción válida: ")
#                     if per == "0":
#                         print("Cerrando sesión...")
#                         sesion = 0
#                     elif per == "1":
#                         continue
#                     else:
#                         print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#                         continue
#                 else:
#                         print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#                         continue
#                         
#                     
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #1.1.2
#             elif eleccion3 == "2":
#                 print("MENORES VENTAS BRUTAS X CATEGORÍA: \n")
#                 c=0
#                 for v in vxc_asc:
#                     c+=1
#                     print(c,"Categoría: ",v[cnom], "\n\tVentas Brutas: ", v[cven] , "\n\t\tMonto Vendido: ", v[cmont],"\n\t\t\tCalif. promedio: ", v[ccalif],"\n")
#                 
#                 eleccion4 = input("Ingrese el número de la categoría que le interese para ver los productos.\nPresione '0' para salir al MENÚ INICIAL.\n\nSelección: ")
#                 if eleccion4 == "0":
#                     continue
#                 elif eleccion4 == "1" or eleccion4 == "2" or eleccion4 == "3" or eleccion4 == "4" or eleccion4 == "5" or eleccion4 == "6" or eleccion4 == "7" or eleccion4 == "8" :
#                     for p in range(0, len(vxp_asc)):
#                         if vxp_asc[p][cat] == vxc_asc[int(eleccion4)-1][0]:
#                             print("PRODUCTO: "+ vxp_asc[p][nom] + "\n\tVENTAS: " + str(vxp_asc[p][ven]))
#                     per = input("\n¿Desea volver al menú o salir?\n0 - salir\n1 - volver al menú\n\nIngrese una opción válida: ")
#                     if per == "0":
#                         print("Cerrando sesión...")
#                         sesion = 0
#                     elif per == "1":
#                         continue
#                     else:
#                         print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#                         continue
#                 else:
#                         print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#                         continue
#                 
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n") 
#             else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")               
# #1.2                
#         elif eleccion2 == "2":
#             print("VENTAS NETAS X CATEGORÍA: \n\n1 - Mayores ventas netas\n2 - Menores ventas netas")
#             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#             if eleccion3 == "0":
#                 print("Regresando...\n")
# #1.2.1
#             elif eleccion3 == "1":
#                 print("MAYORES VENTAS NETAS X CATEGORÍA: \n")
#                 c=0
#                 for v in vrxc_desc:
#                     c+=1
#                     print(c,"Categoría: ",v[cnom], "\n\tVentas Netas: ", v[cven]-v[creemb], "\n\t\tInventario: ", v[cinv], "\n\t\t\tMonto Vendido: ", v[cmontr], "\n\t\t\t\tCalif. promedio: ", v[ccalif],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #1.2.2
#             elif eleccion3 == "2":
#                 print("MENORES VENTAS NETAS X CATEGORÍA: \n")
#                 c=0
#                 for v in vrxc_asc:
#                     c+=1
#                     print(c,"Categoría: ",v[cnom], "\n\tVentas Netas: ", v[cven]-v[creemb], "\n\t\tInventario: ", v[cinv], "\n\t\t\tMonto Vendido: ", v[cmontr], "\n\t\t\t\tCalif. promedio: ", v[ccalif],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#             else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #1.3
#         elif eleccion2 == "3":
#             print("BÚSQUEDAS X CATEGORÍA: \n\n1 - Mayores busquedas\n2 - Menores busquedas")
#             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#             if eleccion3 == "0":
#                 print("Regresando...\n")
# #1.3.1
#             elif eleccion3 == "1":
#                 print("MAYORES BUSQUEDAS X CATEGORÍA: \n")
#                 c=0
#                 for b in bxc_desc:
#                     c+=1
#                     print(c,"Categoría: ",b[cnom], "\n\tBusquedas: ", b[cbus], "\n\t\tVentas: ", b[cven],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #1.3.2
#             elif eleccion3 == "2":
#                 print("MENORES BUSQUEDAS X CATEGORÍA: \n")
#                 c=0 
#                 for b in bxc_asc:
#                     c+=1
#                     print(c,"Categoría: ",b[cnom], "\n\tBusquedas: ", b[cbus], "\n\t\tVentas: ", b[cven],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#             else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #1.4
#         elif eleccion2 == "4":
#             print("CALIFICACIONES X CATEGORÍA: \n\n1 - Mejores Calificaciones\n2 - Peores Calificaciones")                
#             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#             if eleccion3 == "0":
#                 print("Regresando...\n")
# #1.4.1
#             elif eleccion3 =="1":
#                 print("MEJORES CALIFICACIONES X CATEGORÍA: \n")
#                 c=0
#                 for v in cxc_desc:
#                     c+=1
#                     print(c,"Categoría: ",v[cnom], "\n\tCalificación: ", v[ccalif], "\n\t\tVentas Brutas: ", v[cven], "\n\t\t\tReembolsos: ", v[creemb],"\n\t\t\t\tVentas Netas: ", v[cven]-v[creemb],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #1.4.2
#             elif eleccion3 =="2":
#                 print("PEORES CALIFICACIONES X CATEGORÍA: \n")
#                 c=0
#                 for v in cxc_asc:
#                     c+=1
#                     print(c,"Categoría: ",v[cnom], "\n\tCalificación: ", v[ccalif], "\n\t\tVentas Brutas: ", v[cven], "\n\t\t\tReembolsos: ", v[creemb],"\n\t\t\t\tVentas Netas: ", v[cven]-v[creemb],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#             else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #1.5
#         elif eleccion2 == "5":
#              print("REEMBOLSOS X CATEGORÍA: \n\n1 - Mayores reembolsos\n2 - Menores reembolsos")
#              eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#              if eleccion3 == "0":
#                 print("Regresando...\n")
# #1.5.1               
#              elif eleccion3 == "1":
#                 print("MAYORES REEMBOLSOS X CATEGORÍA: \n")
#                 c=0
#                 for v in rxc_desc:
#                     c+=1
#                     print(c,"Categoría: ",v[cnom], "\n\tReembolsos: ", v[creemb],"\n\t\tCalificación: ",v[ccalif], "\n\t\t\tVentas Brutas: ", v[cven],"\n\t\t\t\tVentas Netas: ", v[cven]-v[creemb],"\n")
#                 
#                 eleccion4 = input("Ingrese el número de la categoría que le interese para ver los productos.\nPresione '0' para salir al MENÚ INICIAL.\n\nSelección: ")
#                 if eleccion4 == "0":
#                     continue
#                 elif eleccion4 == "1" or eleccion4 == "2" or eleccion4 == "3" or eleccion4 == "4" or eleccion4 == "5" or eleccion4 == "6" or eleccion4 == "7" or eleccion4 == "8" :
#                     for p in range(0, len(rxp_desc)):
#                         if rxp_desc[p][cat] == rxc_desc[int(eleccion4)-1][0]:
#                             print("PRODUCTO: "+ rxp_desc[p][nom] + "\n\tREEMBOLSOS: " + str(rxp_desc[p][reemb]))
#                     per = input("\n¿Desea volver al menú o salir?\n0 - salir\n1 - volver al menú\n\nIngrese una opción válida: ")
#                     if per == "0":
#                         print("Cerrando sesión...")
#                         sesion = 0
#                     elif per == "1":
#                         continue
#                     else:
#                         print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#                         continue
#                 else:
#                         print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#                         continue    
#                 
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #1.5.2              
#              elif eleccion3 == "2":
#                 print("MENORES REEMBOLSOS X CATEGORÍA: \n")
#                 c=0
#                 for v in rxc_asc:
#                     c+=1
#                     print(c,"Categoría: ",v[cnom], "\n\tReembolsos: ", v[creemb],"\n\t\tCalificación: ",v[ccalif], "\n\t\t\tVentas Brutas: ", v[cven],"\n\t\t\t\tVentas Netas: ", v[cven]-v[creemb],"\n")
#                 
#                 eleccion4 = input("Ingrese el número de la categoría que le interese para ver los productos.\nPresione '0' para salir al MENÚ INICIAL.\n\nSelección: ")
#                 if eleccion4 == "0":
#                     continue
#                 elif eleccion4 == "1" or eleccion4 == "2" or eleccion4 == "3" or eleccion4 == "4" or eleccion4 == "5" or eleccion4 == "6" or eleccion4 == "7" or eleccion4 == "8" :
#                     for p in range(0, len(rxp_asc)):
#                         if rxp_asc[p][cat] == rxc_asc[int(eleccion4)-1][0]:
#                             print("PRODUCTO: "+ rxp_asc[p][nom] + "\n\tREEMBOLSOS: " + str(rxp_asc[p][reemb]))
#                     per = input("\n¿Desea volver al menú o salir?\n0 - salir\n1 - volver al menú\n\nIngrese una opción válida: ")
#                     if per == "0":
#                         print("Cerrando sesión...")
#                         sesion = 0
#                     elif per == "1":
#                         continue
#                     else:
#                         print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#                         continue
#                 else:
#                         print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#                         continue 
#                 
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#              else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #1.6
#         elif eleccion2 == "6":
#              print("INVENTARIO X CATEGORÍA: \n\n1 - Mayor inventario\n2 - Menor inventario")
#              eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#              if eleccion3 == "0":
#                 print("Regresando...\n")
# #1.6.1               
#              elif eleccion3 == "1":
#                 print("MAYOR INVENTARIO X CATEGORÍA: \n")
#                 c=0
#                 for v in ixc_desc:
#                     c+=1
#                     print(c,"Categoría: ",v[cnom], "\n\tInventario: ", v[cinv],"\n\t\tCalificación: ", v[ccalif],"\n\t\t\tVentas Netas: ", v[cven]-v[creemb],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #1.6.2              
#              elif eleccion3 == "2":
#                 print("MENOR INVENTARIO X CATEGORÍA: \n")
#                 c=0
#                 for v in ixc_asc:
#                     c+=1
#                     print(c,"Categoría: ",v[cnom], "\n\tInventario: ", v[inv],"\n\t\tCalificación: ",v[ccalif],"\n\t\t\tVentas Netas: ", v[cven]-v[creemb],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#              else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #1.7
#         elif eleccion2 == "7":
#              print("INGRESOS BRUTOS X CATEGORÍA: \n\n1 - Mayores ingresos brutos\n2 - Menores ingresos brutos")
#              eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#              if eleccion3 == "0":
#                 print("Regresando...\n")
# #1.7.1               
#              elif eleccion3 == "1":
#                 print("MAYORES INGRESOS BRUTOS X CATEGORÍA: \n")
#                 c=0
#                 for v in mxc_desc:
#                     c+=1
#                     print(c,"Categoría: ",v[cnom], "\n\tIngresos Brutos: ", v[cmont], "\n\t\tVentas Brutas: ", v[cven],"\n\t\t\tReembolsos: ", v[creemb],"\n\t\t\t\tVentas Netas: ", v[cven]-v[creemb],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #1.7.2              
#              elif eleccion3 == "2":
#                 print("MENORES INGRESOS BRUTOS X CATEGORÍA: \n")
#                 c=0
#                 for v in mxc_asc:
#                     c+=1
#                     print(c,"Categoría: ",v[cnom], "\n\tIngresos Brutos: ", v[cmont], "\n\t\tVentas Brutas: ", v[cven],"\n\t\t\tReembolsos: ", v[creemb],"\n\t\t\t\tVentas Netas: ", v[cven]-v[creemb],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#              else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #1.8
#         elif eleccion2 == "8":
#              print("INGRESOS NETOS X CATEGORÍA: \n\n1 - Mayores ingresos netos\n2 - Menores ingresos netos")
#              eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#              if eleccion3 == "0":
#                 print("Regresando...\n")
# #1.8.1               
#              elif eleccion3 == "1":
#                 print("MAYORES INGRESOS NETOS X CATEGORÍA: \n")
#                 c=0
#                 for v in mrxc_desc:
#                     c+=1
#                     print(c,"Categoría: ",v[cnom], "\n\tIngresos Netos: ", v[cmontr], "\n\t\tVentas Netas: ", v[cven]-v[creemb],"\n\t\tCalificación: ",v[ccalif],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #1.8.2              
#              elif eleccion3 == "2":
#                 print("MENORES INGRESOS NETOS X CATEGORÍA: \n")
#                 c=0
#                 for v in mrxc_asc:
#                     c+=1
#                     print(c,"Categoría: ",v[cnom], "\n\tIngresos Netos: ", v[cmontr], "\n\t\tVentas Netas: ", v[cven]-v[creemb],"\n\t\tCalificación: ",v[ccalif],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#              else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#         else:
#             print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #2
#     elif eleccion1 == "2":
#         print("POR FECHA: \n\n1 - Ventas brutas x Fecha (sin incluir reembolsos)\n2 - Ventas netas x Fecha (incluyendo reembolsos)\n3 - Ingresos netos x Fecha")
#         eleccion2 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#         if eleccion2 == "0":
#             print("Regresando...\n")
# #2.1       
#         elif eleccion2 == "1":
#             print("VENTAS BRUTAS X FECHA: \n\n1 - Ventas brutas x mes\n2 - Mayores ventas brutas\n3 - Menores ventas brutas")
#             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#             if eleccion3 == "0":
#                 print("Regresando...\n")        
# #2.1.1 
#             elif eleccion3 == "1":
#                 print("VENTAS BRUTAS X MES: \n")
#                 vt = 0 #Ventas Brutas Totales
#                 it = 0 #Ingresos Brutos Totales
#                 c=0
#                 for mm in meses:
#                     c+=1
#                     print(c,"Mes: ",mm[1], "\n\tVentas Brutas: ", mm[2], "\n\t\tIngresos Brutos: ", mm[3],"\n")
#                     vt += mm[2]
#                     it += mm[3]
#                 print("Ventas Brutas Totales: ",vt,"\nIngresos Brutos Totales: ",it,"\n")    
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #2.1.2                  
#             elif eleccion3 == "2":
#                 print("MAYORES VENTAS BRUTAS X MES: \n")
#                 vt = 0 #Ventas Brutas Totales
#                 it = 0 #Ingresos Brutos Totales
#                 c=0
#                 for mm in vxf_desc:
#                     c+=1
#                     print(c,"Mes: ",mm[1], "\n\tVentas Brutas: ", mm[2], "\n\t\tIngresos Brutos: ", mm[3],"\n")
#                     vt += mm[2]
#                     it += mm[3]
#                 print("Ventas Brutas Totales: ",vt,"\nIngresos Brutos Totales: ",it,"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #2.1.3                                     
#             elif eleccion3 == "3":
#                 print("MENORES VENTAS BRUTAS X MES: \n")
#                 vt = 0 #Ventas Brutas Totales
#                 it = 0 #Ingresos Brutos Totales
#                 c=0
#                 for mm in vxf_asc:
#                     c+=1
#                     print(c,"Mes: ",mm[1], "\n\tVentas Brutas: ", mm[2], "\n\t\tIngresos Brutos: ", mm[3],"\n")
#                     vt += mm[2]
#                     it += mm[3]
#                 print("Ventas Brutas Totales: ",vt,"\nIngresos Brutos Totales: ",it,"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#             else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #2.2       
#         elif eleccion2 == "2":
#             print("VENTAS NETAS X FECHA: \n\n1 - Ventas netas x mes\n2 - Mayores ventas netas\n3 - Menores ventas netas")
#             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#             if eleccion3 == "0":
#                 print("Regresando...\n")        
# #2.2.1 
#             elif eleccion3 == "1":
#                 print("VENTAS NETAS X MES: \n")
#                 vrt = 0 #Ventas Netas Totales
#                 irt = 0 #Ingresos Netos Totales
#                 c=0
#                 for mm in meses:
#                     c+=1
#                     print(c,"Mes: ",mm[1], "\n\tVentas Netas: ", mm[2]-mm[4] , "\n\t\tIngresos Netos: ", mm[3]-mm[5],"\n")
#                     vrt += mm[2]-mm[4]
#                     irt += mm[3]-mm[5]
#                 print("Ventas Netas Totales: ",vrt,"\nIngresos Netos Totales: ",irt,"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #2.2.2                  
#             elif eleccion3 == "2":
#                 print("MAYORES VENTAS NETAS X MES: \n")
#                 vrt = 0 #Ventas Netas Totales
#                 irt = 0 #Ingresos Netos Totales
#                 c=0
#                 for mm in vrxf_desc:
#                     c+=1
#                     print(c,"Mes: ",mm[1], "\n\tVentas Netas: ", mm[2]-mm[4], "\n\t\tIngresos Netos: ", mm[3]-mm[5],"\n")
#                     vrt += mm[2]-mm[4]
#                     irt += mm[3]-mm[5]
#                 print("Ventas Netas Totales: ",vrt,"\nIngresos Netos Totales: ",irt,"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #2.2.3                                     
#             elif eleccion3 == "3":
#                 print("MENORES VENTAS NETAS X MES: \n")
#                 vrt = 0 #Ventas Netas Totales
#                 irt = 0 #Ingresos Netos Totales
#                 c=0
#                 for mm in vrxf_asc:
#                     c+=1
#                     print(c,"Mes: ",mm[1], "\n\tVentas Netas: ", mm[2]-mm[4], "\n\t\tIngresos Netos: ", mm[3]-mm[5],"\n")
#                     vrt += mm[2]-mm[4]
#                     irt += mm[3]-mm[5]
#                 print("Ventas Netas Totales: ",vrt,"\nIngresos Netos Totales: ",irt,"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#             else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#                  
# #2.3       
#         elif eleccion2 == "3":
#             print("INGRESOS NET0OS X FECHA: \n\n1 - Ingresos netos x mes\n2 - Mayores ingresos netos\n3 - Menores ingresos netos")
#             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#             if eleccion3 == "0":
#                 print("Regresando...\n")        
# #2.3.1 
#             elif eleccion3 == "1":
#                 print("INGRESOS NETOS X MES: \n")
#                 vrt = 0 #Ventas Netas Totales
#                 irt = 0 #Ingresos Netos Totales
#                 c=0
#                 for mm in meses:
#                     c+=1
#                     print(c,"Mes: ",mm[1], "\n\tIngresos Netos: ", mm[3]-mm[5],"\n\t\tVentas Netas: ", mm[2]-mm[4],"\n")
#                     vrt += mm[2]-mm[4]
#                     irt += mm[3]-mm[5]
#                 print("Ventas Netas Totales: ",vrt,"\nIngresos Netos Totales: ",irt,"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #2.3.2                  
#             elif eleccion3 == "2":
#                 print("MAYORES INGRESOS NETOS X MES: \n")
#                 vrt = 0 #Ventas Netas Totales
#                 irt = 0 #Ingresos Netos Totales
#                 c=0
#                 for mm in mrxf_desc:
#                     c+=1
#                     print(c,"Mes: ",mm[1], "\n\tIngresos Netos: ", mm[3]-mm[5],"\n\t\tVentas Netas: ", mm[2]-mm[4],"\n")
#                     vrt += mm[2]-mm[4]
#                     irt += mm[3]-mm[5]
#                 print("Ventas Netas Totales: ",vrt,"\nIngresos Netos Totales: ",irt,"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #2.3.3                                     
#             elif eleccion3 == "3":
#                 print("MENORES INGRESOS NETOS X MES: \n")
#                 vrt = 0 #Ventas Netas Totales
#                 irt = 0 #Ingresos Netos Totales
#                 c=0
#                 for mm in mrxf_desc:
#                     c+=1
#                     print(c,"Mes: ",mm[1], "\n\tIngresos Netos: ", mm[3]-mm[5],"\n\t\tVentas Netas: ", mm[2]-mm[4],"\n")
#                     vrt += mm[2]-mm[4]
#                     irt += mm[3]-mm[5]
#                 print("Ventas Netas Totales: ",vrt,"\nIngresos Netos Totales: ",irt,"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#             else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#         else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")  
#                                   
#                  
#                  
# #3        
#     elif eleccion1 == "3":
#         print("POR PRODUCTO: \n\n1 - Ventas brutas x Producto (sin incluir reembolsos)\n2 - Ventas netas x Producto (incluyendo reembolsos)\n3 - Búsquedas x Producto\n4 - Calificaciones x Producto\n5 - Reembolsos x Producto\n6 - Inventario x Producto\n7 - Precio x Producto")
#         eleccion2 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#         if eleccion2 == "0":
#             print("Regresando...\n")
# #3.1
#         elif eleccion2 == "1":
#             print("VENTAS BRUTAS X PRODUCTO: \n\n1 - Mayores ventas brutas\n2 - Menores ventas brutas")
#             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#             if eleccion3 == "0":
#                 print("Regresando...\n")
# #3.1.1
#             elif eleccion3 =="1":
#                 print(str(z1),"MAYORES VENTAS BRUTAS X PRODUCTO: \n")
#                 c=0
#                 for p in vxp_desc[:z1]:
#                     c+=1
#                     print(c,"Producto: ",p[nom], "\n\tVentas Brutas: ", p[ven],"\n\t\tPrecio: ", p[prec],"\n\t\t\tCalificación: ",p[calif], "\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #3.1.2
#             elif eleccion3 == "2":
#                 print(str(z1),"MENORES VENTAS BRUTAS X PRODUCTO: \n")
#                 c=0
#                 for p in vxp_asc[:z1]:
#                     c+=1
#                     print(c,"Producto: ",p[nom], "\n\tVentas Brutas: ", p[ven], "\n\t\tPrecio: ", p[prec],"\n\t\t\tCalificación: ",p[calif], "\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#             else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #3.2                
#         elif eleccion2 == "2":
#             print("VENTAS NETAS X PRODUCTO: \n\n1 - Mayores ventas netas\n2 - Menores ventas netas")
#             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#             if eleccion3 == "0":
#                 print("Regresando...\n")
# #3.2.1
#             elif eleccion3 == "1":
#                 print(str(z1),"MAYORES VENTAS NETAS X PRODUCTO: \n")
#                 c=0
#                 for p in vrxp_desc[:z1]:
#                     c+=1
#                     print(c,"Producto: ",p[nom], "\n\tVentas Netas: ", p[ven] - p[reemb], "\n\t\tInventario: ", p[inv],"\n\t\t\tPrecio: ", p[prec],"\n\t\t\t\tCalificación: ",p[calif], "\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #3.2.2
#             elif eleccion3 == "2":
#                 print(str(z1),"MENORES VENTAS NETAS X PRODUCTO: \n")
#                 c=0
#                 for p in vrxp_asc[:z1]:
#                     c+=1
#                     print(c,"Producto: ",p[nom], "\n\tVentas Netas: ", p[ven]-p[reemb], "\n\t\tInventario: ", p[inv],"\n\t\t\tPrecio: ", p[prec],"\n\t\t\t\tCalificación: ",p[calif], "\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#             else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #3.3
#         elif eleccion2 == "3":
#             print("BÚSQUEDAS X PRODUCTO: \n\n1 - Mayores busquedas\n2 - Menores busquedas")
#             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#             if eleccion3 == "0":
#                 print("Regresando...\n")
# #3.3.1
#             elif eleccion3 == "1":
#                 print(str(z1),"MAYORES BUSQUEDAS X PRODUCTO: \n")
#                 c=0
#                 for b in bxp_desc[:z1]:
#                     c+=1
#                     print(c,"Producto: ",b[nom], "\n\tBusquedas: ", b[bus], "\n\t\tVentas: ", b[ven],"\n\t\t\tCalificación: ", b[calif],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #3.3.2
#             elif eleccion3 == "2":
#                 print(str(z1),"MENORES BUSQUEDAS X PRODUCTO: \n")
#                 c=0
#                 for b in bxp_asc[:z1]:
#                     c+=1
#                     print(c,"Producto: ",b[nom], "\n\tBusquedas: ", b[bus], "\n\t\tVentas: ", b[ven],"\n\t\t\tCalificación: ", b[calif],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#             else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #3.4
#         elif eleccion2 == "4":
#             print("CALIFICACIONES X PRODUCTO: \n\n1 - Mejores Calificaciones\n2 - Peores Calificaciones")                
#             eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#             if eleccion3 == "0":
#                 print("Regresando...\n")
# #3.4.1
#             elif eleccion3 =="1":
#                 print(str(z2),"MEJORES CALIFICACIONES X PRODUCTO: \n")
#                 c=0
#                 for v in cxp_desc[:z2]:
#                     c+=1
#                     print(c,"Producto: ",v[nom], "\n\tCalificación: ", v[calif], "\n\t\tVentas Brutas: ", v[ven], "\n\t\t\tReembolsos: ", v[reemb],"\n\t\t\t\tVentas Netas: ", v[ven]-v[reemb],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #3.4.2
#             elif eleccion3 =="2":
#                 print(str(z2),"PEORES CALIFICACIONES X PRODUCTO: \n")
#                 c=0
#                 for v in cxp_asc[:z2]:
#                     c+=1
#                     print(c,"Producto: ",v[nom], "\n\tCalificación: ", v[calif], "\n\t\tVentas Brutas: ", v[ven], "\n\t\t\tReembolsos: ", v[reemb],"\n\t\t\t\tVentas Netas: ", v[ven]-v[reemb],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#             else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #3.5
#         elif eleccion2 == "5":
#              print("REEMBOLSOS X PRODUCTO: \n\n1 - Mayores reembolsos\n2 - Menores reembolsos")
#              eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#              if eleccion3 == "0":
#                 print("Regresando...\n")
# #3.5.1               
#              elif eleccion3 == "1":
#                 print(str(z1),"MAYORES REEMBOLSOS X PRODUCTO: \n")
#                 c=0
#                 for v in rxp_desc[:z1]:
#                     c+=1
#                     print(c,"Producto: ",v[nom], "\n\tReembolsos: ", v[reemb],"\n\t\tCalificación: ",v[calif], "\n\t\t\tVentas Brutas: ", v[ven],"\n\t\t\t\tVentas Netas: ", v[ven]-v[reemb],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #3.5.2              
#              elif eleccion3 == "2":
#                 print(str(z1),"MENORES REEMBOLSOS X PRODUCTO: \n")
#                 c=0
#                 for v in rxp_asc[:z1]:
#                     c+=1
#                     print(c,"Producto: ",v[nom], "\n\tReembolsos: ", v[reemb],"\n\t\tCalificación: ",v[calif], "\n\t\t\tVentas Brutas: ", v[ven],"\n\t\t\t\tVentas Netas: ", v[ven]-v[reemb],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#              else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")   
# #3.6
#         elif eleccion2 == "6":
#              print("INVENTARIO X PRODUCTO: \n\n1 - Mayor inventario\n2 - Menor inventario")
#              eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#              if eleccion3 == "0":
#                 print("Regresando...\n")
# #3.6.1               
#              elif eleccion3 == "1":
#                 print(str(z1),"MAYOR INVENTARIO X PRODUCTO: \n")
#                 c=0
#                 for v in ixp_desc[:z1]:
#                     c+=1
#                     print(c,"Producto: ",v[nom], "\n\tInventario: ", v[inv],"\n\t\tCalificación: ", v[calif],"\n\t\t\tVentas Netas: ", v[ven]-v[reemb],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #3.6.2              
#              elif eleccion3 == "2":
#                 print(str(z1),"MENOR INVENTARIO X PRODUCTO: \n")
#                 c=0
#                 for v in ixp_asc[:z1]:
#                     c+=1
#                     print(c,"Producto: ",v[nom], "\n\tInventario: ", v[inv],"\n\t\tCalificación: ",v[calif],"\n\t\t\tVentas Netas: ", v[ven]-v[reemb],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#              else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #3.7
#         elif eleccion2 == "7":
#              print("PRECIOS X PRODUCTO: \n\n1 - Mayores precios\n2 - Menores precios")
#              eleccion3 = input("Ingrese el número de la opción que desee.\nPresione '0' para regresar al menú inicial\n\nSelección: ")
#              if eleccion3 == "0":
#                 print("Regresando...\n")
# #3.7.1               
#              elif eleccion3 == "1":
#                 print(str(z1),"MAYORES PRECIOS X PRODUCTO: \n")
#                 c=0
#                 for v in pxp_desc[:z1]:
#                     c+=1
#                     print(c,"Producto: ",v[nom], "\n\tPrecio: ", v[prec], "\n\t\tVentas Brutas: ", v[ven],"\n\t\t\tReembolsos: ", v[reemb],"\n\t\t\t\tVentas Netas: ", v[ven]-v[reemb],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
# #3.7.2              
#              elif eleccion3 == "2":
#                 print(str(z1),"MENORES PRECIOS X PRODUCTO: \n")
#                 c=0
#                 for v in pxp_asc[:z1]:
#                     c+=1
#                     print(c,"Producto: ",v[nom], "\n\tPrecio: ", v[prec], "\n\t\tVentas Brutas: ", v[ven],"\n\t\t\tReembolsos: ", v[reemb],"\n\t\t\t\tVentas Netas: ", v[ven]-v[reemb],"\n")
#                 permanecer = input("\n¿Desea continuar visualizando datos o salir?\n1 - continuar\n0 - salir\nSelección: ")
#                 if permanecer == "0":
#                     sesion = 0
#                 elif permanecer == "1":
#                     continue
#                 else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#              else:
#                  print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#         else:
#             print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#     else:
#         print("\nERROR: Selección no válida, porfavor lea y siga cuidadosamente las indicaciones. \n\n")
#             
# 
# 
# 
# =============================================================================
