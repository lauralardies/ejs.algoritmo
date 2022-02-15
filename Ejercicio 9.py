# Media aritmética ponderada

# 1. Escribe un algoritmo que calcula la media aritmética de tres números dados.

Algoritmo media aritmetica

Entrada 
    v1, v2, v3 : REAL # Los valores con los que vamos a calcular la media

Resultado : REAL

Precondicion 

Variables
    s : REAL # Suma de los tres valores dados

Realizacion
    # Sumamos los tres valores aportados
    s <- v1 + v2 + v3 

    # Calculamos la media aritmetica
    Resultado <- s / REAL(3)

Poscondicion 
    min(v1, v2, v3) <= Resultado <= max(v1, v2, v3)

fin media aritmetica




# 2. La misma pregunta para una media ponderada cuando se dan los números y los coeficientes de ponderación.

Algoritmo media aritmetica ponderada 

Entrada 
    v1, v2, v3 : REAL # Los valores con los que vamos a calcular la media
    p1, p2, p3 : REAL # Los coeficientes de ponderación que corresponden a cada valor para la media

Resultado : REAL

Precondicion 

Variables
    m1, m2, m3 : REAL # Cada valor multiplicado por su coeficiente de ponderación correspondiente
    s : REAL # Suma de los tres valores dados con sus ponderaciones
    sp : REAL # Suma de los coeficientes de ponderación

Realizacion
    # Calculamos cada valor aplicando su ponderación correspondiente
    m1 <- v1 * p1 
    m2 <- v2 * p2
    m3 <- v3 * p3 

    # Sumamos los nuevos valores con la ponderación aplicada
    s <- m1 + m2 + m3

    # Sumamos los coeficientes de ponderación
    sp <- p1 + p2 + p3 

    # Calculamos la media aritmetica ponderada
    Resultado <- s / sp 

Poscondicion 
    min(m1, m2, m3) <= Resultado

fin media aritmetica ponderada