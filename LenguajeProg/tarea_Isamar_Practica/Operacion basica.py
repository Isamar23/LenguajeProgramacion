
def Suma (A,B):
    return A+B
def Resta (A,B):
    return A-B
def Multiplicacion (A,B):
    return A*B
def Divicion (A,B):
    return A/B
#Operaciones arismeticas
while True:
    print ("***Operaciones arismeticas***")
    print ("1. Sumando")
    print ("2. Restando")
    print ("3. Multiplicando")
    print ("3. Dividiendo ")
    opcion= input("ingresa una opcion:") 
    numero1=int (input("ingrese el primer numero="))
    numero2=int (input("ingrese el segundo numero="))

if opcion=="1":
    print("la suma es:", Suma(numero1,numero2))
elif opcion== "2":
 print ("la resta es:", Resta(numero1,numero2))
elif opcion== "3":
 print("la multiplicacion es:", Multiplicacion(numero1,numero2))
elif opcion== "4":
 print("la Division es:", Division(numero1,numero2))
else:
 print("opcion invalida")


