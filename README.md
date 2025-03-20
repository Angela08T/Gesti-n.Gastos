# Gesti-n.Gastos
RETO TECNICO

Repositorio:
git https://github.com/Angela08T/Gesti-n.Gastos.git

## **Carpeta de proyecto**
cd gestion-gastos

1. Ejecuta la aplicacion:
python main.py

2. Sigue las instrucciones en el menú:

   1. Agregar gasto: Ingresa el título, motivo, fecha y monto del gasto.

   2. Actualizar gasto: Actualiza los detalles de un gasto existente.

   3. Eliminar gasto: Elimina un gasto de la lista.

   4. Listar gastos: Muestra todos los gastos registrados.

   5. Filtrar gastos por mes: Filtra los gastos por mes (formato MM).

   6. Salir: Guarda los gastos en el archivo gastos.json y cierra la aplicación.

## **Estructura del Proyecto**

gestion-gastos/
│
├── main.py                # Punto de entrada de la aplicación.
├── gasto.py               # Clase Gasto y lógica relacionada.
├── gestor_gastos.py       # Lógica de negocio y gestión de gastos.
├── storage.py             # Manejo de almacenamiento persistente.
├── tests/                 # Pruebas unitarias.
│   └── test_gestor_gastos.py
└── README.md              # Documentación del proyecto.

## **Pruebas**
El proyecto incluye pruebas unitarias para garantizar el correcto funcionamiento del código. 

Para ejecutar las pruebas:

1. Navega a la carpeta del proyecto:
cd gestion-gastos

3. Ejecuta las pruebas:
python -m unittest discover tests

## **Recomendaciones**

### **1. Interfaz Gráfica**
Si deseas mejorar la experiencia del usuario, considera implementar una interfaz gráfica utilizando bibliotecas como `Tkinter` o `PyQt`. Esto permitiría una interacción más intuitiva con la aplicación.

### **2. Validación de Datos**
Para mejorar la robustez del proyecto, agrega validaciones en los datos ingresados por el usuario. Por ejemplo:
- Verifica que las fechas estén en el formato correcto (`YYYY-MM-DD`).
- Asegúrate de que los montos sean números positivos.

### **3. Base de Datos**
Si el proyecto crece en complejidad, considera migrar el almacenamiento de gastos a una base de datos como SQLite, MySQL o PostgreSQL. Esto permitiría manejar grandes volúmenes de datos de manera más eficiente.
