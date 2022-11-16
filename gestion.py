from generales import validarIngresoEntero

def obtenerTrabajadores(nombreArchivo):
  try:
    archivo = open(nombreArchivo,"r")
  except FileNotFoundError:
    archivo = open(nombreArchivo,"a")
    archivo.write("Esteban,18,33333333,Gamer,True")   ###ver revisar
    archivo.close()
    archivo = open(nombreArchivo,"r")

  trabajadores=[]
  for linea in archivo.readlines():
    trabajador=linea.replace('\n','')
    trabajador=trabajador.split(",")
    trabajador= {"nombre":trabajador[0],"edad":int(trabajador[1]),"dni":int(trabajador[2]),"profesion":trabajador[3],"activo":bool(trabajador[4])}
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


def modificarTrabajador(listado,dni):
  for trabajador in listado:
    if trabajador["dni"] == dni:
      print(trabajador)
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
      trabajador["Profesion"]=profesion
      trabajador["Activo"]=activo
      break
  

###
# 
def eliminarTrabajador(listado,dni):
  indice=0
  for trabajador in listado:
    if trabajador["dni"] == dni:
      print(trabajador)
      listado.pop(indice)
      break
    indice = indice + 1

  # Eliminar al trabajador en el archivo
  print(listado)
  trabajadores = open("trabajadores.dat","w")
  contenido=[]
  for trabajador in listado:
    linea = f"\n{trabajador['nombre']},{trabajador['edad']},{trabajador['dni']},{trabajador['profesion']},{trabajador['activo']}"  
    contenido.append(linea)
  contenido[0] = contenido[0].replace("\n","")

  trabajadores.writelines(contenido) # ["","",""]
  trabajadores.close()
      
