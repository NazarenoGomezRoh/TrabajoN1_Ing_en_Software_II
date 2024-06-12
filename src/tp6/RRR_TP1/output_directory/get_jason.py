"""
Extractor de Token para Acceso API Servicios Banco XXX

Este programa permite extraer la clave de acceso API para utilizar los servicios del Banco XXX.

Copyright UADERFCyT-IS2©2024 Todos los derechos reservados.

Autor: [Nombre del autor]
"""

import json
import sys

# Definición de la versión del programa
VERSION = "1.2"

class JsonExtractor:
    """
    Clase JsonExtractor: Utilizada para extraer tokens de un archivo JSON.
    """
    _instance = None

    def __new__(cls, json_file):
        """
        Método __new__: Crea una instancia única de JsonExtractor si no existe.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.json_file = json_file
        return cls._instance

    def get_token(self, bank_name, json_key='token1'):
        """
        Método get_token: Extrae el token correspondiente al banco y la clave especificada.
        """
        try:
            with open(self.json_file, 'r', encoding='utf-8') as myfile:
                data = myfile.read()
            obj = json.loads(data)
            if bank_name not in obj:
                raise KeyError(f"The bank '{bank_name}' does not exist in the JSON file.")
            bank_tokens = obj[bank_name]['tokens']
            token = bank_tokens.get(json_key)
            if token is None:
                raise KeyError(f"The key '{json_key}' does not exist for the bank '{bank_name}' in the JSON file.")
            return token
        except FileNotFoundError as e:
            return f"Error: The file {self.json_file} does not exist. {e}"
        except json.JSONDecodeError as e:
            return f"Error: The file is not a valid JSON file. {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    def select_bank(self, amount):
        """
        Método select_bank: Selecciona el banco con saldo suficiente y que equilibre los pagos.
        """
        try:
            with open(self.json_file, 'r', encoding='utf-8') as myfile:
                data = myfile.read()
            banks = json.loads(data)
            selected_bank = None
            for bank_name, details in banks.items():
                if details['saldo'] >= amount:
                    if selected_bank is None or details['saldo'] < banks[selected_bank]['saldo']:
                        selected_bank = bank_name
            if selected_bank is None:
                return "Error: No bank has sufficient balance for this payment."
            return selected_bank
        except FileNotFoundError as e:
            return f"Error: The file {self.json_file} does not exist. {e}"
        except json.JSONDecodeError as e:
            return f"Error: The file is not a valid JSON file. {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

def print_help():
    """
    Función print_help: Imprime un mensaje de ayuda detallado.
    """
    help_message = """
Mensaje de ayudapyl
    """
    print(help_message)

def main():
    """
    Función principal: Ejecuta el programa.
    """
    if len(sys.argv) < 3 or sys.argv[1] == '-h':
        if len(sys.argv) == 3:
            print_help()
        else:
            print("Usage: python getJason.py <amount> <jsonkey>")
        sys.exit(1)
    elif sys.argv[1] == '-v':
        print(f"Versión {VERSION}")
        sys.exit(0)

    try:
        amount = float(sys.argv[1])
    except ValueError:
        print("Error: Amount must be a number.")
        sys.exit(1)
    json_key = sys.argv[2]
    
    json_file = "sitedata.json"

    extractor = JsonExtractor(json_file)
    bank_name = extractor.select_bank(amount)
    if bank_name.startswith("Error"):
        print(bank_name)
        sys.exit(1)

    token = extractor.get_token(bank_name, json_key)
    if token.startswith("Error"):
        print(token)
        sys.exit(1)
    else:
        print(f"{1.0}{token}")

    # Simulación de liberación de pago
    liberar_pago(bank_name, token, amount)

def liberar_pago(bank_name, token, amount):
    """
    Función liberar_pago: Simula la liberación de un pago utilizando un token.
    """
    print(f"Liberando pago de {amount} para {bank_name} usando el token: {token}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
