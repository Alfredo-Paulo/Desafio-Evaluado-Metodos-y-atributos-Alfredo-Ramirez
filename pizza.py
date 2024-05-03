class Pizza:
    ingredientes_carnicos = ["pollo", "vacuno", "carne vegetal"]
    ingredientes_vegetales = ["tomate", "aceitunas", "champiñones"]
    tipos_masa = ["tradicional", "delgada"]

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        return elemento in valores_posibles

    def __init__(self):
        self.ingrediente_proteico = None
        self.ingrediente_vegetal1 = None
        self.ingrediente_vegetal2 = None
        self.tipo_masa = None
        self.es_valida = False

    def realizar_pedido(self):
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico: ")
        self.ingrediente_vegetal1 = input("Ingrese el primer ingrediente vegetal: ")
        self.ingrediente_vegetal2 = input("Ingrese el segundo ingrediente vegetal: ")
        self.tipo_masa = input("Ingrese el tipo de masa (tradicional/delgada): ")

        self.es_valida = (
            self.validar_elemento(self.ingrediente_proteico, self.ingredientes_carnicos)
            and self.validar_elemento(self.ingrediente_vegetal1, self.ingredientes_vegetales)
            and self.validar_elemento(self.ingrediente_vegetal2, self.ingredientes_vegetales)
            and self.validar_elemento(self.tipo_masa, self.tipos_masa)
        )

        if not self.es_valida:
            print("Pedido no válido. Revise los ingredientes y tipo de masa.")

