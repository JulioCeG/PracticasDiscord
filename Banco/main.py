"""
1. Create an online banking system with the following features:
    * Users must be able to log in with a username and password.
    * If the user enters the wrong credentials three times, the system must lock them out.
    * The initial balance in the bank account is $2000.
    * The system must allow users to deposit, withdraw, view, and transfer money.
    * The system must display a menu for users to perform transactions.

Descripción:
Este programa simula un sistema de gestion de un banco online,
Caracteristicas implementadas:
    * Logueo de usuarios
    * Posibilidad de ingresar, extraer o transferir dinero
    * Desplegar un menu para realizar esas acciones
"""

import argparse

from usuario import User
from banco import Bank
from menu import Menu

#opciones del menu
opciones = ['Depositar', 'Extracción', 'Ver Saldo', 'Transferir', 'Salir']

#instancio un objeto menu de la clase menu
miMenu = Menu(opciones)

# Instancio tres objetos usuarioX de la clase User y los meto en una lista
usuario1 = User('jose', '123')
usuario2 = User('pepe', '456')
usuario3 = User('marcelo', '789')
usuario4 = User('jorge', '1234')

users_list = [usuario1, usuario2, usuario3, usuario4]

# Instancio un objeto fakeBank de la clase Bank
bancoabc = Bank(users_list)

# Aquí comienza el código real del programa.
def main():

    attempts = 0
    max_attempts = 3
    parser = argparse.ArgumentParser(description='client terminal interface for online bank')

    # Agrega argumentos opcionales "-u" y "-p" para el nombre de usuario y la contraseña
    parser.add_argument('-u', '--user', type=str, help='Username')
    parser.add_argument('-p', '--passw', type=str, help='User password')

    args = parser.parse_args()

    if args.user:
        user_name = args.user
    else:
        user_name = input('\nBienvenido al Banco ABC. Por favor ingrese su usuario\nUsuario: ')

    if args.passw:
        user_password = args.passw
    else:
        user_password = input('Contraseña: ')

    if bancoabc.login(user_name, user_password):
        print(f'\nAcceso correcto. \n---->')
        while True:
            # print(f'\n{"*" * 30}')

            #print(f'\n• Cliente: {bancoabc.session.name}. • Código de cliente: {bancoabc.session.user_code}. • Saldo actual: ${bancoabc.session.money}')
            print(f'• Opciones:\n')
            miMenu.showOptions()
            print(f'\n{"*" * 20}')
            selection = input(f'Elija una opcion: (1-{len(opciones)}): ')

            if selection == '1':    # Depositar
                amount = int(input('Monto a depositar: $ '))
                bancoabc.add_money(amount)  
            elif selection == '2':  # Extracción
                amount = int(input('Monto que desea extraer: $ '))
                if bancoabc.enough_mount(amount):
                    bancoabc.extract_money(amount)
                else:
                    print('Error: Saldo insufiente en cuenta para la transferencia que desea realizar.')
            elif selection == '3': # Ver Saldo
                print(f'\nSu saldo actual es de: ${bancoabc.session.money}')
            elif selection == '4':  # Transferir
                bancoabc.show_users()
                payee = int(input('\nCodigo de cliente destino: '))
                amount = int(input('Monto: $ '))
                if bancoabc.enough_mount(amount):
                    bancoabc.send_money(amount, payee)
            elif selection == '5':  # Salir
                print('Sesión finalizada, vuelva pronto!\n')
                break
            else:
                print('Error: Opcion invalida')
if __name__ == "__main__":
    main()