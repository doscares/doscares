from os import system

trabajadores = []

def menu_principal():
    opciones = {
        '1': ('registrar trabajador', accion1),
        '2': ('lista trabajador', listar_trabajadores),
        '3': ('imprimir planilla de trabajadores', accion3),
        '4': ('salir', salir)
    }

    generar_menu(opciones, '4')

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        if opcion != opcion_salida:
            input("Presione Enter para continuar...")  

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

def accion1():
    nombre = input('Ingrese el nombre del trabajador: ')
    cargo = input('Ingrese el cargo del trabajador: ')
    sueldo_bruto = float(input('Ingrese el sueldo bruto del trabajador: '))
    desc_salud = float(input('Ingrese el descuento de salud: '))
    desc_afp = float(input('Ingrese el descuento de AFP: '))
    liquido_pagar = sueldo_bruto - desc_salud - desc_afp
    
    trabajador = {
        'nombre': nombre,
        'cargo': cargo,
        'sueldo_bruto': sueldo_bruto,
        'desc_salud': desc_salud,
        'desc_afp': desc_afp,
        'liquido_pagar': liquido_pagar
    }
    trabajadores.append(trabajador)
    print(f'Trabajador {nombre} registrado.')

def listar_trabajadores():
    print('Lista de trabajadores:')
    for trabajador in trabajadores:
        print(f"- Nombre: {trabajador['nombre']}, Cargo: {trabajador['cargo']}, Sueldo Bruto: {trabajador['sueldo_bruto']}, Desc. Salud: {trabajador['desc_salud']}, Desc. AFP: {trabajador['desc_afp']}, Líquido a Pagar: {trabajador['liquido_pagar']}")

def accion3():
    print('Imprimiendo planilla de trabajadores...')
    for trabajador in trabajadores:
        print(f"- Nombre: {trabajador['nombre']}, Cargo: {trabajador['cargo']}, Sueldo Bruto: {trabajador['sueldo_bruto']}, Desc. Salud: {trabajador['desc_salud']}, Desc. AFP: {trabajador['desc_afp']}, Líquido a Pagar: {trabajador['liquido_pagar']}")

def salir():
    print('Saliendo...')

menu_principal()