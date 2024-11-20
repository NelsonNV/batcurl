# batcurl.py

`batcurl.py` es una herramienta de línea de comandos en Python que utiliza `curl` para realizar solicitudes HTTP. Permite configurar tanto los parámetros `GET` como `POST` mediante un archivo JSON o a través de la línea de comandos. Además, ofrece opciones para guardar la respuesta en un archivo o mostrar solo la respuesta sin detalles adicionales.

## Requisitos

- Python 3.x
- `curl` instalado en el sistema

## Instalación

1. Asegúrate de tener `curl` instalado en tu sistema.
2. Descarga el archivo `batcurl.py` y asegúrate de que tenga permisos de ejecución:

```bash
chmod +x batcurl.py
```

3. Ejecuta el script directamente desde la línea de comandos.

## Uso

### Sintaxis básica:

```bash
./batcurl.py [-f archivo_json] [-u url] [-g parametros_get] [-p parametros_post] [-r] [-o archivo_salida]
```

### Descripción de parámetros:

- `-f, --file`: **(Opcional)** Especifica un archivo JSON que contiene la configuración de la solicitud. El archivo JSON puede incluir la URL, parámetros `GET` y `POST`. Si se especifica un archivo, este tiene prioridad sobre otros parámetros de línea de comandos.
  
  Ejemplo de archivo JSON:
  ```json
  {
      "url": "https://api.ejemplo.com/datos",
      "get": {
          "usuario": "1234"
      },
      "post": {
          "nombre": "Juan",
          "apellido": "Pérez"
      }
  }
  ```

- `-u, --url`: **(Opcional)** Especifica directamente la URL para la solicitud. Si no se usa `-f` (archivo JSON), este parámetro es obligatorio.

  Ejemplo:
  ```bash
  ./batcurl.py -u "https://api.ejemplo.com/datos"
  ```

- `-g, --get`: **(Opcional)** Define los parámetros `GET` como pares clave=valor. Pueden pasarse múltiples parámetros.

  Ejemplo:
  ```bash
  ./batcurl.py -u "https://api.ejemplo.com/datos" -g "usuario=1234" -g "ciudad=Buenos Aires"
  ```

- `-p, --post`: **(Opcional)** Define los parámetros `POST` como pares clave=valor. También pueden pasarse múltiples parámetros.

  Ejemplo:
  ```bash
  ./batcurl.py -u "https://api.ejemplo.com/enviar" -p "nombre=Juan" -p "edad=30"
  ```

- `-r, --respuesta`: **(Opcional)** Si se especifica, solo se mostrará la respuesta de la solicitud HTTP (sin detalles adicionales como el estado o el comando ejecutado).

  Ejemplo:
  ```bash
  ./batcurl.py -u "https://api.ejemplo.com/datos" -g "usuario=1234" -p "ciudad=Buenos Aires" -r
  ```

- `-o, --output`: **(Opcional)** Especifica un archivo donde guardar la respuesta de la solicitud. Si no se proporciona, la respuesta se muestra directamente en la consola.

  Ejemplo:
  ```bash
  ./batcurl.py -u "https://api.ejemplo.com/datos" -g "usuario=1234" -o "respuesta.json"
  ```

### Ejemplos de uso:

1. **Realizar una solicitud `GET` con parámetros de la URL**:
   ```bash
   ./batcurl.py -u "https://api.ejemplo.com/datos" -g "usuario=1234"
   ```

2. **Realizar una solicitud `POST` con parámetros**:
   ```bash
   ./batcurl.py -u "https://api.ejemplo.com/enviar" -p "nombre=Juan" -p "edad=30"
   ```

3. **Usar un archivo JSON para configurar la solicitud**:
   ```bash
   ./batcurl.py -f datos_solicitud.json
   ```

4. **Mostrar solo la respuesta sin detalles adicionales**:
   ```bash
   ./batcurl.py -u "https://api.ejemplo.com/datos" -g "usuario=1234" -p "ciudad=Buenos Aires" -r
   ```

5. **Guardar la respuesta en un archivo**:
   ```bash
   ./batcurl.py -u "https://api.ejemplo.com/datos" -g "usuario=1234" -o "respuesta.json"
   ```

## Manejo de Errores

- Si no se proporciona una URL mediante el archivo JSON o el parámetro `-u`, el script generará un error y no ejecutará la solicitud.
- Si el archivo JSON no se puede leer o contiene datos inválidos, el script también generará un error.

## Contribuciones

Si deseas contribuir, puedes hacer un fork de este repositorio y enviar tus cambios mediante un pull request. Cualquier mejora o corrección será bienvenida.

