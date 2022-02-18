# Cuenta de depósito

# Se considera las cuentas de depósitos alojadas en un banco por los clientes. Solo se permite hacer una retirada si 
# el saldo que queda en la cuenta no es negativo.

# 1. Definir el tipo de datos CUENTA..

tipo CUENTA

saldo : REAL
descubierto : REAL

invariante 
    # El descubierto no está autorizado
    descubierto = 0

    saldo >= descubierto 

fin cuenta




# 2. Definir las operaciones aplicables.

# Abrir una cuenta

Algoritmo abrir (c : CUENTA)

    Entrada
        saldo_inicial : REAL # Tenemos una cantidad de dinero que queremos meter en la cuenta que hemos abierto 

    Precondicion 
        saldo_inicial > 0 

    Realizacion 
        c.saldo <- saldo_inicial
        c.descubierto <- 0 

fin abrir

# Abonar

Algoritmo abonar (c : CUENTA)

    Entrada 
        credito : REAL # Cantidad que quieres abonar

    Precondicion 
        c.saldo =! 0
        credito =! 0

    Realizacion 
        # Añadimos el crédito que queremos añadir al saldo que ya está en la cuenta
        c.saldo <- c.saldo + credito

fin abonar

# Cargar

Algoritmo cargar (c : CUENTA)

    Entrada 
        debito : REAL 
    
    Precondicion 
        c.saldo =! 0 
        debito =! 0
        c.saldo + c.descubierto >= debito > 0 

    Realizacion 
        c.saldo <- c.saldo - debito 

fin cargar

# Consultar

Algoritmo consultar (c : CUENTA)

    Resultado : REAL 

    Precondicion 
        c.saldo =! 0

    Realizacion 
        Resultado <- c.saldo 

fin consultar 

#   - Podemos consultar si el saldo es positivo

Algoritmo positivo (c : CUENTA)

    Resultado : BOOLEANO 

    Precondicion 
        c.saldo =! 0

    Realizacion 
        Resultado <- (c.saldo > 0)

fin positivo  

#   - Podemos consultar si el saldo es negativo

Algoritmo negativo (c : CUENTA)

    Resultado : BOOLEANO  

    Precondicion 
        c.saldo =! 0

    Realizacion 
        Resultado <- (c.saldo > 0)

fin negativo 

# En determinadas circunstancias y para determinados clientes, la banca autoriza un descubierto limitado y temporal.

# 3. Volver a hacer las definiciones previas para permitir estos descubiertos.
