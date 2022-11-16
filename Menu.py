from gestion import obtenerTrabajadores, agregarTrabajadorEnArchivo,agregarTrabajador,modificarTrabajador
from generales import validarIngresoEntero

listadoTrabajadores = obtenerTrabajadores("trabajadores.dat")
print(listadoTrabajadores)
while True:
  print(
    f'''
    \t Menu
    [1]Gestión de trabajadores
    [2]Reportes
    [3]Cambiar status trabajador
    [0]Salir
    '''
    )
  opcion = validarIngresoEntero("Selecccione una opcion: ")
  
  if opcion == 0:
    break
  elif opcion == 1:
    while True:
        print(
        f'''
        \t Gestión de trabajadores
        -------
        [1] Agregar un trabajador
        [2] Modificar un trabajador
        [3] Eliminar un trabajador
        [0] Salir
        '''
            )
        opciones1 = validarIngresoEntero("Selecccione una opcion: ")
        if opciones1 == 0:
            break
        elif opciones1 == 1:
            print("Agregar")
            agregarTrabajador(listadoTrabajadores)
        elif opciones1 == 2:
            print("Modificar")
            modificarTrabajador(listadoTrabajadores,3223233232)
        elif opciones1 == 3:
            print("Eliminar")
        else:
            print("Elija una opcion correcta")

        print(listadoTrabajadores)


  elif opcion == 2:
    while True:
        print(
        f'''
        \t Reportes
        -------
        [1] Mostrar trabajadores activos
        [2] Mostrar trabajadores desocupados
        [3] Mostrar desocupados en un rango de edad
        [4]Mostrar trabajadores segun la profesion
        [0] Salir
        '''
            )
        opciones1 = validarIngresoEntero("Selecccione una opcion: ")
        if opciones1 == 0:
            break
        elif opciones1 == 1:
            print("Mostrar trabajadores activos")
        elif opciones1 == 2:
            print("Mostrar trabajadores desocupados")
        elif opciones1 == 3:
            print("Mostrar desocupados en un rango de edad")
        elif opciones1 == 4:
            print("Mostrar trabajadores segun la profesion")
        else:
            print("Elija una opcion correcta")


  elif opcion == 3:
    print("Cambiar status trabajador")
  else:
    print("Elija una opcion correcta")

print("Gracias por usar la app")


    
