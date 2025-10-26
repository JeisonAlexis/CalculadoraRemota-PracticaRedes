<div align="center">
  <img 
    src="https://raw.githubusercontent.com/JeisonAlexis/CalculadoraRemota-PracticaRedes/main/assets/redesBanner.svg"
    alt="Banner animado"
    style="width: 50%; max-width: 350px; height: auto; border-radius: 10px;" />
</div>

## <picture><img src = "https://github.com/7oSkaaa/7oSkaaa/blob/main/Images/about_me.gif?raw=true" width = 50px></picture> Trabajo Practico TCP IMC remoto


<div style="padding:10px;border-radius:8px;margin-bottom:8px;background:#f7f7f7;">
      <strong>1️⃣ Paso 1:</strong>
      <p style="margin:.25rem 0 0 0;">Entre en modo <strong>super usuario</strong> o <strong>root</strong> en el sistema que va ser el <strong>servidor</strong> en este caso Zorin Os en VM.</p>
</div>

```bash
sudo -i 
```

<div style="padding:10px;border-radius:8px;margin-bottom:8px;background:#f7f7f7;">
      <strong>2️⃣ Paso 2:</strong>
      <p style="margin:.25rem 0 0 0;">Realiza las <strong>actualizaciones de paquetes</strong> necesarias.</p>
</div>

```bash
sudo apt update
sudo apt upgrade -y
```

<div style="padding:10px;border-radius:8px;margin-bottom:8px;background:#f7f7f7;">
      <strong>3️⃣ Paso 3:</strong>
      <p style="margin:.25rem 0 0 0;">Instala Python 3.</p>
</div>

```bash
sudo apt install -y python3 python3-venv python3-pip
```

<div style="padding:10px;border-radius:8px;margin-bottom:8px;background:#f7f7f7;">
      <strong>4️⃣ Paso 4:</strong>
      <p style="margin:.25rem 0 0 0;">Ahora clona este <strong>Repositorio</strong>.</p>
</div>

```bash
git clone https://github.com/JeisonAlexis/CalculadoraRemota-PracticaRedes.git  
```

<div style="padding:10px;border-radius:8px;margin-bottom:8px;background:#f7f7f7;">
      <strong>5️⃣ Paso 5:</strong>
      <p style="margin:.25rem 0 0 0;">Para el paso anterior te pedira instalar Git (si no lo tienes instalado).</p>
</div>

```bash
sudo apt install git
```

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <strong>6️⃣ Paso 6:</strong>
      <p style="margin:.25rem 0 0 0;">Debes conocer la ip del sistemas que vas a ser el <strong>Servidor</strong></p>
</div>

```bash
ip addr
```

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <strong>7️⃣ Paso 7:</strong>
      <p style="margin:.25rem 0 0 0;">Ahora se debe abrir los puertos en este caso del <strong>Servidor</strong>.</p>
</div>

```bash
sudo apt install -y ufw
sudo ufw allow 22/tcp        
sudo ufw allow 9999/tcp      
sudo ufw enable
sudo ufw status verbose
```

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <strong>8️⃣ Paso 8:</strong>
      <p style="margin:.25rem 0 0 0;">Este paso es opcinal (pero recomendado) y es simplemete desactivar el <strong>firewall</strong>.</p>
</div>

```bash
sudo ufw disable
```

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <strong>9️⃣ Paso 9:</strong>
      <p style="margin:.25rem 0 0 0;">Ejecuta el servidor para que esté escuchando las solicitudes (recuerda que la ruta para ejecutar este comando es dentro de la carpeta creada por el repo).</p>
</div>

```bash
python3 server.py --host 0.0.0.0 --port 9999
# Salida esperada de este comado es: [+] Servidor escuchando en 0.0.0.0:9999. Ctrl+C para salir.
```

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <strong>🔟 Paso 10:</strong>
      <p style="margin:.25rem 0 0 0;">Ahora debemos configurar los clientes (estos clientes deben tener instalado Python3), para esta practica los clientes van a ser Ubunto en VM y Windows como sistema operativo nativo. Clona de nuevo el Repositorio</p>
</div>

```bash
git clone https://github.com/JeisonAlexis/CalculadoraRemota-PracticaRedes.git  
```

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <strong>1️⃣1️⃣ Paso 11:</strong>
      <p style="margin:.25rem 0 0 0;">Mandar datos al servidor (por consola) desde el Cliente Ubuntu (para ejecutar este comando ten en cuenta que la ruta debe ser dentro de la carpeta del repo)</p>
</div>


```bash
python3 client.py --server <ip-del-servidor> --port 9999
# Ejemplo de comando python3 client.py --server 192.168.101.83 --port 9999
```

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <strong>1️⃣2️⃣ Paso 12:</strong>
      <p style="margin:.25rem 0 0 0;">Ahora, si deseas algo un poco mas visual simplemente entra con tu editor de texto preferido al archivo "cliente_gui.py" del repo y cambia la variable "SERVER_HOST" por la ip de tu servidor.</p>
</div>


```bash
SERVER_HOST = "192.168.101.73"  # Cambia por la IP de tu servidor
```

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <strong>1️⃣3️⃣ Paso 13:</strong>
      <p style="margin:.25rem 0 0 0;">Finalmente si guardas los cambios del paso anterior y ejecutas el siguiente comando, podras enviar y recibir los datos del servidor de forma visual (no por la terminal).</p>
</div>


```bash
# Esta interfaz usa Tkinter por lo que si no lo tienes instalado antes debes ejecutar este comando: sudo apt install python3-tk -y
python3 client_gui.py
```

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <strong>1️⃣4️⃣ Paso 14:</strong>
      <p style="margin:.25rem 0 0 0;">Para hacer esto mismo pero en Windows el proceso es muy similar, clona el repo, cambia la ip a la del servidor y desde cmd entra a la ruta del repo, para finalmente ejecutar el comando.</p>
</div>

```bash
python client.py --server <ip-del-servidor> --port 9999       #Ingresar datos por Consola
python client_gui.py                                          #Ingresar datos por Interfaz grafica
```

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <strong>1️⃣5️⃣ Paso 15:</strong>
      <p style="margin:.25rem 0 0 0;">Ya para finalizar capturaremos el trafico de estas solicitudes al servidor con Wireshark desde Zorin OS (osea el Servidor).</p>
</div>

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <strong>1️⃣6️⃣ Paso 16:</strong>
      <p style="margin:.25rem 0 0 0;">Recuerda que se debe estar capturando en Wireshark cuando hagas las solicitudes, una vez realizadas terminas la captura y filtras por "tcp.port == 9999" y te saldran todos los paquetes relacionados con esta practica.</p>
</div>

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <strong>Para finalizar</strong>
      <p style="margin:.25rem 0 0 0;">Se subio el archivo de captura de red de Wireshark en este repo "practicaIMC.pcapng"</p>
      <p style="margin:.25rem 0 0 0;">👇👇 Tambien se subio a este repositorio la guia paso a paso con capturas "TrabajoTCP_Practico.pdf" y tambien lo tiene en formato web aca abajo.</p>
</div>

<div style="text-align:center; margin-bottom:15px;">
  <a href="https://jeisonalexis.github.io/documentoTecnicoCupido/index.html" target="_blank">
    📄 Documento Paso Paso
  </a>
</div>


<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=Bitcount+Grid+Single&weight=500&duration=3000&pause=1000&color=F5FF29&background=000000&center=true&vCenter=true&width=400&lines=Redes;TCP;Servidor+Remoto;Wireshark" alt="Typing SVG" />
  </a>
</p>



## <picture><img src = "https://raw.githubusercontent.com/JeisonAlexis/FiltradoEspacio/main/assets/equipo.gif" width = 50px></picture> Presentado Por:

<div style="padding:10px;border-radius:8px;margin-bottom:8px;background:#f7f7f7;">
      <li>Jeison Alexis Rodriguez Angarita</li>
</div>

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <li>Daniel Eduardo Davila Quintero</li>
</div>

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <br>
      <strong>👨‍💻 Redes</strong>
</div>

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <strong>🕒 2025</strong>
</div>

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <strong>👨‍🎓 Universidad de Pamplona</strong>
</div>
