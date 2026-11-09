# Calculadora de Índice de Masa Corporal (IMC)

print("===== CALCULADORA DE IMC =====")

# Solicitar datos al usuario
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))

# Calcular IMC
imc = peso / (estatura ** 2)

# Mostrar resultados
print("\n===== RESULTADOS =====")
print("Nombre:", nombre)
print("Edad:", edad, "años")
print("Peso:", peso, "kg")
print("Estatura:", estatura, "m")
print("Tu IMC es:", round(imc, 2))