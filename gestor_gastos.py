class GestorGastos:
    def __init__(self):
        self.gastos =[]

    def agregar_gasto(self, gasto):
        self.gastos.append(gasto)

    def actualizar_gasto(self, indice, nuevo_gasto):
        if 0 <= indice < len(self.gastos):
            self.gastos[indice] = nuevo_gasto
        else:
            raise ValueError("Indice de gasto no valido")
        
    def eliminar_gasto(self, indice):
        if 0 <= indice < len(self.gastos):
            self.gastos.pop(indice)
        else:
            raise ValueError("Indice de gasto no valido")
        
    def listar_gastos(self):
        return self.gastos
    
    def filtrar_gastos_por_mes(self, mes):
        return [gasto for gasto in self.gastos if gasto.fecha.split("-")[1] == mes]
    
    