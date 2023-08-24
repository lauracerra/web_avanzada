productos_lista = [
    {'id': 1, 'nombre': 'televisor', 'precio': 800, 'id_categoria': 1},
    {'id': 2, 'nombre': 'escritorio en L 62cm', 'precio': 100, 'id_categoria': 2},
    # Agrega más productos aquí si es necesario
]

categorias_diccionario = {
    1: 'tecnologia',
    2: 'decoracion',
    # Agrega más categorías aquí si es necesario
}

# Crear un diccionario combinado con nombre del artículo y su tipo
articulos_con_tipos = {}

for producto in productos_lista:
    producto_id = producto['id']
    nombre_articulo = producto['nombre']
    id_tipo = producto['id_categoria']
    nombre_tipo = categorias_diccionario.get(id_tipo, 'Tipo desconocido')
    
    articulos_con_tipos[nombre_articulo] = nombre_tipo

# Mostrar el diccionario resultante
for articulo, tipo in articulos_con_tipos.items():
    print(f"Artículo: {articulo} - Tipo: {tipo}")


