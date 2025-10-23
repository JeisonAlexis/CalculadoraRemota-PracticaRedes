import socket
import argparse

def main(server_ip, server_port):
    print("=== Calculadora Remota de IMC ===")
    try:
        peso = float(input("Ingresa tu peso en kg: "))
        altura = float(input("Ingresa tu altura en metros (ej: 1.75): "))
    except ValueError:
        print("Error: ingresa valores numéricos válidos.")
        return

    # Crear socket
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect((server_ip, server_port))
        print(f"[+] Conectado al servidor {server_ip}:{server_port}")

        # Enviar datos
        mensaje = f"{peso}|{altura}"
        cliente.sendall(mensaje.encode('utf-8'))

        # Recibir resultado
        resultado = cliente.recv(1024).decode('utf-8')
        print(f"[Servidor]: {resultado}")

    except Exception as e:
        print(f"[!] Error de conexión: {e}")
    finally:
        cliente.close()
        print("[*] Conexión cerrada.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cliente TCP para calcular IMC remotamente.")
    parser.add_argument("--server", required=True, help="Dirección IP del servidor")
    parser.add_argument("--port", type=int, default=9999, help="Puerto TCP del servidor")
    args = parser.parse_args()

    main(args.server, args.port)

