"""
server.py
Servidor TCP para calculadora remota.
Escucha conexiones continuamente y atiende cada cliente en un hilo.
Protocolo simple (texto UTF-8): "operando1|operador|operando2"
Ejemplo de mensaje: "12.5|+|3.4"
Respuesta: resultado como string o mensaje de error.
"""
import socket
import threading
import argparse

def calcular(a: float, op: str, b: float):
    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                return "ERROR: Division por cero"
            return a / b
        else:
            return "ERROR: Operador no soportado"
    except Exception as e:
        return f"ERROR: {e}"

def manejar_cliente(conn: socket.socket, addr):
    with conn:
        try:
            data = conn.recv(1024)  
            if not data:
                return
            mensaje = data.decode('utf-8').strip()
            # formato: "operand1|operator|operand2"
            parts = mensaje.split('|')
            if len(parts) != 3:
                respuesta = "ERROR: Formato invalido. Uso: num1|op|num2"
            else:
                try:
                    a = float(parts[0])
                    op = parts[1]
                    b = float(parts[2])
                    resultado = calcular(a, op, b)
                    respuesta = str(resultado)
                except ValueError:
                    respuesta = "ERROR: Operandos no numericos"
            conn.sendall(respuesta.encode('utf-8'))
        except Exception as e:
            try:
                conn.sendall(f"ERROR: {e}".encode('utf-8'))
            except:
                pass

def main(host: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    print(f"[+] Servidor escuchando en {host}:{port}. Ctrl+C para salir.")
    try:
        while True:
            conn, addr = sock.accept()
            print(f"[+] Conexión entrante desde {addr}")
            hilo = threading.Thread(target=manejar_cliente, args=(conn, addr), daemon=True)
            hilo.start()
    except KeyboardInterrupt:
        print("\n[!] Servidor detenido por usuario.")
    finally:
        sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Servidor TCP calculadora remota")
    parser.add_argument("--host", default="0.0.0.0", help="IP a enlazar (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=9999, help="Puerto a usar (default: 9999)")
    args = parser.parse_args()
    main(args.host, args.port)
