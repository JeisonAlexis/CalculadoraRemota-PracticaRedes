import socket
import tkinter as tk
from tkinter import messagebox

# --- Configuración del servidor ---
SERVER_HOST = "192.168.101.83"  # Cambia por la IP de tu servidor 
SERVER_PORT = 9999

# --- Función para enviar datos al servidor ---
def enviar_datos():
    try:
        peso = entry_peso.get()
        altura = entry_altura.get()

        # Validar datos
        if not peso or not altura:
            messagebox.showwarning("Datos incompletos", "Por favor ingresa peso y altura.")
            return

        # Crear socket TCP
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))

        # Enviar datos al servidor
        mensaje = f"{peso},{altura}"
        client_socket.send(mensaje.encode())

        # Recibir resultado
        resultado = client_socket.recv(1024).decode()
        client_socket.close()

        # Mostrar resultado en ventana
        label_resultado.config(text=f"Tu IMC es: {resultado}", fg="green")

    except Exception as e:
        messagebox.showerror("Error de conexión", f"No se pudo conectar al servidor.\n\n{e}")

# --- Interfaz gráfica (Tkinter) ---
root = tk.Tk()
root.title("Calculadora de IMC Remota")
root.geometry("350x250")
root.config(bg="#f3f3f3")

# Título
titulo = tk.Label(root, text="Calculadora IMC", font=("Arial", 16, "bold"), bg="#f3f3f3")
titulo.pack(pady=10)

# Campo de peso
tk.Label(root, text="Peso (kg):", bg="#f3f3f3").pack()
entry_peso = tk.Entry(root, justify="center")
entry_peso.pack(pady=5)

# Campo de altura
tk.Label(root, text="Altura (m):", bg="#f3f3f3").pack()
entry_altura = tk.Entry(root, justify="center")
entry_altura.pack(pady=5)

# Botón calcular
btn_calcular = tk.Button(root, text="Calcular IMC", command=enviar_datos, bg="#4CAF50", fg="white", font=("Arial", 12))
btn_calcular.pack(pady=15)

# Resultado
label_resultado = tk.Label(root, text="", font=("Arial", 12), bg="#f3f3f3")
label_resultado.pack()

# Iniciar ventana
root.mainloop()
