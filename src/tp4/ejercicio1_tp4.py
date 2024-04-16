import os

# Clase Ping
class Ping:
    def execute(self, ip):
        if ip.startswith("192."):
            for _ in range(10):
                response = os.system("ping -c 1 " + ip)
                print(f"Ping a {ip}: {'Conexión exitosa' if response == 0 else 'Error en la conexión'}")
        else:
            print("La dirección IP no comienza con '192.'")

    def executefree(self, ip):
        for _ in range(10):
            response = os.system("ping -c 1 " + ip)
            print(f"Ping a {ip}: {'Conexión exitosa' if response == 0 else 'Error en la conexión'}")

# Clase PingProxy
class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip):
        if ip == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip)

# Uso del código
proxy = PingProxy()
proxy.execute("192.168.0.1")  # Prueba de ping con dirección IP que comienza con "192."
proxy.execute("8.8.8.8")       # Prueba de ping con dirección IP que no comienza con "192."
proxy.execute("192.168.0.254") # Prueba de ping con dirección IP especial
