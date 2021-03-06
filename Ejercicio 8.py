# Porcentajes, IVA e inversiones

# 1. Escribe un algoritmo que calcula el precio con todos los impuestos incluidos (TII) para un precio sin impuestos y
#    un porcentaje de IVA dado. 

Algoritmo cálculo de impuestos

Entrada 
    v1 : REAL # Precio sin impuestos
    iva : REAL # Porcentaje de IVA

Resultado : REAL 

Precondicion 
    # Todos los datos de entrada deben ser positivos
    v1 > 0
    iva > 0

Variables
    v_iva : REAL # Valor del porcentaje de IVA sobre el precio sin impuestos

Realizacion
    # Cálculo del valor del IVA dependiendo del precio sin impuestos
    v_iva <- v1 * (iva / 100)

    # Cálculo del precio con impuestos incluidos
    Resultado <- v1 + v_iva

Poscondicion 
    # El resultado tiene que ser mayor que el precio inicial
    Resultado > v1

fin cálculo de impuestos 




# 2. Escribe un algoritmo que calcula el importe de los intereses generados por un capital invertido a un interés dado durante
#    un tiempo dado, expresado en meses.

Algoritmo importe 

Entrada
    ci : REAL # Capital inicial
    interes : REAL # El interés (en porcentaje)
    meses : REAL # El tiempo en meses durante el cual se estará invirtiendo 

Precondicion 
    ci > 0
    interes > 0
    meses > 0

Variables
    valor_actual : REAL # El valor sobre el cual voy a estar añadiendo en dinero obtenido tras invertir

Realizacion
    valor_actual = ci
    desde i = 1 hasta i <= meses 
        valor_actual = valor_actual + valor_actual * (interes / 100)
    fin desde 

    Resultado <- valor_actual
    
Poscondicion
    ci < Resultado 

fin importe 