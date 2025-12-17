import os
from Autenticador.main import Finance


def main():
    print("=== Valores Económicos (fuentes alternas) ===\n")
    finance = Finance()

    indicadores = {
        "Dólar": finance.get_usd,
        "Euro": finance.get_eur,
        "UF": finance.get_uf,
        "IVP": finance.get_ivp,
        "IPC": finance.get_ipc,
        "UTM": finance.get_utm,
    }

    resultados = {}
    for nombre, func in indicadores.items():
        try:
            valor = func(None)
            resultados[nombre] = valor
        except Exception as e:
            resultados[nombre] = None
            print(f"Error consultando {nombre}: {e}")

    for nombre, valor in resultados.items():
        if valor is not None:
            print(f"{nombre}: {valor} CLP")
        else:
            print(f"{nombre}: Error al obtener el valor.")


if __name__ == "__main__":
    main()