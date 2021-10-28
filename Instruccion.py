
class InsImprimir():
    def __init__(self, cadena):
        self.cadena = cadena.replace('"',"")
        self.retornar()

    def retornar(self):    
        return self.cadena

class InsImprimirln():
    def __init__(self, cadena):
        self.cadena = cadena.replace('"',"")
        self.cadena = self.cadena+"\n"
        self.retornar()
        
    def retornar(self):    
        return self.cadena

class InsClaves():
    def __init__(self,claves):
        self.claves = claves
        #for clave in self.claves:
            #print(clave)

class InsRegistros():
    def __init__(self,registros):
        self.registros = registros
        #for registro in self.registros:
            #print(registro)

    def cantidadReg(self):
        cantidad = len(self.registros)
        cadena = "\nLa cantidad de registros es: "+ str(cantidad) + "\n"
        return cadena
    
class InsPromedio():
    def __init__(self, campo, claves, registros):
        self.campo = campo
        self.claves = claves
        self.registros = registros
        self.suma = 0
        self.cadena = ""

        for i in range(len(claves)):
            if  self.campo == self.claves[i]:
                for j in range(len(self.registros)):
                    self.suma+= int(registros[j][i])

        self.promedio = self.suma/ len(self.registros)
        self.retornar()

    def retornar(self):
        self.cadena = "\nEl promedio es: "+ str(self.promedio)+"\n"
        return self.cadena

class InsContarSi():
    def __init__(self,campo,numero,claves,registros):
        self.campo = campo
        self.numero = numero
        self.claves = claves
        self.registros = registros
        self.contador = 0
        self.cadena =""

        for i in range(len(claves)):
            if  self.campo == self.claves[i]:

                for j in range(len(self.registros)):
                    if int(self.registros[j][i]) == int(self.numero):
                        self.contador+=1
        self.retornar()

    def retornar(self):
        self.cadena= "\nEn el campo: "+self.campo+" hay "+ str(self.contador)+"\n"
        return self.cadena

class InsDatos():
    def __init__(self, claves, registros):
        self.claves = claves
        self.registros = registros
        self.cadena = ""
        self.retornar()
    def  retornar(self):
        for clave in self.claves:
            self.cadena += clave+"  "
        for registros in self.registros:
            self.cadena+="\n"
            for registro in registros:
                self.cadena+=registro+"  "
        self.cadena+="\n"
        return self.cadena


class InsSuma():
    def __init__(self, campo, claves, registros):
        self.campo = campo
        self.claves = claves
        self.registros = registros
        self.suma = 0
        self.cadena = ""

        for i in range(len(claves)):
            if  self.campo == self.claves[i]:
                for j in range(len(self.registros)):
                    self.suma+= int(registros[j][i])
        self.retornar()
    def retornar(self):
        self.cadena+="La suma es: "+ str(self.suma)+"\n"
        return self.cadena


class InsMax():
    def __init__(self, campo, claves, registros):
        self.campo = campo
        self.claves = claves
        self.registros = registros
        self.listanums = []
        self.cadena=""

        for i in range(len(claves)):
            if  self.campo == self.claves[i]:
                for j in range(len(self.registros)):
                    self.listanums.append(registros[j][i])
        self.retorno()

    def retorno(self):
        self.cadena+= "El número máximo es: "+ str(max(self.listanums))+"\n"
        return self.cadena

class InsMin():
    def __init__(self, campo, claves, registros):
        self.campo = campo
        self.claves = claves
        self.registros = registros
        self.listanums = []
        self.cadena = ""

        for i in range(len(claves)):
            if  self.campo == self.claves[i]:
                for j in range(len(self.registros)):
                    self.listanums.append(registros[j][i])
        self.retorno()
    def retorno(self):
        self.cadena+="El número mínimo es: "+ str(min(self.listanums))+"\n"
        return self.cadena

class InsReporte():
    def __init__(self, nombre, claves, registros):
        self.nombre = nombre.replace('"',"")
        self.cadena = " Se generó el archivo html con el nombre"+self.nombre+"\n"
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
        self.retorno()
    def retorno(self):
        return self.cadena

