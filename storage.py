import json

def guardar_gastos(gastos, archivo ="gastos.json"):
    with open(archivo, "w") as f:
        json.dump([gasto.__dict__ for gasto in gastos], f)

def cargar_gastos(archivo="gastos.json"):
    try:
        with open(archivo, "r") as f:
            datos = json.load(f)
            return [gasto(**gasto) for gasto in datos]
    except FileNotFoundError:
        return []
    