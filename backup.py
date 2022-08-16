import os
import shutil

def arquivos_analisados(argumento):
    """
    Extrai as informacoes contidas em cada linha de um arquivo
    e as coloca em uma lista.
    O foco principal e o arquivo "backup_parm.txt"

    :param argumento: str
    :return list parm (linhas de um arquivo)
    """
    parm = []
    if os.path.isfile(f'{argumento}.txt'):
        with open(f"{argumento}.txt") as file:
            parm = file.readlines()
            parm = [line.rstrip() for line in parm]
    return parm


def extrator_tempo(lista_arquivos):
    """
    Recebe a lista com os arquivos em analise (retirados do arquivo parm), descobre e
    armazena a ultima data de modificacao tanto na pasta HD quanto na Pendrive.

    :param arquivos: list
    :return dict tempos (data de modificacao em 'HD' e 'Pendrive')
    """
    tempos = {}
    for termo in lista_arquivos:
        if os.path.isfile(f'HD/{termo}.txt'):
            hd_file = open(f'HD/{termo}.txt')
            tempo1 = os.path.getmtime(f'D:/Projetos/Projeto3_MP/HD/{termo}.txt')
            hd_file.close()
            tempos[termo] = [tempo1]
        else:
            tempos[termo] = ['inexistente']


        if os.path.isfile(f'Pendrive/{termo}.txt'):
            pendrive_file = open(f'Pendrive/{termo}.txt')
            tempo2 = os.path.getmtime(f'D:/Projetos/Projeto3_MP/Pendrive/{termo}.txt')
            pendrive_file.close()
            tempos[termo].append(tempo2)
        else:
            tempos[termo].append('inexistente')
    return tempos

print(extrator_tempo(('arquivo1', 'arquivo2', 'arquivo3')))