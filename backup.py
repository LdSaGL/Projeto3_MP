"""
Este programa utiliza a tabela de decisao apresentada em sala para realizar um backup ou uma
restauracao
"""

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
        with open(f"{argumento}.txt", 'r', encoding='utf-8') as file:
            parm = file.readlines()
            parm = [line.rstrip() for line in parm]
    return parm


def extrator_tempo(lista_arquivos):
    """
    Recebe a lista com os arquivos em analise (retirados do arquivo parm), descobre e
    armazena a ultima data de modificacao tanto na pasta HD quanto na Pendrive.

    :param lista_arquivos: list
    :return dict tempos (data de modificacao em 'HD' e 'Pendrive')
    """
    tempos = {}
    if len(lista_arquivos) == 1:
        arquivo = lista_arquivos[0]
        if os.path.isfile(f'HD/{arquivo}.txt'):
            tempo1 = os.path.getmtime(f'D:/Projetos/Projeto3_MP/HD/{arquivo}.txt')
            tempos[arquivo] = [tempo1]
        else:
            tempos[arquivo] = ['inexistente']


        if os.path.isfile(f'Pendrive/{arquivo}.txt'):
            tempo2 = os.path.getmtime(f'D:/Projetos/Projeto3_MP/Pendrive/{arquivo}.txt')
            tempos[arquivo].append(tempo2)
        else:
            tempos[arquivo].append('inexistente')

    else:
        for termo in lista_arquivos:
            if os.path.isfile(f'HD/{termo}.txt'):
                tempo1 = os.path.getmtime(f'D:/Projetos/Projeto3_MP/HD/{termo}.txt')
                tempos[termo] = [tempo1]
            else:
                tempos[termo] = ['inexistente']


            if os.path.isfile(f'Pendrive/{termo}.txt'):
                tempo2 = os.path.getmtime(f'D:/Projetos/Projeto3_MP/Pendrive/{termo}.txt')
                tempos[termo].append(tempo2)
            else:
                tempos[termo].append('inexistente')
    return tempos


def backup(lista_arquivos):
    """
    E chamada quando a primeira linha do backup_parm for: 'backup'
    Recebe a lista com os arquivos em analise (retirados do arquivo parm), chama a funcao
    'extrator_tempo', executa a parte da tabela de decisao relacionada ao backup
    (HD para Pendrive) e retorna se deve ser feito o backup.

    :param lista_arquivos: list
    :return list tarefas mensagem de erro ou solicitacao de backup
    """
    tempos = extrator_tempo(lista_arquivos)
    tarefa = []
    for i in tempos:
        if tempos[i][0] == 'inexistente' and tempos[i][1] == 'inexistente':
            tarefa.append('Erro: arquivos nao existem em nenhum dos diretorios.')
        elif tempos[i][1] == 'inexistente':
            tarefa.append(f'Fazer backup do: {i}')
        elif tempos[i][0] != 'inexistente':
            if tempos[i][0] > tempos[i][1]:
                tarefa.append(f'Fazer backup do: {i}')
            elif tempos[i][0] < tempos[i][1]:
                tarefa.append('Erro: o arquivo do Pendrive mais recente do que o do HD.')
    return tarefa


def restore(lista_arquivos):
    """
    E chamada quando a primeira linha do backup_parm for: 'restore'
    Recebe a lista com os arquivos em analise (retirados do arquivo parm), chama a funcao
    'extrator_tempo', executa a parte da tabela de decisao relacionada a restauracao
    (Pendrive para HD) e retorna se deve ser feita a restauracao.


    :param lista_arquivos: list
    :return list tarefas mensagem de erro ou solicitacao de reatauracao
    """
    tempos = extrator_tempo(lista_arquivos)
    tarefa = []
    for j in tempos:
        if tempos[j][0] == 'inexistente' and tempos[j][1] == 'inexistente':
            tarefa.append('Erro: arquivos nao existem em nenhum dos diretorios.')
        elif tempos[j][1] == 'inexistente':
            tarefa.append('Erro: arquivo presente apenas no HD.')
        elif tempos[j][0] == 'inexistente':
            tarefa.append(f'Fazer restauracao do: {j}')
        elif tempos[j][0] > tempos[j][1]:
            tarefa.append('Erro: arquivo do HD mais recente do que o do Pendrive.')
        elif tempos[j][0] < tempos[j][1]:
            tarefa.append(f'Fazer restauracao do: {j}')
    return tarefa
