import os
import shutil

def arquivos_analisados(argumento):
    """
    Extrai as informacoes contidas em cada linha de um arquivo
    e as coloca em uma lista.
    O foco principal e o arquivo "backup_parm.txt"

    :param argumento: str
    :return list linhas de um arquivo 
    """
    parm = []
    if os.path.isfile(f'{argumento}.txt'):
        with open(f"{argumento}.txt") as file:
            parm = file.readlines()
            parm = [line.rstrip() for line in parm]
    return parm