"""
client.py
Cliente TCP para la calculadora remota.
Solicita dos operandos y el operador al usuario, envía al servidor y muestra resultado.
Protocolo: "operand1|operator|operand2"
"""
import socket
import argparse

def solicitar_datos():
    a = input("Ingrese el primer número: ").strip()
    op = input("Ingrese la operación (+, -, *, /): ").strip()
    b = input("Ingrese el segundo número: ").strip()
    return a, op, b

def main(server_ip: str, port: int):
    a, op, b = solicitar_datos()
    mensaje = f"{a}|{op}|{b}"
    try:
        with socket.create_connection((server_ip, port), timeout=10) as sock:
            sock.sendall(mensaje.encode('utf-8'))
            respuesta = sock.recv(1024)
            if not respuesta:
                print("No se recibió respuesta del servidor.")
            else:
                print("Resultado del servidor:", respuesta.decode('utf-8'))
    except Exception as e:
        print("Error de conexión/operación:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cliente TCP calculadora remota")
    parser.add_argument("--server", required=True, help="IP del servidor")
    parser.add_argument("--port", type=int, default=9999, help="Puerto del servidor (default: 9999)")
    args = parser.parse_args()
    main(args.server, args.port)
