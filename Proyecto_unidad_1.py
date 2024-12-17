print("Bienvenido a tu app de operacion entre conjuntos")
print("Para usarlo, deberas ingresar los elementos del conjunto A y conjunto B")
print("La aplicacion calculara por ti las operaciones de Union, Interseccion, Diferencia, Diferencia simetrica y si son o no subcojuntos")

def elementos_conjunto(nombre_conjunto): 
    elementos = input(f"Ingresa los elementos del conjunto {nombre_conjunto}, separados por comas: ") 
    conjunto = set() 
    for elemento in elementos.split(','): 
        elemento = elemento.strip()  
        try: 
            if '.' in elemento: 
                conjunto.add(float(elemento))  
            else: 
                conjunto.add(int(elemento)) 
        except ValueError: 
            if len(elemento) == 1: 
                conjunto.add(elemento)  
            else: 
                conjunto.add(elemento) 
    return conjunto

A = elementos_conjunto("A")
B = elementos_conjunto("B")

union = A | B
print("Unión de A y B:", union)

interseccion = A & B
print("Intersección de A y B:", interseccion)

diferencia = A - B
print("Diferende A m B:", diferencia)

diferencia_simetrica = A ^ B
print("Diferencia simétrica de A y B:", diferencia_simetrica)

es_subconjunto_A_B = A <= B
print("A es subconjunto de B:", es_subconjunto_A_B)

es_subconjunto_B_A = B <= A
print("B es subconjunto de A:", es_subconjunto_B_A)
