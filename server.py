import socket
import threading

# Función para calcular IMC
def calcular_imc(peso, altura):
    try:
        imc = peso / (altura ** 2)
        if imc < 18.5:
            estado = "Bajo peso"
        elif 18.5 <= imc < 25:
            estado = "Normal"
        elif 25 <= imc < 30:
            estado = "Sobrepeso"
        else:
            estado = "Obesidad"
        return f"Tu IMC es {imc:.2f} ({estado})"
    except Exception as e:
        return f"Error en el cálculo: {e}"

# Manejo de cada cliente
def manejar_cliente(conn, addr):
    print(f"[+] Conexión entrante desde {addr}")
    try:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            return
        print(f"[>] Datos recibidos: {data}")

        # Esperamos recibir "peso|altura"
        try:
            peso_str, altura_str = data.split('|')
            peso = float(peso_str)
            altura = float(altura_str)
        except ValueError:
            conn.sendall("Error: formato incorrecto. Usa peso|altura".encode('utf-8'))
            return

        resultado = calcular_imc(peso, altura)
        conn.sendall(resultado.encode('utf-8'))

    except Exception as e:
        print(f"[!] Error con cliente {addr}: {e}")
    finally:
        conn.close()
        print(f"[-] Conexión cerrada con {addr}")

# Servidor principal
def iniciar_servidor(host='0.0.0.0', port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[+] Servidor escuchando en {host}:{port}")

    while True:
        conn, addr = server.accept()
        hilo = threading.Thread(target=manejar_cliente, args=(conn, addr))
        hilo.start()

if __name__ == "__main__":
    iniciar_servidor()


