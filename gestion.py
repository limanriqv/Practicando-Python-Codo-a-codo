from generales import validarIngresoEntero

def obtenerTrabajadores(nombreArchivo):
  try:
    archivo = open(nombreArchivo,"r")
  except FileNotFoundError:
    archivo = open(nombreArchivo,"a")
    archivo.write("xxx,11,111111,xxxxxx,xxxx")   
    archivo.close()
    archivo = open(nombreArchivo,"r")

  trabajadores=[]
  for linea in archivo.readlines():
    trabajador=linea.replace('\n','')
    trabajador=trabajador.split(",")
    trabajador= {"nombre":trabajador[0],"edad":int(trabajador[1]),"dni":int(trabajador[2]),"profesion":trabajador[3],"activo":trabajador[4]}
    trabajadores.append(trabajador)
  archivo.close()
  return trabajadores

def agregarTrabajadorEnArchivo(nombreArchivo,trabajador):
  archivo = open(nombreArchivo,"a")
  linea = f"\n{trabajador['nombre']},{trabajador['edad']},{trabajador['dni']},{trabajador['profesion']},{trabajador['activo']}"
  archivo.write(linea)
  archivo.close()


def agregarTrabajador(listado):
  nombre=input("Nombre: ")
  edad = validarIngresoEntero("Edad: ")
  dni = validarIngresoEntero("DNI: ")
  profesion=input("Profesión: ")
  activo = input("Activo: True o False: ")
  trabajador = {"nombre":nombre,"edad":edad, "dni":dni, "profesion":profesion, "activo":activo}
  listado.append(trabajador)
  agregarTrabajadorEnArchivo("trabajadores.dat",trabajador)

############################################

def modificarTrabajador(listado,dni):
  for trabajador in listado:
    if trabajador["dni"] == dni:
      nombre = input("Nombre(Presione enter para no modificar) ")
      if nombre == '':
        nombre=trabajador["nombre"]
      edad = input("Edad(Presione enter para no modificar) ")  
      if edad == '':
        edad = trabajador["edad"]
      dni = input("DNI(Presione enter para no modificar) ")
      if dni == '':
        dni = trabajador["dni"]
      profesion = input("Profesion(Presione enter para no modificar) ")
      if profesion == '':
        profesion=trabajador["profesion"]
      activo = input("Activo(Presione enter para no modificar) ")
      if activo == '':
        activo = trabajador["activo"]

      # Modificar el trabajador del listado con los nuevos datos
      trabajador["nombre"] = nombre
      trabajador["edad"] = edad
      trabajador["dni"]= dni
      trabajador["profesion"]=profesion
      trabajador["activo"]=activo
      break


      # Modificar el trabajador del listado con los nuevos datos
  file = open("trabajadores.dat","w")
  contenido=[]
  for trabajador in listado:
    linea = f"\n{trabajador['nombre']},{trabajador['edad']},{trabajador['dni']},{trabajador['profesion']},{trabajador['activo']}"
    contenido.append(linea)
  contenido[0] = contenido[0].replace("\n","")
  file.writelines(contenido)
  file.close()
  


#### 
def eliminarTrabajador(listado,dni):
  indice=0
  for trabajador in listado:
    if trabajador["dni"] == dni:
      listado.pop(indice)
      break
    indice = indice + 1

  # Eliminar al trabajador en el archivo
  trabajadores = open("trabajadores.dat","w")
  contenido=[]
  for trabajador in listado:
    linea = f"\n{trabajador['nombre']},{trabajador['edad']},{trabajador['dni']},{trabajador['profesion']},{trabajador['activo']}"  
    contenido.append(linea)
  contenido[0] = contenido[0].replace("\n","")

  trabajadores.writelines(contenido) # ["","",""]
  trabajadores.close()
      

#####REPORTES
#########################
# Mostrar trabajadores activos

def mostrarTrabajadorActivo(listado):
  for t in listado:
    if t["activo"]=="True":
      print(t)


###########################
# Mostrar trabajadores desocupados")
def mostrarTrabajadorDesocupados(listado):
  for t in listado:
    if t["activo"]=="False":
      print(t)


########################
# Mostrar desocupados en un rango de edad
def mostrarTDesocupadosUnRangoEdad(listado,edad1,edad2):
  edadRango = list(range(edad1,edad2+1)) 
  for t in listado:
    for num in edadRango:
      if num==t["edad"] and t["activo"]=="False":
          print(t)
  else:
    print("Ingresa una opcion valida")


#############################
#Mostrar trabajadores segun la profesion
def mostrarTrabajadoresSegunProfesion(listado,profesion):
  for t in listado:
    if t["profesion"]==profesion:
      print(t)
            


##########################
def cambiarStatusTrabajadores(listado,dni):         
  for t in listado:
    if t["dni"] == dni:
      if t["activo"]=="False":
        t["activo"]="True"
      else:
        t["activo"]="False"
  
  print (listado)

  file = open("trabajadores.dat","w")
  contenido=[]
  for trabajador in listado:
    linea = f"\n{trabajador['nombre']},{trabajador['edad']},{trabajador['dni']},{trabajador['profesion']},{trabajador['activo']}"
    contenido.append(linea)
  contenido[0] = contenido[0].replace("\n","")
  file.writelines(contenido)
  file.close()



  