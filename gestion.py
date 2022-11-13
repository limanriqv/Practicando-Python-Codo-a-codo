from generales import validarIngresoEntero

def obtenerTrabajadores(nombreArchivo):
  try:
    archivo = open(nombreArchivo,"r")
  except FileNotFoundError:
    archivo = open(nombreArchivo,"a")
    archivo.write("Enzo,12,3223233232,Gamer,True")   ###ver revisar
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
  activo = input("Activo: True o False")
  
  trabajador = {"nombre":nombre,"edad":edad, "dni":dni, "profesion":profesion, "activo":activo}
  listado.append(trabajador)
  agregarTrabajadorEnArchivo("trabajadores.dat",trabajador)
