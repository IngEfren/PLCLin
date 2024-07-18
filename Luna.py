# Importamos el modulo para trabajar con comunicacion ethernet
from pycomm3 import LogixDriver

# Importamos el modulo para trabajar con sockets
import socket
# Importamos el modulo para trabajar con pausas
from time import sleep

# Direccion IP del PLC
IP = "192.168.10.1/0"

# IP del Babylin
HOST = '192.168.10.40'
# Puerto del Babylin
PORT = 10002

def main():
    try:
        # Ajustamos los parametro del servidor socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Realizamos una conexion con la direccion del servidor y el puerto
        client_socket.connect((HOST, PORT))
        # Mostramos un mensaje de conexion exitosa
        print("\nConexión establecida con Baby-LIN-MB-II")
        # Enviamos el comando al servidor Baby-LIN-MB-II
        client_socket.send(":LoadSdf 0 maintest.sdf\n".encode())
        # Almacenamos la informacion resivida del servidor Baby-LIN-MB-II
        response = client_socket.recv(2048)
        # Si la respuesta es 0
        if (response.decode() == ':0\r'):
            # Mostramos el mensaje recibido
            print(f"Carga de SDF: Correcta")
        # Enviamos el comando para iniciar una simulacion
        client_socket.send(":Start 0 2\n".encode())
        # Almacenamos la informacion resivida del servidor Baby-LIN-MB-II
        response = client_socket.recv(2048)
        # Si la respuesta es 0
        if (response.decode() == ':0\r'):
            # Mostramos el mensaje recibido
            print(f"Estatus de la simulacion: Correcta")
        # Cerramos la comunicación socket
        client_socket.close()
    # En caso de no tener una conexion mostramos el siguiente mensaje
    except ConnectionRefusedError:
        # Mostramos un mensaje de falla
        print("No se pudo conectar al servidor")

    # Creamos un buble infinito
    while True:
        with LogixDriver(IP) as plc:
            valueTag01 = plc.read("ST30BabylinRedTest")[1]
            valueTag02 = plc.read("ST30BabylinGreenTest")[1]
            valueTag03 = plc.read("ST30BabylinBlueTest")[1]
            valueTag04 = plc.read("ST30BabylinTurnOffTest")[1]
            valueTag05 = plc.read("ST30BabylinTriggerPCBTest")[1]
            valueTag06 = plc.read("ST30BabylinTriggerButtonTest")[1]
            valueTag07 = plc.read("ST30BabylinTriggerMagneticTest")[1]
            valueTag08 = plc.read("ST30BabylinTriggerResetAllTest")[1]
            valueTag09 = plc.read("ST30BabylinTriggerTest01")[1]
            valueTag10 = plc.read("ST30BabylinTriggerTest02")[1]
            valueTag11 = plc.read("ST30BabylinTriggerTest03")[1]
            valueTag12 = plc.read("ST30BabylinTriggerTest04")[1]
            valueTag13 = plc.read("ST30BabylinTriggerTest05")[1]

            # Ajustamos los parametro del servidor socket
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Leemos una etiqueta
            if (valueTag01):
                # Tratamos de ejecutar el siguiente codigo
                try:
                    # Realizamos una conexion con la direccion del servidor y el puerto
                    client_socket.connect((HOST, PORT))
                    # Enviamos el comando al servidor Baby-LIN-MB-II
                    client_socket.send(":MacroExec 0 5\n".encode())
                    # Mostramos el mensaje recibido
                    print(f"LEDs rojos encendidos")
                    # Cerramos la comunicación socket
                    client_socket.close()
                # En caso de no tener una conexion mostramos el siguiente mensaje
                except ConnectionRefusedError:
                    # Mostramos un mensaje de falla
                    print("No se pudo conectar al servidor")
            # Leemos una etiqueta
            if (valueTag02):
                # Tratamos de ejecutar el siguiente codigo
                try:
                    # Realizamos una conexion con la direccion del servidor y el puerto
                    client_socket.connect((HOST, PORT))
                    # Enviamos el comando al servidor Baby-LIN-MB-II
                    client_socket.send(":MacroExec 0 6\n".encode())
                    # Mostramos el mensaje recibido
                    print(f"LEDs verdes encendidos")
                    # Cerramos la comunicación socket
                    client_socket.close()
                # En caso de no tener una conexion mostramos el siguiente mensaje
                except ConnectionRefusedError:
                    # Mostramos un mensaje de falla
                    print("No se pudo conectar al servidor")
            # Leemos una etiqueta
            if (valueTag03):
                # Tratamos de ejecutar el siguiente codigo
                try:
                    # Realizamos una conexion con la direccion del servidor y el puerto
                    client_socket.connect((HOST, PORT))
                    # Enviamos el comando al servidor Baby-LIN-MB-II
                    client_socket.send(":MacroExec 0 7\n".encode())
                    # Mostramos el mensaje recibido
                    print(f"LEDs azules encendidos")
                    # Cerramos la comunicación socket
                    client_socket.close()
                # En caso de no tener una conexion mostramos el siguiente mensaje
                except ConnectionRefusedError:
                    # Mostramos un mensaje de falla
                    print("No se pudo conectar al servidor")
            # Leemos una etiqueta
            if (valueTag04):
                # Tratamos de ejecutar el siguiente codigo
                try:
                    # Realizamos una conexion con la direccion del servidor y el puerto
                    client_socket.connect((HOST, PORT))
                    # Enviamos el comando al servidor Baby-LIN-MB-II
                    client_socket.send(":MacroExec 0 8\n".encode())
                    # Mostramos el mensaje recibido
                    print(f"LEDs apagados")
                    # Cerramos la comunicación socket
                    client_socket.close()
                # En caso de no tener una conexion mostramos el siguiente mensaje
                except ConnectionRefusedError:
                    # Mostramos un mensaje de falla
                    print("No se pudo conectar al servidor")  
            # Leemos una etiqueta
            if (valueTag05):
                # Tratamos de ejecutar el siguiente codigo
                try:
                    # Realizamos una conexion con la direccion del servidor y el puerto
                    client_socket.connect((HOST, PORT))
                    # Enviamos el comando
                    client_socket.send(":MacroExec 0 2\n".encode())
                    # Almacenamos la informacion de la respuesta
                    response = client_socket.recv(2048)
                    # Esperamos un tiempo
                    sleep(1.2)
                    # Enviamos el comando al servidor
                    client_socket.send(":LinrdSignal 0 !ResultPCB\n".encode())
                    # Almacenamos la informacion resivida del servidor Baby-LIN-MB-II
                    response = client_socket.recv(2048)
                    # Si el valor es 1...
                    if (response.decode() == ":1\r"):
                        # Ajustamos la variable
                        plc.write('ST30BabylinResultPCBTest', 1)
                    # Mostramos el mensaje recibido
                    print(f"Resultado prueba PCB: {response.decode()}")
                    # Cerramos la comunicación socket
                    client_socket.close()
                # En caso de no tener una conexion mostramos el siguiente mensaje
                except ConnectionRefusedError:
                    print("No se pudo conectar al servidor")  
            # Leemos una etiqueta
            if (valueTag06):
                # Tratamos de ejecutar el siguiente codigo
                try:
                    # Realizamos una conexion con la direccion del servidor y el puerto
                    client_socket.connect((HOST, PORT))
                    # Enviamos el comando
                    client_socket.send(":MacroExec 0 1\n".encode())
                    # Almacenamos la informacion de la respuesta
                    response = client_socket.recv(2048)
                    # Esperamos un tiempo
                    sleep(1.2)
                    # Enviamos el comando
                    client_socket.send(":LinrdSignal 0 !ResultButton\n".encode())
                    # Almacenamos la informacion de la respuesta
                    response = client_socket.recv(2048)
                    # Si el valor es 1...
                    if (response.decode() == ":1\r"):
                        # Ajustamos la variable
                        plc.write('ST30BabylinResultButtonTest', 1)
                    # Mostramos el mensaje recibido
                    print(f"Resultado prueba boton: {response.decode()}")
                    # Cerramos la comunicación socket
                    client_socket.close()
                # En caso de no tener una conexion mostramos el siguiente mensaje
                except ConnectionRefusedError:
                    print("No se pudo conectar al servidor")
            # Leemos una etiqueta
            if (valueTag07):
                # Tratamos de ejecutar el siguiente codigo
                try:
                    # Realizamos una conexion con la direccion del servidor y el puerto
                    client_socket.connect((HOST, PORT))
                    # Enviamos el comando al servidor Baby-LIN-MB-II
                    client_socket.send(":MacroExec 0 3\n".encode())
                    # Almacenamos la informacion resivida del servidor Baby-LIN-MB-II
                    response = client_socket.recv(2048)
                    # Esperamos un tiempo
                    sleep(1)
                    # Enviamos el comando al servidor Baby-LIN-MB-II
                    client_socket.send(":LinrdSignal 0 !ResultMagnetic\n".encode())
                    # Almacenamos la informacion resivida del servidor Baby-LIN-MB-II
                    response = client_socket.recv(2048)
                    # Si el valor es 1...
                    if (response.decode() == ":1\r"):
                        # Ajustamos la variable
                        plc.write('ST30BabylinResultMagneticTest', 1)
                    # Mostramos el mensaje recibido
                    print(f"Resultado prueba magnetica: {response.decode()}")
                    # Cerramos la comunicación socket
                    client_socket.close()
                # En caso de no tener una conexion mostramos el siguiente mensaje
                except ConnectionRefusedError:
                    print("No se pudo conectar al servidor")
            # Leemos una etiqueta
            if (valueTag08):
                # Tratamos de ejecutar el siguiente codigo
                try:
                    # Realizamos una conexion con la direccion del servidor y el puerto
                    client_socket.connect((HOST, PORT))
                    # Enviamos el comando al servidor Baby-LIN-MB-II
                    client_socket.send(":MacroExec 0 4\n".encode())
                    # Cerramos la comunicación socket
                    client_socket.close()
                # En caso de no tener una conexion mostramos el siguiente mensaje
                except ConnectionRefusedError:
                    print("No se pudo conectar al servidor")

            # Leemos una etiqueta
            if (valueTag09):
                # Tratamos de ejecutar el siguiente codigo
                try:
                    # Realizamos una conexion con la direccion del servidor y el puerto
                    client_socket.connect((HOST, PORT))
                    # Enviamos el comando
                    client_socket.send(":MacroExec 0 9\n".encode())
                    # Almacenamos la informacion de la respuesta
                    response = client_socket.recv(2048)
                    # Esperamos un tiempo
                    sleep(1)
                    # Enviamos el comando
                    client_socket.send(":LinrdSignal 0 !ResultTest01\n".encode())
                    # Almacenamos la informacion de la respuesta
                    response = client_socket.recv(2048)
                    # Si el valor es 1...
                    if (response.decode() == ":1\r"):
                        # Ajustamos la variable
                        plc.write('ST30BabylinResultTest01', 1)
                    # Mostramos el mensaje recibido
                    print(f"Resultado de Test01: {response.decode()}")
                    # Cerramos la comunicación socket
                    client_socket.close()
                # En caso de no tener una conexion mostramos el siguiente mensaje
                except ConnectionRefusedError:
                    print("No se pudo conectar al servidor")
            # Leemos una etiqueta
            if (valueTag10):
                # Tratamos de ejecutar el siguiente codigo
                try:
                    # Realizamos una conexion con la direccion del servidor y el puerto
                    client_socket.connect((HOST, PORT))
                    # Enviamos el comando
                    client_socket.send(":MacroExec 0 10\n".encode())
                    # Almacenamos la informacion de la respuesta
                    response = client_socket.recv(2048)
                    # Esperamos un tiempo
                    sleep(1)
                    # Enviamos el comando
                    client_socket.send(":LinrdSignal 0 !ResultTest02\n".encode())
                    # Almacenamos la informacion de la respuesta
                    response = client_socket.recv(2048)
                    # Si el valor es 1...
                    if (response.decode() == ":1\r"):
                        # Ajustamos la variable
                        plc.write('ST30BabylinResultTest02', 1)
                    # Mostramos el mensaje recibido
                    print(f"Resultado de Test02: {response.decode()}")
                    # Cerramos la comunicación socket
                    client_socket.close()
                # En caso de no tener una conexion mostramos el siguiente mensaje
                except ConnectionRefusedError:
                    print("No se pudo conectar al servidor")
            if (valueTag11):
                # Tratamos de ejecutar el siguiente codigo
                try:
                    # Realizamos una conexion con la direccion del servidor y el puerto
                    client_socket.connect((HOST, PORT))
                    # Enviamos el comando
                    client_socket.send(":MacroExec 0 11\n".encode())
                    # Almacenamos la informacion de la respuesta
                    response = client_socket.recv(2048)
                    # Esperamos un tiempo
                    sleep(1)
                    # Enviamos el comando
                    client_socket.send(":LinrdSignal 0 !ResultTest03\n".encode())
                    # Almacenamos la informacion de la respuesta
                    response = client_socket.recv(2048)
                    # Si el valor es 1...
                    if (response.decode() == ":1\r"):
                        # Ajustamos la variable
                        plc.write('ST30BabylinResultTest03', 1)
                    # Mostramos el mensaje recibido
                    print(f"Resultado de Test03: {response.decode()}")
                    # Cerramos la comunicación socket
                    client_socket.close()
                # En caso de no tener una conexion mostramos el siguiente mensaje
                except ConnectionRefusedError:
                    print("No se pudo conectar al servidor")
            if (valueTag12):
                # Tratamos de ejecutar el siguiente codigo
                try:
                    # Realizamos una conexion con la direccion del servidor y el puerto
                    client_socket.connect((HOST, PORT))
                    # Enviamos el comando
                    client_socket.send(":MacroExec 0 12\n".encode())
                    # Almacenamos la informacion de la respuesta
                    response = client_socket.recv(2048)
                    # Esperamos un tiempo
                    sleep(1)
                    # Enviamos el comando
                    client_socket.send(":LinrdSignal 0 !ResultTest04\n".encode())
                    # Almacenamos la informacion de la respuesta
                    response = client_socket.recv(2048)
                    # Si el valor es 1...
                    if (response.decode() == ":1\r"):
                        # Ajustamos la variable
                        plc.write('ST30BabylinResultTest04', 1)
                    # Mostramos el mensaje recibido
                    print(f"Resultado de Test04: {response.decode()}")
                    # Cerramos la comunicación socket
                    client_socket.close()
                # En caso de no tener una conexion mostramos el siguiente mensaje
                except ConnectionRefusedError:
                    print("No se pudo conectar al servidor")
            if (valueTag13):
                # Tratamos de ejecutar el siguiente codigo
                try:
                    # Realizamos una conexion con la direccion del servidor y el puerto
                    client_socket.connect((HOST, PORT))
                    # Enviamos el comando
                    client_socket.send(":MacroExec 0 13\n".encode())
                    # Almacenamos la informacion de la respuesta
                    response = client_socket.recv(2048)
                    # Esperamos un tiempo
                    sleep(1)
                    # Enviamos el comando
                    client_socket.send(":LinrdSignal 0 !ResultTest05\n".encode())
                    # Almacenamos la informacion de la respuesta
                    response = client_socket.recv(2048)
                    # Si el valor es 1...
                    if (response.decode() == ":1\r"):
                        # Ajustamos la variable
                        plc.write('ST30BabylinResultTest05', 1)
                    # Mostramos el mensaje recibido
                    print(f"Resultado de Test05: {response.decode()}")
                    # Cerramos la comunicación socket
                    client_socket.close()
                # En caso de no tener una conexion mostramos el siguiente mensaje
                except ConnectionRefusedError:
                    print("No se pudo conectar al servidor")

    # Creamos un punto de acceso
if __name__ == "__main__":
    # Llamamos a la funcion principal
    main()