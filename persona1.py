class Persona:
    def __init__(self,nombre,apellido):
        self.__nombre=nombre
        self.__apellido=apellido
    
    @property
    def nombre(self):
      return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo):
       self.__nombre=nuevo
       
    

        