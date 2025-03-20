class Gasto:
    def __init__(self, titulo, motivo, fecha, monto):
        self.titulo = titulo
        self.motivo = motivo
        self.fecha = fecha
        self.monto = monto

    def __str__(self):
        return f"{self.titulo} - {self.motivo} - {self.fecha} - ${self.monto: 2f}"
    
    