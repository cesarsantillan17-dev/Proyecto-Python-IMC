
# Calculadora de Indice de Masa Corporal (IMC)

print("===== CALCULADORA DE IMC =====")

# Solicitar datos al usuario
nombre = input("Ingresa tu nombre: ").title()
apellido = input("Ingresa tu apellido: ").title()
edad = int(input("Ingresa tu edad: "))
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))

# Calcular IMC
imc = peso / (estatura ** 2)

# Mostrar resultados
print("\n" + "=" * 40)
print("         RESULTADOS DEL IMC")
print("=" * 40)

print(f"Nombre:       {nombre} {apellido}")
print(f"Edad:         {edad} años")
print(f"Peso:         {peso:.2f} kg")
print(f"Estatura:     {estatura:.2f} m")
print("-" * 40)
print(f"Tu IMC es:    {imc:.2f}")
print("=" * 40)
