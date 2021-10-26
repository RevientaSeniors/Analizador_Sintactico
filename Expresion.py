class ExpresionLiteral():
    def __init__(self,tipo,valor):
        self.tipo = tipo
        self.valor = valor

    def get_tipo(self):
        return self.tipo

    def get_valor(self):
        return self.tipo

class ExpresionIdentificador() :
    def __init__(self, id) :
        self.id = id

    def get_Valor(self, entorno):
        return entorno.get(self.id)
        