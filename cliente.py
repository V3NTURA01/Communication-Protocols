import socket

# Crear un objeto de socket
mi_socket = socket.socket(
    socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

try:
    # Conectarse al servidor
    # Reemplaza 'Direccion_MAC_del_servidor' con la dirección MAC del dispositivo Bluetooth del servidor
    mi_socket.connect(("e0:d4:64:60:4f:ae", 4))

    while True:
        # Enviar un mensaje al servidor
        mensaje = input("Cliente: ")
        mi_socket.send(mensaje.encode('utf-8'))

        # Recibir una respuesta del servidor
        respuesta = mi_socket.recv(1024)
        print(f"Servidor: {respuesta.decode('utf-8')}")

finally:
    # Cerrar la conexión
    mi_socket.close()
