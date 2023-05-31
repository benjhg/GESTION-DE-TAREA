class tareas:
        
        def __init__(self,tareas, nombre):

            tareas = []
            self.nombre = nombre

        def mostrar_menu(opciones):
            print('Seleccione una opción:')
            for clave in sorted(opciones):
                print(f' {clave}) {opciones[clave][0]}')


        def leer_opcion(opciones):
            while (a := input('Opción: ')) not in opciones:
                print('Opción incorrecta, vuelva a intentarlo.')
            return a


        def ejecutar_opcion(opcion, opciones):
            opciones[opcion][1]()


        def generar_menu(opciones, opcion_salida):
            opcion = None
            while opcion != opcion_salida:
                mostrar_menu(opciones)
                opcion = leer_opcion(opciones)
                ejecutar_opcion(opcion, opciones)
                print()


        def menu_principal():
            opciones = {
                '1': ('Opción 1 : Esto es para añadir la tarea en frente, esto significa que la tarea es importante', addFront),
                '2': ('Opción 2 : Esto es para añadir la tarea al final, esto significa que la tarea no es tan importante', addBack),
                '3': ('Opción 3 : Esto es para ver el estado en el que esta la tarea', contains),
                '4': ('Salir', salir)
            }

            generar_menu(opciones, '4')


        def addFront():
            print('Has elegido la opción 1')


        def addBack():
            print('Has elegido la opción 2')


        def contains():
            print('Has elegido la opción 3')


        def salir():
            print('Saliendo')


        if __name__ == '__main__':
            menu_principal()