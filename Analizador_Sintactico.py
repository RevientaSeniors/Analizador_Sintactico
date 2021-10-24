from tkinter.constants import E, S
from Token import Token
from Error import Error

class Analizador_Sintactico():
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.i = 0

    def analizarOrden(self, listaTokens):
        self.listaTokens = listaTokens
        self.inicio()
        
    def inicio(self):
        self.listaInstrucciones()

    def listaInstrucciones(self):
        if self.listaTokens[self.i].get_tipo() == 'claves' or self.listaTokens[self.i].get_tipo() == 'registros' or self.listaTokens[self.i].get_tipo() == 'imprimir' or self.listaTokens[self.i].get_tipo() == 'imprimirln' or self.listaTokens[self.i].get_tipo() == 'conteo' or self.listaTokens[self.i].get_tipo() == 'promedio' or self.listaTokens[self.i].get_tipo() == 'contarsi' or self.listaTokens[self.i].get_tipo() == 'datos' or self.listaTokens[self.i].get_tipo() == 'sumar' or self.listaTokens[self.i].get_tipo() == 'maximo' or self.listaTokens[self.i].get_tipo() == 'minimo' or self.listaTokens[self.i].get_tipo() == 'reporte' or self.listaTokens[self.i].get_tipo() == 'comentarioComillas' or self.listaTokens[self.i].get_tipo() == 'comentarioSharp':
            self.instruccion()
            self.listaInstrucciones2()
        else:
            self.listaErrores.append(Error("ERROR SINTÁCTICO: "+ self.listaTokens[self.i].get_lexema(), self.listaTokens[self.i].get_fila(), self.listaTokens[self.i].get_columna()))
    
    def instruccion(self):
        if self.listaTokens[self.i].get_tipo()=='claves':
            self.insClaves()
        elif self.listaTokens[self.i].get_tipo()=='registros':
            self.insRegistros()
        elif self.listaTokens[self.i].get_tipo()=='imprimir':
            self.insImprimir()
        elif self.listaTokens[self.i].get_tipo()=='imprimirln':
            self.insImprimirLn()
        elif self.listaTokens[self.i].get_tipo()=='conteo':
            self.insConteo()
        elif self.listaTokens[self.i].get_tipo()=='promedio':
            self.insPromedio()
        elif self.listaTokens[self.i].get_tipo()=='contarsi':
            self.insContarSi()
        elif self.listaTokens[self.i].get_tipo()=='datos':
            self.insDatos()
        elif self.listaTokens[self.i].get_tipo()=='sumar':
            self.insSumar()
        elif self.listaTokens[self.i].get_tipo()=='maximo':
            self.insMaxima()
        elif self.listaTokens[self.i].get_tipo()=='minimo':
            self.insMinima()
        elif self.listaTokens[self.i].get_tipo()=='reporte':
            self.insReporte()
        elif self.listaTokens[self.i].get_tipo()=='comentarioComillas':
            self.comentarioComillas()
        elif self.listaTokens[self.i].get_tipo()=='comentarioSharp':
            self.comentarioSharp()
            

    def listaInstrucciones2(self):
        if self.listaTokens[self.i].get_tipo() == 'claves' or self.listaTokens[self.i].get_tipo() == 'registros' or self.listaTokens[self.i].get_tipo() == 'imprimir' or self.listaTokens[self.i].get_tipo() == 'imprimirln' or self.listaTokens[self.i].get_tipo() == 'conteo' or self.listaTokens[self.i].get_tipo() == 'promedio' or self.listaTokens[self.i].get_tipo() == 'contarsi' or self.listaTokens[self.i].get_tipo() == 'datos' or self.listaTokens[self.i].get_tipo() == 'sumar' or self.listaTokens[self.i].get_tipo() == 'maximo' or self.listaTokens[self.i].get_tipo() == 'minimo' or self.listaTokens[self.i].get_tipo() == 'reporte' or self.listaTokens[self.i].get_tipo() == 'comentarioComillas' or self.listaTokens[self.i].get_tipo() == 'comentarioSharp':
            self.instruccion()
            self.listaInstrucciones2()
        elif self.listaTokens[self.i].get_tipo() == 'dolar':
            print("CADENA PERMITIDA SINTÁCTICAMENTE")
        else:
            self.listaErrores.append(Error("ERROR SINTÁCTICO: "+ self.listaTokens[self.i].get_lexema(), self.listaTokens[self.i].get_fila(), self.listaTokens[self.i].get_columna()))
            print("ERROR:  ", self.listaErrores[0].get_descripcion())
   
    def insClaves(self):
        if self.listaTokens[self.i].get_tipo()=='claves':
            self.i+=1
            if self.listaTokens[self.i].get_tipo()=='igual':
                self.i+=1
                if self.listaTokens[self.i].get_tipo()=='corcheteAbierto':
                    self.i+=1
                    self.listaValorClaves()
                    if self.listaTokens[self.i].get_tipo()=='corcheteCerrado':
                        self.i+=1

    def insImprimir(self):
        if self.listaTokens[self.i].get_tipo()=='imprimir':
            self.i+=1
            if self.listaTokens[self.i].get_tipo()=='parentesisAbierto':
                self.i+=1
                if self.listaTokens[self.i].get_tipo()=='cadena':
                    self.i+=1
                    if self.listaTokens[self.i].get_tipo()=='parentesisCerrado':
                        self.i+=1
                        if self.listaTokens[self.i].get_tipo()=='puntocoma':
                            self.i+=1
                            pass
                        
    def insImprimirLn(self):
        if self.listaTokens[self.i].get_tipo()=='imprimirln':
            self.i+=1
            if self.listaTokens[self.i].get_tipo()=='parentesisAbierto':
                self.i+=1
                if self.listaTokens[self.i].get_tipo()=='cadena':
                    self.i+=1
                    if self.listaTokens[self.i].get_tipo()=='parentesisCerrado':
                        self.i+=1
                        if self.listaTokens[self.i].get_tipo()=='puntocoma':
                            self.i+=1
                            pass           
    
    def insConteo(self):
        if self.listaTokens[self.i].get_tipo()=='conteo':
            self.i+=1
            if self.listaTokens[self.i].get_tipo()=='parentesisAbierto':
                self.i+=1
                if self.listaTokens[self.i].get_tipo()=='parentesisCerrado':
                    self.i+=1
                    if self.listaTokens[self.i].get_tipo()=='puntocoma':
                        self.i+=1
                        pass  

    def insPromedio(self):
        if self.listaTokens[self.i].get_tipo()=='promedio':
            self.i+=1
            if self.listaTokens[self.i].get_tipo()=='parentesisAbierto':
                self.i+=1
                if self.listaTokens[self.i].get_tipo()=='cadena':
                    self.i+=1
                    if self.listaTokens[self.i].get_tipo()=='parentesisCerrado':
                        self.i+=1
                        if self.listaTokens[self.i].get_tipo()=='puntocoma':
                            self.i+=1
                            pass
    def insContarSi(self):
        if self.listaTokens[self.i].get_tipo()=='contarsi':
            self.i+=1
            if self.listaTokens[self.i].get_tipo()=='parentesisAbierto':
                self.i+=1
                if self.listaTokens[self.i].get_tipo()=='cadena':
                    self.i+=1
                    if self.listaTokens[self.i].get_tipo()=='coma':
                        self.i+=1
                        if self.listaTokens[self.i].get_tipo()=='entero':
                            self.i+=1
                            if self.listaTokens[self.i].get_tipo()=='parentesisCerrado':
                                self.i+=1
                                if self.listaTokens[self.i].get_tipo()=='puntocoma':
                                    self.i+=1
                                    pass

    def insDatos(self):
        if self.listaTokens[self.i].get_tipo()=='datos':
            self.i+=1
            if self.listaTokens[self.i].get_tipo()=='parentesisAbierto':
                self.i+=1
                if self.listaTokens[self.i].get_tipo()=='parentesisCerrado':
                    self.i+=1
                    if self.listaTokens[self.i].get_tipo()=='puntocoma':
                        self.i+=1
                        pass
    
    def insSumar(self):
        if self.listaTokens[self.i].get_tipo()=='sumar':
            self.i+=1
            if self.listaTokens[self.i].get_tipo()=='parentesisAbierto':
                self.i+=1
                if self.listaTokens[self.i].get_tipo()=='cadena':
                    self.i+=1
                    if self.listaTokens[self.i].get_tipo()=='parentesisCerrado':
                        self.i+=1
                        if self.listaTokens[self.i].get_tipo()=='puntocoma':
                            self.i+=1
                            pass

    def insMaxima(self):
        if self.listaTokens[self.i].get_tipo()=='maximo':
            self.i+=1
            if self.listaTokens[self.i].get_tipo()=='parentesisAbierto':
                self.i+=1
                if self.listaTokens[self.i].get_tipo()=='cadena':
                    self.i+=1
                    if self.listaTokens[self.i].get_tipo()=='parentesisCerrado':
                        self.i+=1
                        if self.listaTokens[self.i].get_tipo()=='puntocoma':
                            self.i+=1
                            pass
                            
    def insMinima(self):
        if self.listaTokens[self.i].get_tipo()=='minimo':
            self.i+=1
            if self.listaTokens[self.i].get_tipo()=='parentesisAbierto':
                self.i+=1
                if self.listaTokens[self.i].get_tipo()=='cadena':
                    self.i+=1
                    if self.listaTokens[self.i].get_tipo()=='parentesisCerrado':
                        self.i+=1
                        if self.listaTokens[self.i].get_tipo()=='puntocoma':
                            self.i+=1
                            pass

    def insReporte(self):
        if self.listaTokens[self.i].get_tipo()=='reporte':
            self.i+=1
            if self.listaTokens[self.i].get_tipo()=='parentesisAbierto':
                self.i+=1
                if self.listaTokens[self.i].get_tipo()=='cadena':
                    self.i+=1
                    if self.listaTokens[self.i].get_tipo()=='parentesisCerrado':
                        self.i+=1
                        if self.listaTokens[self.i].get_tipo()=='puntocoma':
                            self.i+=1
                            pass
    
    def comentarioComillas(self):
        if self.listaTokens[self.i].get_tipo()=='comentarioComillas':
            self.i+=1
            pass
    
    def comentarioSharp(self):
        if self.listaTokens[self.i].get_tipo()=='comentarioSharp':
            self.i+=1
            pass


    def listaValorClaves(self):
        if self.listaTokens[self.i].get_tipo()=='cadena':
            self.i+=1
            self.listaValorClaves2()
        
    def listaValorClaves2(self):
        if self.listaTokens[self.i].get_tipo()=='coma':
            self.i+=1
            if self.listaTokens[self.i].get_tipo()=='cadena':
                self.i+=1
                self.listaValorClaves2()
        elif self.listaTokens[self.i].get_tipo()=='corcheteCerrado':
          pass



    def insRegistros(self):
        if self.listaTokens[self.i].get_tipo()=='registros':
            self.i+=1
            if self.listaTokens[self.i].get_tipo()=='igual':
                self.i+=1
                if self.listaTokens[self.i].get_tipo()=='corcheteAbierto':
                    self.i+=1
                    self.listaRegistros()
                    if self.listaTokens[self.i].get_tipo()=='corcheteCerrado':
                        self.i+=1

    def listaRegistros(self):
        self.registro()
        self.listaRegistros2()
    
    def listaRegistros2(self):
        if self.listaTokens[self.i].get_tipo()=='corcheteCerrado':
            pass
        else:
            self.registro()
            self.listaRegistros2()
    
    def registro(self):
        if self.listaTokens[self.i].get_tipo()=='llaveAbierta':
            self.i+=1
            self.listaValoresRegistros()
            if self.listaTokens[self.i].get_tipo()=='llaveCerrada':
                self.i+=1

    def listaValoresRegistros(self):
        self.valorRegistro()
        self.listaValoresRegistros2()

    def listaValoresRegistros2(self):
        if self.listaTokens[self.i].get_tipo()=='coma':
            self.i+=1
            self.valorRegistro()
            self.listaValoresRegistros2()
        elif self.listaTokens[self.i].get_tipo()=='llaveCerrada':
          pass

    def valorRegistro(self):
        if self.listaTokens[self.i].get_tipo()=='cadena':
            self.i+=1
        elif self.listaTokens[self.i].get_tipo()=='entero':
            self.i+=1
        elif self.listaTokens[self.i].get_tipo()=='decimal':
            self.i+=1
        