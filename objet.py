import json
class Receta:

    def __init__(self,nombre,ingredientes=None,preparacion=None):
        self.nombre = nombre
        self.ingredientes = ["ingredientes"]
        self.preparacion = ["preparacion"]
      
    def mostrar(self):
       print(self.nombre,self.ingredientes)   

    def agregar_ingredientes(self,ingre,gr,cant):
     ingredientes={"nombre":ingre,"unidad medida":gr,"cantidad":cant}  
     self.ingredientes.append(ingredientes)
     return(self.ingredientes)

    def crear_preparacion(self,text):
       self.preparacion.append(text)
       print(self.preparacion)

    def crear_json(self):
       receta=[self.nombre,self.ingredientes,self.preparacion]
       with open("receta.json",'a+')as archivo:
          print(len(archivo.read()))
        #   json.dump(receta,archivo,indent=4)  

    def mostrar_info(self):
       print(self.nombre,self.ingredientes,self.preparacion)      

    def modificar_receta(self):
       with open("recetaFideos caseros.json")as archivo:
          receta = json.load(archivo)
          print(receta)
receta3 = Receta("Salteado de verduras, pollo y arroz") 
receta3.agregar_ingredientes("pechuga de pollo","800gr","1")
receta3.agregar_ingredientes("zanahoria","60gr","1")
receta3.agregar_ingredientes("cebolla","50gr","1")
receta3.agregar_ingredientes("pimiento rojo","40gr","1")
receta3.agregar_ingredientes("pimiento verde","30gr","1")
receta3.agregar_ingredientes("ajo","8gr","1")
receta3.agregar_ingredientes("sal","40gr","1")
receta3.agregar_ingredientes("pimienta","20gr","1")
receta3.agregar_ingredientes("salsa de soja","22gr","1")
receta3.agregar_ingredientes("semillas de sésamo","10gr","1")
receta3.agregar_ingredientes("vino blanco","20gr","1")
receta3.agregar_ingredientes("arroz basmati","250gr","1")
receta3.crear_preparacion("En una olla hervir el arroz basmati hasta el punto al dente y reservar")
receta3.crear_preparacion("Maceramos la pechuga cortada en tiras con la salsa de soja, el vino y el diente de ajo prensado al menos por media hora.")
receta3.crear_preparacion("Mientras vamos picando en juliana las verduras.")
receta3.crear_preparacion("Escurrimos el pollo del líquido de la maceración y lo ponemos en el wok con un poquito de aceite. Cuando estén dorados los retiramos y ponemos las verduras (todas a la vez) y en cuando empiezan a ablandarse y coger color añadimos el líquido de la maceración y salteamos sin parar pero con cuidado.")
receta3.crear_preparacion("En cuanto el alcohol del vino haya evaporado y el líquido se reduzca ponemos el pollo y el arroz cocido y muy bien escurrido, damos unas vueltas con cuidado para que el arroz no se deshaga ni apelmace y servimos caliente con el sésamo por encima.")

receta3.crear_json()
# Receta.modificar_receta("salteado")