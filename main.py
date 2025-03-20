from gestor_gastos import GestorGastos
from storage import cargar_gastos, guardar_gastos
from gasto import Gasto 

def main():
    gestor = GestorGastos()
    gestor.gastos = cargar_gastos()

    while True:
        print("\n--- Gestion de Gastos ---")
        print("1. Agregar gasto")
        print("2. Actualizar gasto")
        print("3. Eliminar gasto")
        print("4. Listar gastos")
        print("5. Filtrar gastos por mes")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion =="1":
            titulo = input("Titulo: ")
            motivo = input("Motivo: ")
            fecha = input("Fecha (YYYY-MM-DD): ")
            monto = float(input("Monto: "))
            gestor.agregar_gasto(Gasto(titulo, motivo, fecha, monto))

        elif opcion == "2":
            indice = int(input("Indice del gasto a actualizar: "))
            titulo = input("Nuevo Titulo: ")
            motivo = input("Nuevo motivo: ")
            fecha = input("Nueva fecha (YYYY-MM-DD): ")
            monto = float(input("Nuevo monto: "))
            gestor.actualizar_gasto(indice, Gasto(titulo, motivo, fecha, monto))

        elif opcion == "3":
            indice = int(input("Indice del gasto a eliminar: "))
            gestor.eliminar_gasto(indice)

        elif opcion == "4":
            for i, gasto in enumerate(gestor.listar_gastos()):
                print(f"{i}. {gasto}")

        elif opcion == "5":
            mes = input("Mes a flitrar (MM): ")
            gastos_filtrados = gestor.filtrar_gastos_por_mes(mes)
            for gasto in gastos_filtrados:
                print(gasto)
        
        elif opcion == "6":
            guardar_gastos(gestor.gastos)
            print("Saliendo...")
            break
        
        else:
            print("Opcion no valida. Intente de nuevo.")

if __name__ == "__main__":
    main()

