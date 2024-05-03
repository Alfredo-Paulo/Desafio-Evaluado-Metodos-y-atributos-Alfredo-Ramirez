from pizza import Pizza

# a. Mostrar los atributos de clase de la clase importada
print("Ingredientes cárnicos:", Pizza.ingredientes_carnicos)
print("Ingredientes vegetales:", Pizza.ingredientes_vegetales)
print("Tipos de masa:", Pizza.tipos_masa)

# b. Verificar si un elemento está presente en una lista
print("¿El elemento 'salsa de tomate' está presente en la lista?",
      Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# c. Realizar un pedido
mi_pedido = Pizza()
mi_pedido.realizar_pedido()

# d. Mostrar los ingredientes y tipo de masa del pedido realizado
if mi_pedido.es_valida:
    print("Ingredientes vegetales:", mi_pedido.ingrediente_vegetal1, ",", mi_pedido.ingrediente_vegetal2)
    print("Ingrediente proteico:", mi_pedido.ingrediente_proteico)
    print("Tipo de masa:", mi_pedido.tipo_masa)
    print("¿Es una pizza válida?", mi_pedido.es_valida)

# e. Verificar si la clase Pizza es válida o no
print("¿Es la clase Pizza una pizza válida?", Pizza().es_valida)
