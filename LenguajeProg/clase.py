class Persona:
    def __init__(self,nombre,edad):
        self.nombre= nombre
        self.edad=edad
        
    def saludar(self):
        print (f"Hola, soy {self.nombre} y tengo {self.edad}años.")
        
    #Crear objeto persona
personal= Persona ("bonilla",19)
personal.saludar ()
    
class Estudiante (Persona):
    def __init__(self,nombre, edad, grado):
        super().__init__(nombre,edad)
        self.grado=grado
        
    def estudiar (self):
        print (f"{self.nombre} esta estudiando el grado {self.grado}.")
                
estudiante1= Estudiante ("nAHOMY", 19, "mAESTRIA")
estudiante1.saludar()
estudiante1.estudiar()
    
    