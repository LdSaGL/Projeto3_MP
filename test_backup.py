import backup

# 1 - Testa se a funcao consegue extrair efetivamente todas as informacoes do arquivo


def testeParm1():
    assert backup.arquivos_analisados('backup_parm_teste') == ['backup', 'arquivo1', 'arquivo2', 'arquivo3']

def testeParm2():
    assert backup.arquivos_analisados('bac') == []


# 2 - Testa se o data de modificacao obtida por meio da funcao condiz com a verdadeira

def testeTempo1():
    assert backup.extrator_tempo(['arquivo1', 'arquivo2', 'arquivo3']) == {'arquivo1': [1660614617.2689965, 1660614629.3149662], 'arquivo2': [1660616812.60954, 1660616807.5729384], 'arquivo3': ['inexistente', 1660616818.9820714]}

def testeTempo2():
    assert backup.extrator_tempo(['arq', 'arquivo1', 'sistemawin']) == {'arq': ['inexistente', 'inexistente'], 'arquivo1': [1660614617.2689965, 1660614629.3149662], 'sistemawin': ['inexistente', 'inexistente']}

def testeTempo3():
    assert backup.extrator_tempo([]) == {}


# 3 - Testa se a funcao backup esta executando conforme tabela de decisao

def testeBackup1():
    assert backup.backup(['arquivo9']) == ['Erro: arquivos nao existem em nenhum dos diretorios.']

def testeBackup2():
    assert backup.backup(['arquivo4']) == ['Fazer backup do: arquivo4']

def testeBackup3():
    assert backup.backup(['arquivo1']) == ['Erro: o arquivo do Pendrive mais recente do que o do HD.']

def testeBackup4():
    assert backup.backup(['arquivo2']) == ['Fazer backup do: arquivo2']

def testeBackup5():
    assert backup.backup([]) == []

def testeBackup6():
    assert backup.backup(['arquivo3']) == []


# 4 - Testa se a funcao restauracao esta executando conforme tabela de decisao

def testeRestauracao1():
    assert backup.restore(['arquivox']) == ['Erro: arquivos nao existem em nenhum dos diretorios.']

def testeRestauracao2():
    assert backup.restore(['arquivo4']) == ['Erro: arquivo presente apenas no HD.']

def testeRestauracao3():
    assert backup.restore(['arquivo3']) == ['Fazer restauracao do: arquivo3']

def testeRestauracao4():
    assert backup.restore(['arquivo1']) == ['Fazer restauracao do: arquivo1']

def testeRestauracao5():
    assert backup.restore(['arquivo2']) == ['Erro: arquivo do HD mais recente do que o do Pendrive.']

def testeRestauracao6():
    assert backup.restore([]) == []
