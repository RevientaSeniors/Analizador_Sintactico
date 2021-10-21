from sre_constants import FAILURE
from Token import Token
from Error import Error
import re
class Analizador_Lexico():

    def __init__(self):
        self.listaTokens=[]
        self.listaErrores=[]

    def analizarTexto(self,contenido):
        fila = 1
        columna = 1
        buffer ='' #almacenar el lexema
        centinela2 = False
        centinela ='$'
        contenido+=centinela
        estado = 0
        #Automata

        i = 0
        while i < len(contenido):
            caracterLeido = contenido[i]
            if estado == 0:
                if re.search('[a-zA-Z]',caracterLeido):
                    buffer +=caracterLeido
                    columna+=1
                    estado = 1
                elif caracterLeido == '=':
                    self.listaTokens.append(Token("igual", caracterLeido, fila, columna))
                    columna+=1
                elif caracterLeido == '[':
                    self.listaTokens.append(Token("corcheteAbierto", caracterLeido, fila, columna))
                    columna+=1
                elif caracterLeido == ']':
                    self.listaTokens.append(Token("corcheteCerrado", caracterLeido, fila, columna))
                    columna+=1
                elif caracterLeido == '"':
                    buffer +=caracterLeido
                    columna +=1
                    estado = 2
                elif caracterLeido == ",":
                    self.listaTokens.append(Token("coma",caracterLeido, fila, columna))
                    columna+=1
                elif caracterLeido == "{":
                    self.listaTokens.append(Token("llaveAbierta",caracterLeido, fila, columna))
                    columna+=1
                elif caracterLeido == "}":
                    self.listaTokens.append(Token("llaveCerrada",caracterLeido, fila, columna))
                    columna+=1
                elif re.search("\d",caracterLeido):
                    buffer += caracterLeido
                    columna +=1
                    estado = 3
                elif caracterLeido == "(":
                    self.listaTokens.append(Token("parentesisAbierto", caracterLeido, fila, columna))
                    columna+=1
                elif caracterLeido == ")":
                    self.listaTokens.append(Token("parentesisCerrado", caracterLeido, fila, columna))
                    columna+=1
                elif caracterLeido == ";":
                    self.listaTokens.append(Token("puntocoma", caracterLeido, fila, columna))
                    columna+=1
                elif caracterLeido == "#":
                    buffer +=caracterLeido
                    columna +=1
                    estado = 5
                elif caracterLeido == "'":
                    columna +=1
                    if contenido[i+1]=="'" and contenido[i+2]== "'":
                        centinela2 = True
                    elif centinela2 == True:
                        estado = 6 
                        columna+=1
                elif re.search("\n",caracterLeido):
                    columna=1
                    fila +=1
                elif re.search("\t",caracterLeido):
                    fila +=1
                elif caracterLeido == "$":
                    self.listaTokens.append(Token("dolar", caracterLeido, fila, columna))
                    columna+=1
                    break
            elif estado == 1:
                if re.search('[a-zA-Z]',caracterLeido):
                    buffer+=caracterLeido
                    columna+=1
                else:
                    if buffer == 'Claves':
                        self.listaTokens.append(Token("claves", buffer, fila, columna))
                    elif buffer == 'Registros':
                        self.listaTokens.append(Token('registros',buffer, fila, columna))
                    elif buffer == 'imprimir':
                        self.listaTokens.append(Token('imprimir', buffer, fila, columna))
                    elif buffer == 'imprimirln':
                        self.listaTokens.append(Token('imprimirln',buffer, fila, columna))
                    elif buffer == 'conteo':
                        self.listaTokens.append(Token('conteo', buffer, fila, columna))
                    elif buffer == 'promedio':
                        self.listaTokens.append(Token('promedio', buffer, fila, columna))
                    elif buffer == 'contarsi':
                        self.listaTokens.append(Token('contarsi', buffer, fila, columna))
                    elif buffer == 'datos':
                        self.listaTokens.append(Token('datos', buffer, fila, columna))
                    elif buffer == 'sumar':
                        self.listaTokens.append(Token('sumar', buffer, fila, columna))
                    elif buffer == 'max':
                        self.listaTokens.append(Token('maximo', buffer, fila, columna))
                    elif buffer == 'min':
                        self.listaTokens.append(Token('minimo', buffer, fila, columna))
                    elif buffer == 'exportarReporte':
                        self.listaTokens.append(Token('reporte', buffer, fila, columna))
                    buffer = ''
                    i -= 1
                    estado = 0
            elif estado == 2:
                if caracterLeido == '\n':
                    columna = 1
                    fila +=1
                elif caracterLeido=='"':
                    buffer+=caracterLeido
                    self.listaTokens.append(Token("cadena", buffer, fila, columna))
                    buffer = ''
                    columna +=1
                    estado = 0
                else:
                    buffer +=caracterLeido
            elif estado == 3:
                if re.search("\d",caracterLeido):
                    buffer +=caracterLeido
                    columna +=1
                elif caracterLeido == ".":
                    buffer+=caracterLeido
                    columna+=1
                    estado = 4
                else:
                    self.listaTokens.append(Token("entero", buffer, fila, columna))
                    buffer = ''
                    estado = 0
                    i-=1
            elif estado == 4:
                if re.search("\d",caracterLeido):
                    buffer +=caracterLeido
                    columna +=1
                else:
                    self.listaTokens.append(Token("decimal", buffer, fila, columna))
                    buffer = ''
                    estado = 0
                    i-=1
            elif estado == 5:
                if caracterLeido == "\n":
                    self.listaTokens.append(Token("comentarioSharp", buffer, fila, columna))
                    columna = 1
                    fila +=1
                    buffer =''
                    estado = 0
                else:
                    buffer +=caracterLeido 
            elif estado == 6:
                if caracterLeido == "'":
                    columna +=1
                    if contenido[i+1]=="'" and contenido[i+2]== "'":
                        centinela2 = False
                        columna+=1
                    elif centinela2 == False:
                        self.listaTokens.append(Token("comentarioComillas", buffer,fila,columna))
                        buffer =''
                        estado = 0
                else:
                    buffer += caracterLeido
                    columna +=1

            i+=1    
        for token in self.listaTokens:
            print(token.get_tipo(),"   ", token.get_lexema())
        
        
