from importaciones.pantallainicio import pantallaInicio
from importaciones.muestramenu import muestraMenu
from importaciones.atrapaopcion import atrapaOpcion
'''
Programa de gestión
v0.1 Jose Vicente Carratalá
'''

# Declaraciones
NOMBRE_PROGRAMA = "Programa de gestión"
VERSION_Y_AUTOR = "v0.1 Jose Vicente Carratalá"
BORRAR = "\033c"

print(BORRAR)
pantallaInicio(NOMBRE_PROGRAMA,VERSION_Y_AUTOR)
while True:
    print(BORRAR)
    muestraMenu()
    atrapaOpcion()


