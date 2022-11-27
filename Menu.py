from gestion import obtenerTrabajadores,agregarTrabajador,modificarTrabajador,eliminarTrabajador,mostrarTrabajadorActivo,mostrarTrabajadorDesocupados,mostrarTDesocupadosUnRangoEdad,mostrarTrabajadoresSegunProfesion,cambiarStatusTrabajadores

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
        --------------------------
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
            dni = int(input("Ingresa el dni del trabajador a modificar: "))
            modificarTrabajador(listadoTrabajadores, dni)

            
            
        elif opciones1 == 3:
            print("Eliminar")
            dni= int(input("Ingresa el dni del trabajador a eliminarr: "))
            eliminarTrabajador(listadoTrabajadores,dni)

            

            
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
            mostrarTrabajadorActivo(listadoTrabajadores)

        

        elif opciones1 == 2:
            print("Mostrar trabajadores desocupados")
            mostrarTrabajadorDesocupados(listadoTrabajadores)

         

        elif opciones1 == 3:
            print("Mostrar desocupados en un rango de edad")
            #filtrar por un rango de edad
            edad1 = int(input("Ingrese edad desde: "))
            edad2 = int(input("Ingrese edad hasta: "))
            mostrarTDesocupadosUnRangoEdad(listadoTrabajadores,edad1,edad2)


        elif opciones1 == 4:
            print("Mostrar trabajadores segun la profesion")
            profesion= input("Ingresa la profesion de trabajadores a buscar: ")
            mostrarTrabajadoresSegunProfesion(listadoTrabajadores,profesion)

        else:
            print("Elija una opcion correcta")


  elif opcion == 3:
    print("Cambiar status trabajador")
    dni= int(input("Ingresa el dni del trabajador a modificar status: "))
    cambiarStatusTrabajadores(listadoTrabajadores,dni)  
  
  else:
    print("Elija una opcion correcta")

print("Gracias por usar la app")


    
