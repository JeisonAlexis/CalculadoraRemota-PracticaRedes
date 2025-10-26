import socket
import tkinter as tk
from tkinter import messagebox

# --- Configuración del servidor ---
SERVER_HOST = "192.168.101.73"  # Cambia por la IP de tu servidor
SERVER_PORT = 9999

# --- Función para enviar datos al servidor ---
def enviar_datos():
    try:
        peso = entry_peso.get().strip()
        altura = entry_altura.get().strip()

        # Validar datos
        if not peso or not altura:
            messagebox.showwarning("Datos incompletos", "Por favor ingresa peso y altura.")
            return

        # Crear socket TCP
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))

        # Enviar datos al servidor
        mensaje = f"{peso}|{altura}"
        client_socket.sendall(mensaje.encode("utf-8"))

        # Recibir resultado
        resultado = client_socket.recv(1024).decode("utf-8")
        client_socket.close()

        # Mostrar resultado en ventana
        label_resultado.config(text=f"Resultado: {resultado}", fg="#2E7D32")

    except Exception as e:
        messagebox.showerror("Error de conexión", f"No se pudo conectar al servidor.\n\n{e}")

# --- Interfaz gráfica (Tkinter) ---
root = tk.Tk()
root.title("💻 Calculadora de IMC Remota")
root.geometry("400x320")
root.resizable(False, False)
root.config(bg="#E3F2FD")

# --- Marco principal ---
frame = tk.Frame(root, bg="white", bd=2, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center", width=340, height=280)

# --- Título ---
titulo = tk.Label(frame, text="Calculadora de IMC", font=("Segoe UI", 16, "bold"), bg="white", fg="#0D47A1")
titulo.pack(pady=(15, 10))

# --- Campo de peso ---
tk.Label(frame, text="Peso (kg):", bg="white", font=("Segoe UI", 11)).pack()
entry_peso = tk.Entry(frame, justify="center", font=("Segoe UI", 11), bd=1, relief="solid")
entry_peso.pack(pady=5, ipadx=5, ipady=3)

# --- Campo de altura ---
tk.Label(frame, text="Altura (m):", bg="white", font=("Segoe UI", 11)).pack()
entry_altura = tk.Entry(frame, justify="center", font=("Segoe UI", 11), bd=1, relief="solid")
entry_altura.pack(pady=5, ipadx=5, ipady=3)

# --- Label de resultado ---
label_resultado = tk.Label(frame, text="", font=("Segoe UI", 12, "bold"), bg="white", fg="#2E7D32")
label_resultado.pack(pady=(10, 5))

# --- Botón con animación ---
def on_enter(e): btn_calcular.config(bg="#1B5E20")
def on_leave(e): btn_calcular.config(bg="#4CAF50")

btn_calcular = tk.Button(
    frame, text="Calcular IMC", command=enviar_datos,
    bg="#4CAF50", fg="white", font=("Segoe UI", 11, "bold"),
    relief="flat", cursor="hand2", activebackground="#43A047"
)
btn_calcular.pack(pady=10, ipadx=10, ipady=5)
btn_calcular.bind("<Enter>", on_enter)
btn_calcular.bind("<Leave>", on_leave)

# --- Pie de ventana ---
footer = tk.Label(root, text="Servidor TCP | Proyecto IMC", bg="#E3F2FD", fg="#1565C0", font=("Segoe UI", 9))
footer.pack(side="bottom", pady=5)

# --- Iniciar ventana ---
root.mainloop()

