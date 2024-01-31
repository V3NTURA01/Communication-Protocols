import socket

# Crear un objeto de socket
mi_socket = socket.socket(
    socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Especifica una dirección MAC; '' indica que aceptará conexiones en todas las interfaces disponibles
mi_socket.bind(("e0:d4:64:60:4f:ae", 4))

# Poner el socket en modo de escucha
mi_socket.listen(1)

print("Servidor Bluetooth escuchando...")

try:
    while True:
        conexion, addr = mi_socket.accept()
        print("Conexión establecida con:", addr)

        while True:
            mensaje_cliente = conexion.recv(1024).decode('utf-8')
            print(f"Cliente: {mensaje_cliente}")

            mensaje = input("Servidor: ")
            conexion.send(mensaje.encode('utf-8'))

except KeyboardInterrupt:
    print("\nServidor cerrado manualmente.")
    mi_socket.close()
