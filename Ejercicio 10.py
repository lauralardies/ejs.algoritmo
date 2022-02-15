# Área del triángulo

# 1. Escribir un algoritmo que calcula el área de un triángulo del que se da la medida de un lado y la de la 
#    altura relativa a ese lado.

Algoritmo área

Entrada
    l : REAL # Valor del lado 
    h : REAL # Valor de la altura a la que corresponde el lado (l)

Resultado : REAL

Precondicion 
    # Los datos que nos aporta el enunciado tienen que ser mayores que 0
    l > 0
    h > 0

Variables 
    lh : REAL # Producto del lado y la altura

Realizacion 
    # Calulamos el producto entre el lado y la altura 
    lh <- l * h

    # Calculamos el área del triángulo
    Resultado <- lh / REAL(2)

Poscondicion 

fin área

# 2. ¿Se puede utilizar este algoritmo para un triángulo rectángulo si se dan las medidas de sus dos lados perpendiculares?

# Sí que se podría emplear el algoritmo anterior ya que la altura se mide de manera perpendicular al lado. Por lo tanto, 
# al ser perpendiculares los lados que te dan, uno de estos se puede considerar la altura. De esta manera tenemos un lado
# con su altura correspondiente y así podemos seguir el código que hemos creado. 