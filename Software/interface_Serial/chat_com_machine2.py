import tkinter as tk
from tkinter import scrolledtext
import threading
import serial

# Función para enviar el mensaje a través del puerto serie
def enviar_mensaje():
    mensaje = enviar_entry.get()
    enviar_entry.delete(0, tk.END)
    chat_log.insert(tk.END, f"Yo: {mensaje}\n")
    ser.write(mensaje.encode())

# Función para leer mensajes del puerto serie
def leer_mensajes():
    while True:
        try:
            mensaje = ser.readline().decode().strip()
            if mensaje:
                chat_log.insert(tk.END, f"Otro: {mensaje}\n")
                chat_log.see(tk.END)  # Desplazar automáticamente hacia abajo
        except Exception as e:
            print("Error al leer mensaje:", e)

# Crear la interfaz de chat
root = tk.Tk()
root.title("Chat Serial Machine 2")

# Crear la caja de chat
chat_log = scrolledtext.ScrolledText(root, height=15, width=50)
chat_log.pack(padx=10, pady=10)

# Crear la entrada de mensaje y botón de enviar
enviar_entry = tk.Entry(root, width=40)
enviar_entry.pack(padx=10, pady=5)

enviar_button = tk.Button(root, text="Enviar", command=enviar_mensaje)
enviar_button.pack(padx=10, pady=5)

# Abrir el puerto serie COM6
ser = serial.Serial('COM9', 9600, timeout=0.1)  # Añadimos un tiempo de espera

# Iniciar el hilo para leer mensajes
leer_hilo = threading.Thread(target=leer_mensajes)
leer_hilo.daemon = True
leer_hilo.start()

# Iniciar la interfaz
root.mainloop()

# Cerrar el puerto serie al salir
ser.close()
