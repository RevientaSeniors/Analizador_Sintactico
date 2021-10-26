class InsImprimir():
    def __init__(self, cadena):
        self.cadena = cadena.replace('"',"")
        return print(self.cadena, end=" ")

class InsImprimirln():
    def __init__(self, cadena):
        self.cadena = cadena.replace('"',"")
        return print("\n"+self.cadena)

class InsClaves():
    def __init__(self,claves):
        self.claves = claves
        for clave in self.claves:
            print(clave)

class InsRegistros():
    def __init__(self,registros):
        self.registros = registros
        for registro in self.registros:
            print(registro)

    def cantidadReg(self):
        cantidad = len(self.registros)
        print("La cantidad de registros es: ",cantidad)
    
class InsPromedio():
    def __init__(self, campo, claves, registros):
        self.campo = campo
        self.claves = claves
        self.registros = registros
        self.suma = 0

        for i in range(len(claves)):
            if  self.campo == self.claves[i]:
                for j in range(len(self.registros)):
                    self.suma+= int(registros[j][i])
        
        self.promedio = self.suma/ len(self.registros)
        print("el promedio es: ", self.promedio)

class InsContarSi():
    def __init__(self,campo,numero,claves,registros):
        self.campo = campo
        self.numero = numero
        self.claves = claves
        self.registros = registros
        self.contador = 0

        for i in range(len(claves)):
            if  self.campo == self.claves[i]:

                for j in range(len(self.registros)):
                    if int(self.registros[j][i]) == int(self.numero):
                        self.contador+=1
        print("En el campo: ",self.campo, " hay ", self.contador)

class InsDatos():
    def __init__(self, claves, registros):
        self.claves = claves
        self.registros = registros

class InsSuma():
    def __init__(self, campo, claves, registros):
        self.campo = campo
        self.claves = claves
        self.registros = registros
        self.suma = 0

        for i in range(len(claves)):
            if  self.campo == self.claves[i]:
                for j in range(len(self.registros)):
                    self.suma+= int(registros[j][i])
        
        print("La suma es: ", self.suma)


class InsMax():
    def __init__(self, campo, claves, registros):
        self.campo = campo
        self.claves = claves
        self.registros = registros
        self.listanums = []

        for i in range(len(claves)):
            if  self.campo == self.claves[i]:
                for j in range(len(self.registros)):
                    self.listanums.append(registros[j][i])
        
        print("El número máximo es: ", max(self.listanums))

class InsMin():
    def __init__(self, campo, claves, registros):
        self.campo = campo
        self.claves = claves
        self.registros = registros
        self.listanums = []

        for i in range(len(claves)):
            if  self.campo == self.claves[i]:
                for j in range(len(self.registros)):
                    self.listanums.append(registros[j][i])
        
        print("El número mínimo es: ", min(self.listanums))

class InsReporte():
    def __init__(self, nombre, claves, registros):
        self.nombre = nombre.replace('"',"")
        self.nombre+=".html"
        self.claves = claves
        self.registros = registros

        documento = open(self.nombre,'w')
        mensaje = """
    <!DOCTYPE html>
        <html lang="en">
            <head>
                <title> NOTAS </title>
            </head>
                <body>
                    <h1> DATOS </h1>
                    <table class="default" border="1">
                        <thead>
				            <tr>
					            <th colspan="2">""" +self.nombre+ """</th>
				            </tr>
			            </thead>
                        <tr>
                        """
        for clave in self.claves:
            mensaje +=""" 
                            <th>"""+clave+""" </th>
                        """

        mensaje+=""" 
                        </tr>
                     """
        for i in range(len(self.registros)):
            mensaje += """
                        <tr> 
                        """
            for j in range(len(self.registros[i])):
                mensaje += """    
                            <td>"""+self.registros[i][j]+""" </td>    
                    """
        mensaje += """
                        </tr>
                    </table>
                    """
        mensaje += """       
                </body>
        </html>"""
        documento.write(mensaje)
        documento.close()