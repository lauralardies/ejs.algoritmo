# Cuenta de depósito

# Se considera las cuentas de depósitos alojadas en un banco por los clientes. Solo se permite hacer una retirada si 
# el saldo que queda en la cuenta no es negativo.

# 1. Definir el tipo de datos CUENTA..

tipo CUENTA

saldo : REAL

invariante 
    # El descubierto no está autorizado
    descubierto = 0

    saldo >= descubierto 

fin cuenta




# 2. Definir las operaciones aplicables.

# Abrir una cuenta
# Abonar
# Cargar
# Consultar:
#   - Saldo positivo
#   - Saldo negativo

# En determinadas circunstancias y para determinados clientes, la banca autoriza un descubierto limitado y temporal.

# 3. Volver a hacer las definiciones previas para permitir estos descubiertos.
