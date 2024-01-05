'''
2. Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
    * The user must choose their initial currency and the currency they want to exchange to.
    * The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
    * If the user decides to withdraw the funds, the system will charge a 1% commission.
    * Set a minimum and maximum amount for each currency, it can be of your choice.
    * The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process; otherwise, the system should close.  
'''
class CurrencyConversor:
    def __init__(self):
        # Definicion de los valores de conversion
        self.currencys = {
            'CLP': 1200.0,
            'ARS': 1000.0,
            'USD': 1.0,
            'EUR': 0.11,
            'TRY': 0.13,
            'GBP': 1.32
        }

        # Definicion de monto minimo y maximo
        self.min_amount = 10
        self.max_amount = 10000

    def convert(self, amount, initial_currency, final_currency, withdraw):
        # Valida que el monto este entre los valores permitidos
        if amount < self.min_amount or amount > self.max_amount:
            return "La cantidad ingresada está fuera del rango permitido."
        # Validacion de moneda existente
        if initial_currency not in self.currencys or final_currency not in self.currencys:
            return "Moneda no válida."
        # Aplica comisión del 1% si se retiran los fondos
        if withdraw:
            commission = amount * 0.01
            amount -= commission

        converted_amount = amount * self.currencys[final_currency] / self.currencys[initial_currency]

            
        result = f"{amount:.2f} {initial_currency} equivale a {converted_amount:.2f} {final_currency}."

        if withdraw:
            result += f"\nSe ha aplicado una comisión del 1% ({commission:.2f} {initial_currency})."
        

        return result


def main():
    converter = CurrencyConversor()

    while True:
        print("Bienvenido al convertidor de monedas.\n Por favor elija una de las monedas disponibles:")
        for currency in converter.currencys:
            print(f"- {currency}")

        from_currency = input("Ingrese la moneda inicial (ej. USD): ").upper()

        if from_currency not in converter.currencys:
            print("Moneda no válida.\n")
            continue

        print("Monedas de destino disponibles:")
        for currency in converter.currencys:
            print(f"- {currency}")

        to_currency = input("Ingrese la moneda de destino (ej. EUR): ").upper()

        if to_currency not in converter.currencys:
            print("Moneda no válida.\n")
            continue

        amount = float(input("Ingrese la cantidad a convertir: "))
        withdraw_funds = input("¿Desea retirar los fondos? (s/n): ").lower() == 's'

        result = converter.convert(amount, from_currency, to_currency, withdraw_funds)
        print(result)

        another_operation = input("¿Desea realizar otra operación? (s/n): ").lower()
        if another_operation != 's':
            break


if __name__ == "__main__":
    main()