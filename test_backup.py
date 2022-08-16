from msilib.schema import Error
import backup

# 1 - Testa se a funcao consegue extrair efetivamente todas as informacoes do arquivo


def testeParm1():
    assert backup.arquivos_analisados('backup_parm_teste') == ['backup', 'arquivo1', 'arquivo2', 'arquivo3']

def testeParm2():
    assert backup.arquivos_analisados('bac') == []


# 2 - Testa se o data de modificacao obtida por meio da funcao condiz com a verdadeira

def testeTempo1():
    assert backup.extrator_tempo(('arquivo1', 'arquivo2', 'arquivo3')) == {'arquivo1': [1660614617.2689965, 1660614629.3149662], 'arquivo2': [1660616812.60954, 1660616807.5729384], 'arquivo3': ['inexistente', 1660616818.9820714]}

def testeTempo2():
    assert backup.extrator_tempo(('arq', 'arquivo1', 'sistemawin')) == {'arq': ['inexistente', 'inexistente'], 'arquivo1': [1660614617.2689965, 1660614629.3149662], 'sistemawin': ['inexistente', 'inexistente']}

def testeTempo3():
    assert backup.extrator_tempo(()) == {}