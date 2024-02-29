def pantallaInicio(NOMBRE_PROGRAMA,VERSION_Y_AUTOR):
    AZUL = '\033[94m'
    RESET = '\033[0m'
    
    print(AZUL)
    print(f"\033[15;15H",NOMBRE_PROGRAMA)
    print(f"\033[16;15H",VERSION_Y_AUTOR)
    print(RESET)
    input(f"\033[17;15HPulsa una tecla para continuar...")
