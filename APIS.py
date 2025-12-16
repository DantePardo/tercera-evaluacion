import requests

# URL base de la API
BASE_URL = "https://mindicador.cl/api"

def obtener_indicador(indicador):
    """Consulta un indicador específico desde la API."""
    try:
        response = requests.get(f"{BASE_URL}/{indicador}")
        data = response.json()
        return data["serie"][0]["valor"]
    except Exception as e:
        print(f"Error obteniendo {indicador}: {e}")
        return None

def main():
    print("=== Valores Económicos desde mindicador.cl ===\n")

    indicadores = {
        "UF": "uf",
        "IVP": "ivp",
        "IPC": "ipc",
        "UTM": "utm",
        "Dólar": "dolar",
        "Euro": "euro"
    }

    resultados = {}

    for nombre, clave in indicadores.items():
        valor = obtener_indicador(clave)
        resultados[nombre] = valor

    # Mostrar resultados
    for nombre, valor in resultados.items():
        if valor is not None:
            print(f"{nombre}: {valor} CLP")
        else:
            print(f"{nombre}: Error al obtener el valor.")

if __name__ == "__main__":
    main()