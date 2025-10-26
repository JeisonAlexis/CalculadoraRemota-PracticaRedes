<div align="center">
  <img 
    src="https://raw.githubusercontent.com/JeisonAlexis/CalculadoraRemota-PracticaRedes/main/assets/redesBanner.svg"
    alt="Banner animado"
    style="width: 50%; max-width: 350px; height: auto; border-radius: 10px;" />
</div>

## <picture><img src = "https://github.com/7oSkaaa/7oSkaaa/blob/main/Images/about_me.gif?raw=true" width = 50px></picture> Trabajo Practico TCP IMC remoto


<div style="padding:10px;border-radius:8px;margin-bottom:8px;background:#f7f7f7;">
      <strong>1️⃣ Paso 1:</strong>
      <p style="margin:.25rem 0 0 0;">Entre en modo <strong>super usuario</strong> o <strong>root</strong> en el sistema que va ser el <strong>servidor</strong>.</p>
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
      <p style="margin:.25rem 0 0 0;">Ejecuta el servidor para que este escuchando las solicitudes.</p>
</div>

```bash
python3 server.py --host 0.0.0.0 --port 9999
# Salida esperada de este comado es: [+] Servidor escuchando en 0.0.0.0:9999. Ctrl+C para salir.
```

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <strong>🔟 Paso 10:</strong>
      <p style="margin:.25rem 0 0 0;">Siga el flujo de ejecucion del Jupyter pero ten en cuenta que en la variable "carpeta" debe estar tu ruta de la carpeta de imagenes <strong>Ej: carpeta = r"C:\Users\jeyco\Documents\GitHub\FiltradoEspacio\images\imagenes"</strong>.</p>
</div>

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <strong>1️⃣1️⃣ Paso 11:</strong>
      <p style="margin:.25rem 0 0 0;">Descargar los archivos de la ruta <strong>/codigos/</strong> de este <strong>Repositorio</strong> y muevelos a la carpeta de esta <strong>practica</strong>.</p>
</div>

<div style="padding:10px;border-radius:8px;background:#f7f7f7;">
      <strong>1️⃣2️⃣ Paso 12:</strong>
      <p style="margin:.25rem 0 0 0;">Abrir el archivo en VisualStudio y ejecutar los siguientes comandos para la compilacion y ejecucion: <strong>practica</strong>.</p>
</div>


```bash
-- Recuerda ejecutar estos comandos en la ruta .\codigos\
gcc filtros.c pgm_utils.c -o filtros -fopenmp
.\filtros.exe
```

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
