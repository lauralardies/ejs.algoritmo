# Salario y horas extra

# El cálculo de una nómina tiene en cuenta el salario bruto asociado a las horas «normales» que debe hacer el empleado y 
# las horas «extra» trabajadas en el mes. Las horas extra se remuneran según las siguientes normas administrativas:
# - Tarifa por hora aumentada en un 125 % para las horas entre la 36.ª y la 43.ª.
# - Tarifa por hora aumentada en un 150 % para las horas a partir de la 44.ª.

# El aumento se realiza sobre la tarifa por hora normal, calculado a partir del salario mensual bruto para un año de 52 
# semanas repartidas en 12 meses, sobre la base de 35 horas trabajadas por semana.

# Escribir el algoritmo que calcula el importe de las horas extra que hay que pagar, a partir del salario mensual bruto y 
# de la cantidad de horas extra. Se podrá suponer que el cálculo siempre se usa para una cantidad de horas superior a 8.

Algoritmo pago

Entrada 
    sal_mensual : REAL # Valor del salario mensual bruto
    horas_extra : REAL # El número de horas extra que ha realizado el trabajador en total

Resultado : REAL # El resultado es lo que cuestan las horas extra

Precondicion
    horas_extra > 8

Variables
    horas_125 : ENTERO # El número de horas extra que aumenta la tarifa un 125%
    horas_150 : REAL # El número de horas extra que aumenta la tarifa un 150%
    sal_hora : ENTER # Valor del salario por hora. 

Realizacion
    # Primero dividimos las horas extra entre las de 125% y las de 150%
    # Siempre las primeras 8 horas aumentan un 125% el sueldo.
    horas_125 <- 8
    horas_150 <- horas_extra - 8

    # Seguidamente, pasamos de salario mensual a salario por hora. Sabemos que trabaja 52 semanas repartidas en 12 meses, trabajando
    # 35 horas por semana.
    sal_hora <- sal_mensual / REAL(35 * 52 / 12)

    Resultado <- sal_hora * (horas_125 * 1.25 + horas_150 * 1.50)

fin pago