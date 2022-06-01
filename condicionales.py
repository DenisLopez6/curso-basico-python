# Declaramos una variable 
calificacion = input("introduce tu calificación de la AZ-900: ")

calificacion = int(calificacion)

# Preguntamos si la calificación es menor a 700
if calificacion < 700 :
    print("Veees, por no estudiar") # Si es menor a 700, pasa esto 
elif calificacion > 1000 :
    print("MENTIRA!!! No puedes sacar más de mil") 
else : # Si no se cumple el if anterior, pasa a esto
    print("Felicidades, pasa por tu certificado") # Se ejecuta si ninguno de los if se cumple

# Verificador de mayoria de edad
edad = input("introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Bienvenido al mamitas")
elif edad > 100 :
    print("Si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fuera viajero de tiempo")
else :
    print("No puedes llevarte esos cigarros")