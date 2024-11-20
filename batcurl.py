#!/usr/bin/env python3
import json
import subprocess
import sys
from urllib.parse import urlencode
import argparse


def read_json_file(file):
    """Leer un archivo JSON y retornar los datos."""
    try:
        with open(file, "r") as json_file:
            return json.load(json_file)
    except Exception as e:
        print(f"ERROR: No se pudo leer el archivo JSON: {e}")
        return {}


def construct_url(url, get_params):
    """Construir la URL con parámetros GET."""
    return f"{url}?{urlencode(get_params)}" if get_params else url


def construct_post_data(post_params):
    """Construir los datos POST."""
    return urlencode(post_params) if post_params else None


def build_curl_command(url, post_data, get_params):
    """Construir el comando curl."""
    curl_command = ["curl", "-s", "-X", "POST" if post_data else "GET", url]
    if post_data:
        curl_command += ["-d", post_data]
    return curl_command


def execute_curl(curl_command):
    """Ejecutar el comando curl y retornar el resultado."""
    return subprocess.run(curl_command, capture_output=True, text=True)


def handle_response(result, response_only, curl_command, output_file):
    """Manejar la respuesta de la solicitud."""
    if result.returncode != 0:
        print("Error en la solicitud:", result.stderr)
        return

    # Mostrar la respuesta si `--respuesta` no está habilitado
    if not response_only:
        print("Estado:", result.returncode)
        print("Comando ejecutado:", " ".join(curl_command))

    # Imprimir o guardar la respuesta
    if result.stdout:
        if output_file:
            with open(output_file, "w") as f:
                f.write(result.stdout)
            print(f"Respuesta guardada en: {output_file}")
        else:
            print(result.stdout)

    if result.stderr:
        print("Error:")
        print(result.stderr)


def make_request_with_curl(
    file=None,
    url=None,
    get_params=None,
    post_params=None,
    response_only=False,
    output_file=None,
):
    try:
        data = {}
        if file:
            data = read_json_file(file)

        # Determinar la URL (prioridad: CLI > JSON)
        url = url or data.get("url", None)
        if not url:
            raise ValueError(
                "Se debe especificar una URL ya sea en el archivo JSON o con el parámetro --url."
            )

        get_params = {**data.get("get", {}), **(get_params or {})}
        post_params = {**data.get("post", {}), **(post_params or {})}

        full_url = construct_url(url, get_params)

        post_data = construct_post_data(post_params)

        curl_command = build_curl_command(full_url, post_data, get_params)

        result = execute_curl(curl_command)

        handle_response(result, response_only, curl_command, output_file)

    except Exception as e:
        print(f"ERROR: {e}")


# Punto de entrada
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Herramienta para realizar solicitudes HTTP con curl y manejar datos JSON."
    )
    parser.add_argument(
        "-f", "--file", help="Archivo JSON con los datos de la solicitud."
    )
    parser.add_argument(
        "-u", "--url", help="URL para la solicitud (prioridad sobre archivo JSON)."
    )
    parser.add_argument(
        "-g",
        "--get",
        nargs="*",
        help="Parámetros GET en formato clave=valor.",
        default=[],
    )
    parser.add_argument(
        "-p",
        "--post",
        nargs="*",
        help="Parámetros POST en formato clave=valor.",
        default=[],
    )
    parser.add_argument(
        "-r",
        "--respuesta",
        action="store_true",
        help="Muestra solo la respuesta de la solicitud.",
    )
    parser.add_argument(
        "-o", "--output", help="Nombre del archivo para guardar la respuesta."
    )

    args = parser.parse_args()

    # Convertir parámetros GET y POST de listas a diccionarios
    get_params = dict(param.split("=", 1) for param in args.get) if args.get else {}
    post_params = dict(param.split("=", 1) for param in args.post) if args.post else {}

    # Llamar a la función principal
    make_request_with_curl(
        file=args.file,
        url=args.url,
        get_params=get_params,
        post_params=post_params,
        response_only=args.respuesta,
        output_file=args.output,
    )
