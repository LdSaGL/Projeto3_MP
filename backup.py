"""
Este programa utiliza a tabela de decisao apresentada em sala para realizar um backup ou uma
restauracao
"""


import os
import shutil


"""
Assertivas de entrada
'argumento' deve ser o nome do arquivo sem a extensao '.txt'
"""
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
"""
Assertivas de saida
E garantido que 'parm' e uma lista
E garantido que parm sera vazia caso o arquivo nao exista
"""


"""
Assertivas de entrada
O len() do argumento deve ser maior que 0 
'lista_arquivos' deve conter apenas nomes de arquivos sem a extensao '.txt'
O diretorio deve ser o caminho ate a pasta com o projeto
"""
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
            tempo1 = os.path.getmtime(f'{DIRETORIO}/HD/{arquivo}.txt')
            tempos[arquivo] = [tempo1]
        else:
            tempos[arquivo] = ['inexistente']


        if os.path.isfile(f'Pendrive/{arquivo}.txt'):
            tempo2 = os.path.getmtime(f'{DIRETORIO}/Pendrive/{arquivo}.txt')
            tempos[arquivo].append(tempo2)
        else:
            tempos[arquivo].append('inexistente')

    else:
        for termo in lista_arquivos:
            if os.path.isfile(f'HD/{termo}.txt'):
                tempo1 = os.path.getmtime(f'{DIRETORIO}/HD/{termo}.txt')
                tempos[termo] = [tempo1]
            else:
                tempos[termo] = ['inexistente']


            if os.path.isfile(f'Pendrive/{termo}.txt'):
                tempo2 = os.path.getmtime(f'{DIRETORIO}/Pendrive/{termo}.txt')
                tempos[termo].append(tempo2)
            else:
                tempos[termo].append('inexistente')
    return tempos
"""
E garantido que a funcao retorna um dicionario 'tempos'
E garantido que as chaves do dicionario sao os nomes dos arquivos contidos no parm
E garantido que os valores de cada chave sao listas com dois termos
E garantido que os termos sao um float ou a string 'inexistente'
"""


"""
Assertivas de entrada
'backup_parm[0]' deve ser 'backup'
'lista_arquivos' deve conter todos os termos de 'backup_parm' excluindo o primeiro
A funcao 'extrator_tempo(lista)' deve retornar um dict
"""
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
"""
Assertivas de saida
E garantido que 'tarefa' e uma lista
E garantido que, caso a acao seja nao fazer nada, nada sera adicionado
E garantido que sera passado integralmente para a lista o respectivo erro ou o que deve
ser feito com qual arquivo
"""


"""
Assertivas de entrada
'backup_parm[0]' deve ser 'backup'
'lista_arquivos' deve conter todos os termos de 'backup_parm' excluindo o primeiro
A funcao 'extrator_tempo(lista)' deve retornar um dict
"""
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
"""
Assertivas de saida
E garantido que 'tarefa' e uma lista
E garantido que, caso a acao seja nao fazer nada, nada sera adicionado
E garantido que sera passado integralmente para a lista o respectivo erro ou o que deve
ser feito com qual arquivo
"""


DIRETORIO = 'D:/Projetos/Projeto3_MP' #informar o diretorio onde a pasta do projeto esta localizada
arquivos_parm = arquivos_analisados('backup_parm') #informar qual o nome do arquivo de instrucao

"""
Segmento do codigo que verifica se deve ser realizado um backup ou uma restauracao, chama as
respectivas funcoes e realiza a copia do arquivo caso necessario
"""
if len(arquivos_parm) > 0:
    if arquivos_parm[0] == 'backup':
        lista_mensagens = backup(arquivos_parm[1:])
        CONTADOR = 1
        for item in lista_mensagens:
            print(item)
            if item == f'Fazer backup do: {arquivos_parm[CONTADOR]}':
                shutil.copy2(f'{DIRETORIO}/Pendrive/{arquivos_parm[CONTADOR]}.txt',
                f'{DIRETORIO}/HD/{arquivos_parm[CONTADOR]}.txt')
            CONTADOR += 1
    elif arquivos_parm[0] == 'restore':
        lista_mensagens = restore(arquivos_parm[1:])
        CONTADOR = 1
        for item in lista_mensagens:
            print(item)
            if item == f'Fazer restauracao do: {arquivos_parm[CONTADOR]}':
                shutil.copy2(f'{DIRETORIO}/HD/{arquivos_parm[CONTADOR]}.txt',
                f'{DIRETORIO}/Pendrive/{arquivos_parm[CONTADOR]}.txt')
            CONTADOR += 1
    else:
        print('Erro: nao foi seguido o padrao de construcao do arquivo de instrucao')
else:
    print('Erro: nao foi informado nada no arquivo de instrucao')
