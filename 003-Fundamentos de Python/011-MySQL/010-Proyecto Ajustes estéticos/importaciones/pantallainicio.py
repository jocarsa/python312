import shutil

def pantallaInicio(NOMBRE_PROGRAMA,VERSION_Y_AUTOR):
    AZUL = '\033[94m'
    RESET = '\033[0m'
    AMARILLO = '\033[93m'
    columnas, filas = shutil.get_terminal_size()
    print(AZUL)
    mediapantallax = columnas/2
    mediapantallay = filas/2
    
    iniciox = str(round(mediapantallax-len(NOMBRE_PROGRAMA)/2))
    inicioy = str(round(mediapantallay)) 
    print(f"\033[{inicioy};{iniciox}H",NOMBRE_PROGRAMA)
    iniciox = str(round(mediapantallax-len(VERSION_Y_AUTOR)/2))
    inicioy = str(round(mediapantallay) +1 )
    print(f"\033[{inicioy};{iniciox}H",VERSION_Y_AUTOR)
    mensaje = f"Pulsa una tecla para continuar..."
    print(RESET)
    iniciox = str(round(mediapantallax-len(mensaje)/2))
    inicioy = str(round(mediapantallay) +2 )
    print(f"{AMARILLO}\033[{inicioy};{iniciox}H{RESET}",mensaje)
    input()
