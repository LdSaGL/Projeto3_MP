import backup

# 1 - Testa se a funcao consegue extrair efetivamente todas as informacoes do arquivo


def testeParm1():
    assert backup.arquivos_analisados('backup_parm_teste') == ['backup', 'arquivo1', 'arquivo2', 'arquivo3']

def testeParm2():
    assert backup.arquivos_analisados('bac') == []

