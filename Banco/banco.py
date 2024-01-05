class Bank():
    def __init__(self, users_list, max_attempts=3, ):
        self.users_list = users_list
        self.session = None
        self.attempts = 0
        self.max_attempts = max_attempts

    # Lista los usuarios
    def show_users(self):
        print('Usuarios: ')
        for i in self.users_list:
            print(f'\tNombre: {i.name}\t   Codigo de usuario: {i.user_code}')

    # Chequeo de usuario existente
    def user_exist(self, user_name):
        for user in self.users_list:
            if user.name == user_name:
                return user
        return False
    
    # Chequeo de codigo de usuario existente
    def code_exist(self, usr_code):
        for user in self.users_list:
            if user.user_code == usr_code:
                return user
        return False

    # Logueo con su validacion de intentos maximos
    def login(self, user_name, user_password):
        user = self.user_exist(user_name)

        if user:
            for _ in range(self.max_attempts):
                if user.password == user_password:
                    self.session = user
                    self.attempts = 0  # Reiniciar el contador de intentos al iniciar sesión exitosamente
                    return True
                else:
                    self.attempts += 1
                    print('Error: Contraseña incorrecta')
                    remaining_attempts = self.max_attempts - self.attempts
                    if remaining_attempts > 0:
                        print(f'Tiene {remaining_attempts} más para intentarlo.')
                        user_password = input('Contraseña: ')  # Solicitar nuevamente la contraseña
                    else:
                        print(f"Superó la cantidad de intentos fallidos ({self.attempts}). Su cuenta ha sido bloqueada.")
                        break  # Salir del bucle después de superar los intentos máximos
        else:
            self.attempts += 1
            print("Usuario inexistente. Por favor, vuelva a intentarlo.")
            remaining_attempts = self.max_attempts - self.attempts
            while remaining_attempts > 0:
                print(f'Tiene {remaining_attempts} más para intentarlo.')
                user_name = input('Usuario: ')  # Solicitar nuevamente el usuario
                user_password = input('Contraseña: ')  # Solicitar nuevamente la contraseña
                user = self.user_exist(user_name)
                if user and user.password == user_password:
                    self.session = user
                    self.attempts = 0
                    return True
                else:
                    print('Error: Contraseña incorrecta. Intente nuevamente.')
                    self.attempts += 1
                    remaining_attempts = self.max_attempts - self.attempts

            print(f"Superó la cantidad de intentos fallidos ({self.attempts}). Su cuenta ha sido bloqueada.")

        return False
      
    # Chequeo de saldo suficiente
    def enough_mount(self, mount):
        if self.session.money < mount:
            return False
        return True

    # Agregar dinero a cuenta
    def add_money(self, amount):
        if self.session == False:
            print('Error: No está logueado.')
            return False
        else:
            self.session.money += amount
            print(f'Deposito realizado correctamente.')
    
    # Extraer dinero de la cuenta
    def extract_money(self, amount):
        if self.enough_mount(amount):
            self.session.money -= amount
            print(f'Extraccion realizada correctamente.')

    # Transferir dinero de la cuenta
    def send_money(self, amount, payee_code):
        usr = self.code_exist(payee_code)
        if usr == False:
            print(f'Error: No se encuentra el codigo de usuario: {payee_code}')
            return False
        else:
            self.session.money -= amount
            usr.money += amount
            print('Transferencia realizada correctamente.')