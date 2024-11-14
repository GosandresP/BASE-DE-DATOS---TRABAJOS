from pymongo import MongoClient
import matplotlib.pyplot as plt

def conectar_mongodb():
    # Configura la conexión a MongoDB
    cliente = MongoClient("mongodb://localhost:27017/")  # Cambia la URI si es necesario
    base_datos = cliente["bdworking"]  # Reemplaza por el nombre de tu base de datos
    coleccion = base_datos["work"]  # Reemplaza por el nombre de tu colección
    return coleccion

# Conectar con la colección en MongoDB
coleccion = conectar_mongodb()

# Obtener datos de la colección
datos = coleccion.find({}, {"NOMBRE": 1, "AFORO": 1, "_id": 0}).sort("AFORO", -1).limit(8)  # Limitar a los 8 mejores

# Preparar listas para los datos
nombres = []
aforos = []

# Extraer datos de los documentos de MongoDB
for dato in datos:
    nombres.append(dato["NOMBRE"])
    aforos.append(dato["AFORO"])

# Limitar la longitud de los nombres para una mejor visualización
nombres_acortados = [nombre if len(nombre) <= 20 else nombre[:17] + '...' for nombre in nombres]

# Graficar los datos
plt.figure(figsize=(14, 8))  # Aumentar el tamaño de la figura
plt.barh(nombres_acortados, aforos, color='skyblue')
plt.xlabel("Aforo", fontsize=14)
plt.ylabel("Nombre del Restaurante", fontsize=14)
plt.title("Top 8 Restaurantes por Aforo", fontsize=16)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Rotar las etiquetas del eje Y para mejorar la legibilidad
plt.yticks(rotation=0, fontsize=12)  # Mantener las etiquetas horizontales

# Ajustar las etiquetas y el diseño
plt.xticks(fontsize=12)
plt.tight_layout()  # Ajusta el diseño para que no se corten las etiquetas

# Mostrar el gráfico
plt.show()

#hola mundo